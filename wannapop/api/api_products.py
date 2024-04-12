from . import api_bp
from .helper_auth import token_auth
from ..models import Product, Category, Status, BannedProduct, Order, ConfirmedOrder
from .helper_json import json_request, json_response
from .errors import not_found, bad_request, forbidden_access
from flask import request
from .. import logger

# List
@api_bp.route('/products', methods=['GET'])
def get_products():
    search = request.args.get('title')
    if search:
        # Watch SQL at terminal
        Product.db_enable_debug()
        # Filter using query param
        my_filter = Product.title.like('%' + search + '%')
        products = Product.db_query_with(join_cls=Category,outerjoin_cls=BannedProduct).filter(my_filter)
    else:
        # No filter
        products = Product.get_all_with(join_cls=Category,outerjoin_cls=BannedProduct)
    data = Product.to_dict_collection(products)
    return json_response(data)

# Read
@api_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    result = Product.get_with(product_id, join_cls=[Category, Status], outerjoin_cls=BannedProduct)
    if result:
        (product, category, status, banned) = result
        # Serialize data
        data = product.to_dict()
        # Add relationships
        data["category"] = category.to_dict()
        del data["category_id"]
        data["status"] = status.to_dict()
        del data["status_id"]
        if (banned):
            data["banned"] = banned.to_dict()
            del data["banned_id"]
        return json_response(data)
    else:
        logger.debug("Product {} not found".format(id))
        return not_found("Product not found")

# Update
@api_bp.route('/products/<int:product_id>', methods=['PUT'])
@token_auth.login_required
def update_product(product_id):
    product = Product.get(product_id)

    if not product:
        logger.debug("Product {} not found".format(product_id))
        return not_found("Product not found")

    if (product.seller_id != token_auth.current_user().id):
        return forbidden_access("You are not the owner of this product")

    try:
        data = json_request(['title', 'description', 'photo', 'price', 'category_id', 'status_id'], False)
    except Exception as e:
        logger.debug(e)
        return bad_request(str(e))
    else:
        product.update(**data)
        logger.debug("UPDATED product: {}".format(product.to_dict()))
        return json_response(product.to_dict())

# Orders list
@api_bp.route('/products/<int:product_id>/orders', methods=['GET'])
@token_auth.login_required
def get_product_orders(product_id):
    orders = Order.get_all_filtered_by(product_id=product_id)
    data = Order.to_dict_collection(orders)
    return json_response(data)
