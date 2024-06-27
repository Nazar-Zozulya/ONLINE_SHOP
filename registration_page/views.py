try:
    import flask
    from .models import User
    from Shop.settings import DATABASE

    def render_reg():
        cookies = flask.request.cookies.get('product')
        if cookies:
            cookies = cookies.split(' ')
            cookies = len(cookies)
        else:
            cookies = 0
        is_registration = False
        # перевірка, чи відправлено форму 
        if flask.request.method == 'POST':
            # створення нового користувача з введеними даним
            user = User(name = flask.request.form['name'], password = flask.request.form['password'], email = flask.request.form['email'], is_admin = False)
            print(User.query.all())
            DATABASE.session.add(user)
            DATABASE.session.commit()
            is_registration = True
            # перенаправлення на головну сторінку
            return flask.redirect('/')

        return flask.render_template(template_name_or_list = 'registration.html',cookies=cookies, is_registration = is_registration)
except Exception as error:
    print(error)