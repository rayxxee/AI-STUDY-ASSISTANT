import os
import google.generativeai as genai
from flask import Blueprint, jsonify
from routes.upload import vector_store

summary_bp = Blueprint('summary', __name__)

@summary_bp.route('/summarize', methods=['GET'])
def summarize_endpoint():
    """
    Extracts all loaded texts from the vector store (up to a limit)
    and uses Gemini to generate a high-level 5-bullet-point summary.
    """
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        return jsonify({'error': 'GEMINI_API_KEY is not set.'}), 500
        
    if not hasattr(vector_store, 'texts') or not vector_store.texts:
        return jsonify({'error': 'No documents have been uploaded yet.'}), 404
        
    # Concatenate texts up to a reasonable limit (~30k chars for safety)
    full_text = "\n".join(vector_store.texts)[:30000]
    
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"""
You are an expert AI Study Assistant.
Please read the provided knowledge base content and generate a concise, high-level summary consisting of exactly 5 bullet points.

Knowledge Base Content:
{full_text}

Summary:
"""
    try:
        response = model.generate_content(prompt)
        return jsonify({'summary': response.text.strip()}), 200
    except Exception as e:
        return jsonify({'error': f'Generation failed: {str(e)}'}), 500
