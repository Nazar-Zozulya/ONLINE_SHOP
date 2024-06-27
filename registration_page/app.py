try:
    import flask

    reg = flask.Blueprint(
        name = "reg",
        import_name = "registration_page",
        template_folder = "templates",
        static_folder = "static",
        static_url_path = "/registration/"
    )
except Exception as error:
    print(error)