from flask import Blueprint, request, jsonify
from ..services import resume_service
from ..types import TrainModelRequest, ChatCompletionRequest

bp = Blueprint('resume', __name__, url_prefix='/resume')

@bp.route("/train_model", methods=['POST']) 
async def train_model():
    data = request.get_json()
    train_model_request = TrainModelRequest(**data)
    response = await resume_service.train_model(train_model_request)
    return jsonify(response.to_dict()), 200

@bp.route("/chat_completion", methods=['POST'])
def chat_completion():
    
    data = request.get_json();
    chat_completion_request = ChatCompletionRequest(**data)
    response = resume_service.chat_completion(chat_completion_request)
    return jsonify(response.to_dict()), 200
