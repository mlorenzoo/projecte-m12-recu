from . import api_bp
from ..models import User, BlockedUser, Product
from .helper_json import json_response
from .errors import not_found
from .. import logger
from flask import request

# List
@api_bp.route('/users', methods=['GET'])
def get_users():
    search = request.args.get('name')
    if search:
        # Watch SQL at terminal
        User.db_enable_debug()
        # Filter using query param
        my_filter = User.name.like('%' + search + '%')
        users = User.db_query_with(join_cls=[], outerjoin_cls=BlockedUser).filter(my_filter)
    else:
        # No filter
        users = User.get_all_with(join_cls=[], outerjoin_cls=BlockedUser)
    data = User.to_dict_collection(users)
    return json_response(data)

# Read
@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get(user_id)
    if user:
        # Serialize data
        data = user.to_dict()
        return json_response(data)
    else:
        logger.debug("Product {} not found".format(id))
        return not_found("Product not found")

# Orders list
@api_bp.route('/users/<int:user_id>/products', methods=['GET'])
def get_user_products(user_id):
    products = Product.get_all_filtered_by(seller_id=user_id)
    data = Product.to_dict_collection(products)
    return json_response(data)
