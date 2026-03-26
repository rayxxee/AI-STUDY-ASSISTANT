from flask import Blueprint, request, jsonify
from routes.upload import vector_store
from rag.retriever import retrieve_context
from rag.generator import generate_answer
from memory.chat_memory import memory_store
from rag.rewriter import rewrite_query

query_bp = Blueprint('query', __name__)

@query_bp.route('/query', methods=['POST'])
def query_endpoint():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'Missing question in request body'}), 400
        
    question = data['question']
    
    # 1. Get current chat history string
    chat_history_str = memory_store.format_history_string()
    
    # 2. Rewrite Query (Phase 3)
    try:
        rewritten_question = rewrite_query(question, chat_history_str)
    except Exception as e:
        print(f"Warning: Rewriter failed, using original: {e}")
        rewritten_question = question
    
    # 3. Retrieve context using standard/rewritten query
    try:
        contexts = retrieve_context(rewritten_question, vector_store, top_k=3)
    except Exception as e:
        return jsonify({'error': f'Retrieval failed: {str(e)}'}), 500
        
    # 4. Generate Answer
    try:
        answer = generate_answer(question, contexts, chat_history_str)
    except Exception as e:
        return jsonify({'error': f'Generation failed: {str(e)}'}), 500
        
    # 5. Save to Memory
    memory_store.add_message("user", question)
    memory_store.add_message("assistant", answer)
        
    # Format contexts for the response payload to show what was retrieved
    formatted_contexts = [{"text": ctx["text"], "distance": ctx["distance"]} for ctx in contexts]
    
    return jsonify({
        'original_question': question,
        'rewritten_question': rewritten_question,
        'answer': answer,
        'context_used': formatted_contexts
    }), 200
