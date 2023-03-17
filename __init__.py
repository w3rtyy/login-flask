from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "asdasdasdsdf"
    
    from itp.routes import views
    app.register_blueprint(views)
    
    return app