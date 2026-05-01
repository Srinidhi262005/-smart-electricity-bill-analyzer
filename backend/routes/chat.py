from flask import Blueprint, request, jsonify
from services.chatbot_service import respond_to_message

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/chat', methods=['POST'])
def chat():
    """Handle user chatbot requests in English and Telugu."""
    payload = request.get_json(force=True)
    message = payload.get('message', '')
    lang = payload.get('lang', 'en')

    if not message:
        return jsonify({'error': 'Message is required.'}), 400

    response = respond_to_message(message, lang)
    return jsonify({'success': True, 'response': response})
