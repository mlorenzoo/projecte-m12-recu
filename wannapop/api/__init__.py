from flask import Blueprint

api_bp = Blueprint('api', __name__)

# necessari per a que es carreguin les rutes
from . import errors, helper_auth, api_tokens, api_category, api_status, api_products, api_users, api_orders