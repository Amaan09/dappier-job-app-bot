from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from .routes import resume

load_dotenv()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    # Register blueprints
    app.register_blueprint(resume.bp)

    return app
