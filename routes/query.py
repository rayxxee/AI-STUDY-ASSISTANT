from flask import Blueprint, request, jsonify
from routes.upload import vector_store
from rag.retriever import retrieve_context
from rag.generator import generate_answer

query_bp = Blueprint('query', __name__)

@query_bp.route('/query', methods=['POST'])
def query_endpoint():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'Missing question in request body'}), 400
        
    question = data['question']
    
    # 1. Retrieve context
    try:
        contexts = retrieve_context(question, vector_store, top_k=3)
    except Exception as e:
        return jsonify({'error': f'Retrieval failed: {str(e)}'}), 500
        
    # 2. Generate Answer
    try:
        answer = generate_answer(question, contexts)
    except Exception as e:
        return jsonify({'error': f'Generation failed: {str(e)}'}), 500
        
    # Format contexts for the response payload to show what was retrieved
    formatted_contexts = [{"text": ctx["text"], "distance": ctx["distance"]} for ctx in contexts]
    
    return jsonify({
        'answer': answer,
        'context_used': formatted_contexts
    }), 200
