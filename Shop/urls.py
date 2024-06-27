try:
    # імпорт необхідних бібліотек
    import home_page
    import authorization_page
    import registration_page
    import shop_page
    import cart_page
    import admin_app
    from .settings import shop_app

    # додавання нової сторінки 
    home_page.home.add_url_rule(
        # посилання на сторінку
        rule = "/",
        # функція для відображення сторінки
        view_func = home_page.render_home
    )

    authorization_page.auth.add_url_rule(
        rule = '/auth',
        view_func = authorization_page.render_auth,
        # методи які використовує сторінка 
        methods = ["GET", "POST"]
    )

    registration_page.reg.add_url_rule(
        rule = '/registration',
        view_func = registration_page.render_reg,
        methods = ["GET", "POST"]
    )

    shop_page.shop.add_url_rule(
        rule = "/shop",
        view_func = shop_page.render_shop
    )
    cart_page.cart.add_url_rule(
        rule="/cart",
        view_func = cart_page.render_cart,
        methods = ["GET", "POST"]
    )

    admin_app.admin.add_url_rule(
        rule = "/admin/", 
        view_func = admin_app.render_admin, 
        methods = ["GET","POST"]
    )

    shop_app.register_blueprint(
        blueprint = home_page.home
    )
    shop_app.register_blueprint(
        blueprint = authorization_page.auth
    )
    shop_app.register_blueprint(
        blueprint = registration_page.reg
    )
    shop_app.register_blueprint(
        blueprint = shop_page.shop
    )
    shop_app.register_blueprint(
        blueprint = cart_page.cart
    )
    shop_app.register_blueprint(
        blueprint = admin_app.admin
    )
except Exception as error:
    print(error)