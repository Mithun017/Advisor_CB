from flask import Blueprint, request, jsonify
from services.gemini import get_gemini_response, get_embedding
from services.memory import store_memory, retrieve_memories
from services.github_api import fetch_repos_by_language

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_id = data['user_id']
    query = data['query']

    embedding = get_embedding(query)
    store_memory(user_id, query, embedding, metadata={})

    previous_context = retrieve_memories(user_id).data
    response = get_gemini_response(f"User: {query}\n\nContext: {previous_context}")
    
    return jsonify({"response": response})
