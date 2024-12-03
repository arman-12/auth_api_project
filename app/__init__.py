from flask import Flask
from config import Config
from .models import db, bcrypt
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    from .views import views_blueprint
    from .controllers import controllers_blueprint

    app.register_blueprint(views_blueprint)
    app.register_blueprint(controllers_blueprint)

    return app
