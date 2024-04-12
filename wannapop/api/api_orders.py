from . import api_bp
from .helper_auth import token_auth
from ..models import Order, ConfirmedOrder, Product
from .helper_json import json_request, json_response
from .errors import not_found, bad_request, forbidden_access, internal_error
from .. import logger

# Create
@api_bp.route('/orders', methods=['POST'])
@token_auth.login_required
def create_order():
    try:
        data = json_request(['product_id', 'offer'])
    except Exception as e:
        logger.debug(e)
        return bad_request(str(e))
    else:
        data['buyer_id'] = token_auth.current_user().id
        order = Order.create(**data)
        if (order):
            logger.debug("CREATED order: {}".format(order.to_dict()))
            return json_response(order.to_dict(), 201)
        else:
            logger.debug("CREATE order FAILED: {}".format(data))
            return internal_error("Sorry. Unable to create order.")

# Update
@api_bp.route('/orders/<int:order_id>', methods=['PUT'])
@token_auth.login_required
def update_orders(order_id):
    result = Order.get_with(order_id, join_cls=[], outerjoin_cls=ConfirmedOrder)

    if not result:
        logger.debug("Order {} not found".format(order_id))
        return not_found("Order not found")
    
    (order, confirmed_order) = result
    if (order.buyer_id != token_auth.current_user().id):
        return forbidden_access("You are not the owner of this order")

    if confirmed_order:
        return bad_request("Order already confirmed")

    try:
        data = json_request(['offer'], False)
    except Exception as e:
        logger.debug(e)
        return bad_request(str(e))
    else:
        order.update(**data)
        logger.debug("UPDATED order: {}".format(order.to_dict()))
        return json_response(order.to_dict())

# Delete
@api_bp.route('/orders/<int:order_id>', methods=['DELETE'])
@token_auth.login_required
def delete_order(order_id):
    result = Order.get_with(order_id, join_cls=[], outerjoin_cls=ConfirmedOrder)

    if not result:
        logger.debug("Order {} not found".format(order_id))
        return not_found("Order not found")
    
    (order, confirmed_order) = result
    if (order.buyer_id != token_auth.current_user().id):
        return forbidden_access("You are not the owner of this order")

    if confirmed_order:
        return bad_request("Order already confirmed")
    
    order.delete()
    logger.debug("DELETED order: {}".format(order_id))
    return json_response(order.to_dict())

# Accept order
@api_bp.route('/orders/<int:order_id>/confirmed', methods=['POST'])
@token_auth.login_required
def create_confirmed_order(order_id):
    result = Order.get_with(order_id, join_cls=Product, outerjoin_cls=ConfirmedOrder)

    if not result:
        logger.debug("Order {} not found".format(order_id))
        return not_found("Order not found")

    (_, product, confirmed_order) = result
    if (product.seller_id != token_auth.current_user().id):
        return forbidden_access("You are not the owner of this product")

    if confirmed_order:
        logger.debug("Order {} already confirmed".format(order_id))
        return bad_request("Order already confirmed")
    
    new_confirmed_order = ConfirmedOrder.create(order_id=order_id)
    if (new_confirmed_order):
        logger.debug("CREATED confirmed_order: {}".format(new_confirmed_order.to_dict()))
        return json_response(new_confirmed_order.to_dict(), 201)
    else:
        logger.debug("CREATE confirmed_order FAILED: {}".format(order_id))
        return internal_error("Sorry. Unable to confirm order.")

# Decline order
@api_bp.route('/orders/<int:order_id>/confirmed', methods=['DELETE'])
@token_auth.login_required
def delete_confirmed_order(order_id):
    result = Order.get_with(order_id, join_cls=Product, outerjoin_cls=ConfirmedOrder)

    if not result:
        logger.debug("ConfirmedOrder {} not found".format(order_id))
        return not_found("ConfirmedOrder not found")
    
    (_, product, confirmed_order) = result
    if not confirmed_order:
        logger.debug("ConfirmedOrder {} not found".format(order_id))
        return not_found("ConfirmedOrder not found")

    if (product.seller_id != token_auth.current_user().id):
        return forbidden_access("You are not the owner of this product")
    
    confirmed_order.delete()
    logger.debug("DELETED confirmed_order: {}".format(confirmed_order.to_dict()))
    return json_response(confirmed_order.to_dict())
