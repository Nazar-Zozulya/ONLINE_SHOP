try:
    import flask
    import flask_login
    from registration_page.models import User

    def render_auth():
        # отримуємо cookies
        cookies = flask.request.cookies.get('product')
        if cookies:
            cookies = cookies.split(' ')
            cookies = len(cookies)
        else:
            cookies = 0
        # робимо  умову на те якщо користувач зареєстрован і перекидуємо його на головну сторінку
        if flask_login.current_user.is_authenticated:
            return flask.render_template(template_name_or_list = "home.html")
        # якщо ні то ми логиннимо користувача і перекидуємо його на головну сторінку
        else:
            if flask.request.method == 'POST':
                for user in User.query.filter_by(name = flask.request.form["name"]):
                        flask_login.login_user(user)
                        return flask.redirect('/')
                
            return flask.render_template(template_name_or_list = "authorization.html",cookies = cookies)
except Exception as error:
    print(error)