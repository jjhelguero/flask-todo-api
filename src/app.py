from flask import Flask
from flask_smorest import Api
from src.config.config import APIConfig
from src.api.routes.todo import todo

def create_app():
    app = Flask(__name__)
    app.config.from_object(APIConfig)
    
    api = Api(app)
    api.register_blueprint(todo)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()