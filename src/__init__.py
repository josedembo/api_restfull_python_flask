from flask import Flask
import os
from dotenv import find_dotenv, load_dotenv
from src.routes.user import user

load_dotenv(find_dotenv())

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    
    if test_config is None:
        app.config.from_mapping(
            SECRETE_KEY=os.environ.get("SECRET_KEY")
        )
    else:
        app.config.from_mapping(test_config)
    
    app.register_blueprint(user)
    
    return app