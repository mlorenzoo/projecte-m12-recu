from . import api_bp
from ..models import Category
from .helper_json import json_response

# List
@api_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.get_all()
    data = Category.to_dict_collection(categories)
    return json_response(data)
