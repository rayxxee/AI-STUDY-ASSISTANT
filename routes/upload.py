import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from utils.text_processing import extract_text, chunk_text
from rag.embeddings import get_embeddings
from rag.vector_store import VectorStore

upload_bp = Blueprint('upload', __name__)

UPLOAD_FOLDER = 'temp_uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}

vector_store = VectorStore()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)
        
        # 1. Extraction
        file_ext = filename.rsplit('.', 1)[1].lower()
        text = extract_text(filepath, file_ext)
        if not text.strip():
            return jsonify({'error': 'Failed to extract text or file is empty'}), 400
            
        # 2. Chunking
        chunks = chunk_text(text, chunk_size=400, overlap=50)
        
        # 3. Embeddings & Storage
        try:
            embeddings = get_embeddings(chunks)
            vector_store.add_texts(chunks, embeddings)
        except Exception as e:
            import traceback
            traceback.print_exc()
            return jsonify({'error': f'Failed during embedding generation: {str(e)}'}), 500
            
        # Cleanup
        try:
            os.remove(filepath)
        except:
            pass
            
        return jsonify({
            'message': 'File successfully processed and ingested into vector database.', 
            'filename': filename,
            'chunks_added': len(chunks)
        }), 200
        
    return jsonify({'error': 'File type not allowed'}), 400
