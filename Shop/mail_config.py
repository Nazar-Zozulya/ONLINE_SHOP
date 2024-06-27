try:
    import flask_mail
    from .settings import shop_app
    ADMINISTRATION_ADRESS = "shoponlinee26@gmail.com"
    ADMINISTRATION_PASSWORD = "cfxs youx qhhe nkzu"
    # налаштування SMTP сервера для відправки повідомлен
    shop_app.config["MAIL_SERVER"] = "smtp.gmail.com"
    # налаштування порту
    shop_app.config["MAIL_PORT"] = 587
    # використання TLS для безпечного зв'язку
    shop_app.config["MAIL_USE_TLS"] = True
    # налаштування логіну та паролю для входу до SMTP сервера
    shop_app.config["MAIL_USERNAME"] = ADMINISTRATION_ADRESS
    shop_app.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD
    # створення об'єкту для відправки повідомлень
    mail = flask_mail.Mail(app = shop_app)
except Exception as error:
    print(error)