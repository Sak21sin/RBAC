from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize the SQLAlchemy instance with the app
    db.init_app(app)
    jwt = JWTManager(app)

    # Register Blueprints
    from routes.auth import auth_bp
    from routes.admin import admin_bp
    from routes.moderator import moderator_bp
    from routes.user import user_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(moderator_bp, url_prefix='/moderator')
    app.register_blueprint(user_bp, url_prefix='/user')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
