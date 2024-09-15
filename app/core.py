def create_app():
    from flask import Flask

    omega = Flask(__name__)

    from app.config.setup import Config

    app.config.from_object(Config)

    from app.config.boost import login_manager
    from app.mold.models import Professor

    login_manager.init_app(omega)

    @login_manager.user_loader
    def load_user(taxnr):
        return Professor.query.get(taxnr)

    from app.config.boost import db

    db.init_app(omega)

    from app.config.boost import migrate

    migrate.init_app(omega, db)

    from app.config.boost import mail

    mail.init_app(omega)

    from app.home.routes import bp_home_routes

    app.register_blueprint(bp_home_routes, url_prefix="/")

    from app.auth.routes import bp_auth_routes

    app.register_blueprint(bp_auth_routes, url_prefix="/auth")

    from app.user.routes import bp_user_routes

    app.register_blueprint(bp_user_routes, url_prefix="/user")

    return omega


omega = create_app()
