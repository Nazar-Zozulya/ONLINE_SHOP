try:
    # імпорт необхідних бібліотек
    import flask
    import os
    import flask_sqlalchemy
    import flask_migrate

    # створення головного додатку
    shop_app = flask.Flask(
        import_name = "Shop",
        template_folder = "templates",
        static_folder = "static",
        instance_path = os.path.abspath(__file__ + "/.."),
        static_url_path = "/shop_app/"
    )

    # конфігурація бази даних
    shop_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" 

    # ініціалізація бази даних
    DATABASE = flask_sqlalchemy.SQLAlchemy(app = shop_app)
    # ініціалізація міграцій
    MIGRATE = flask_migrate.Migrate(app = shop_app, db = DATABASE)
except Exception as error:
    print(error)