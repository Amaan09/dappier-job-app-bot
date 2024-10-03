from flask import Flask
from .routes import resume
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Register blueprints
    app.register_blueprint(resume.bp)

    return app