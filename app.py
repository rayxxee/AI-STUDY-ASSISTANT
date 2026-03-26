from flask import Flask
from routes.upload import upload_bp
from routes.query import query_bp
from routes.summary import summary_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(upload_bp)
    app.register_blueprint(query_bp)
    app.register_blueprint(summary_bp)
    
    @app.route('/health')
    def health():
        return {"status": "ok"}
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
