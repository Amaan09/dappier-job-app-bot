import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
import hmac
import hashlib
from .routes import resume

load_dotenv()

DAPPIER_BOT_API_SECRET = os.getenv('DAPPIER_BOT_API_SECRET')

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    # Middleware to validate HMAC signature
    @app.before_request
    def validate_signature():
        signature = request.headers.get('X-Signature')

        if not signature:
            return jsonify({'error': 'Signature missing'}), 401

        if not DAPPIER_BOT_API_SECRET:
            return jsonify({'error': 'API secret key missing'}), 401

        expected_signature = hmac.new(DAPPIER_BOT_API_SECRET.encode(), digestmod=hashlib.sha256).hexdigest()

        if not hmac.compare_digest(signature, expected_signature):
            return jsonify({'error': 'Unauthorized access'}), 401

    # Register blueprints
    app.register_blueprint(resume.bp)

    return app
