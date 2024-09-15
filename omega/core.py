def create_app():
    from flask import Flask

    omega = Flask(__name__)

    from omega.config.setup import Config

    omega.config.from_object(Config)

    from omega.config.boost import login_manager
    from omega.mold.models import Professor

    login_manager.init_app(omega)

    @login_manager.user_loader
    def load_user(taxnr):
        return Professor.query.get(taxnr)

    from omega.config.boost import db

    db.init_app(omega)

    from omega.config.boost import migrate

    migrate.init_app(omega, db)

    from omega.config.boost import mail

    mail.init_app(omega)

    from omega.home.routes import bp_home_routes

    omega.register_blueprint(bp_home_routes, url_prefix="/")

    from omega.auth.routes import bp_auth_routes

    omega.register_blueprint(bp_auth_routes, url_prefix="/auth")

    from omega.user.routes import bp_user_routes

    omega.register_blueprint(bp_user_routes, url_prefix="/user")

    return omega


omega = create_app()
