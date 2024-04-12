from . import api_bp
from ..models import Status
from .helper_json import json_response

# List
@api_bp.route('/statuses', methods=['GET'])
def get_statuses():
    statuses = Status.get_all()
    data = Status.to_dict_collection(statuses)
    return json_response(data)
