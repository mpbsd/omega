def create_app():
    from flask import Flask

    omega = Flask(__name__)

    from omega.conf.setup import Config

    omega.config.from_object(Config)

    from omega.conf.boost import login_manager
    from omega.mold.models import Professor

    login_manager.init_app(omega)

    @login_manager.user_loader
    def load_user(taxnr):
        return Professor.query.get(taxnr)

    from omega.conf.boost import db

    db.init_app(omega)

    from omega.conf.boost import migrate

    migrate.init_app(omega, db)

    from omega.conf.boost import mail

    mail.init_app(omega)

    from omega.home.routes import bp_home_routes

    omega.register_blueprint(bp_home_routes, url_prefix="/")

    from omega.auth.routes import bp_auth_routes

    omega.register_blueprint(bp_auth_routes, url_prefix="/auth")

    from omega.user.routes import bp_user_routes

    omega.register_blueprint(bp_user_routes, url_prefix="/user")

    return omega


omega = create_app()
