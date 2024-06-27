try:
    import flask
    from shop_page.models import Product
    from flask_login import current_user
    from flask_mail import Message
    from Shop.mail_config import ADMINISTRATION_ADRESS, mail
    from .models import Cart
    from Shop.settings import DATABASE

    def render_cart():
        products = []
        
        is_name = False
        is_authenticated = False
        is_admin = False
        if current_user.is_authenticated:
            is_admin = current_user.is_admin
            is_authenticated = True
            is_name = current_user.name

        cookies = flask.request.cookies.get('product')
        if cookies:
            cookies = cookies.split(' ')
            cookies = len(cookies)
        else:
            cookies = 0
        # якщо в cookies є продукт получаємо всі продуктии
        # if 'product' in flask.request.cookies:
        id_products = flask.request.cookies.get('product').split(' ')
        
        ids = []
        # робимо цикл на вивід всіх продуктів у корзину
        for id in id_products:
            if not id in ids:
                count_products = id_products.count(id)
                ids.append(id)
                products.append(Product.query.get(id))
                print(count_products)

                print(flask.request.cookies.get('product'))
                len_products = len(id_products)
                print(flask.request.cookies)
                print(len(id_products))
                try:
                    products[-1].count = count_products
                except:
                    return flask.render_template(template_name_or_list = "cart2.html", is_authenticated = is_authenticated, is_name = is_name, is_admin = is_admin, cookies = cookies)
                if flask.request.method == "POST":
                    # додаємо продукти до моделі корзини
                    product_cart = Cart(name = flask.request.form['name'], surname = flask.request.form['surname'], number = flask.request.form['number'], email = flask.request.form['email'], city = flask.request.form['city'], post_office = flask.request.form['post_office'], additional_wish = flask.request.form['additional_wish'], status = False)
                    print(product_cart)
                    DATABASE.session.add(product_cart)
                    DATABASE.session.commit()
                    
                    message_text = "Замовлення було оформлене:\n\n"
                    # виводимо інформацію про продукти на пошту
                    for product in products:
                        message_text += f"Назва - {product.name}\nЦіна - {product.price}\nЗнижка - {product.sale}\nЧисло - {product.count}\n\nДякую за замовлення ❤️"
                    message = Message(
                        "Замовлення", 
                        sender = ADMINISTRATION_ADRESS, 
                        recipients = [current_user.email],
                        body = message_text
                    )
                    mail.send(message)
        return flask.render_template(template_name_or_list = "cart.html", products = products, cookies = cookies, is_authenticated = is_authenticated, is_name = is_name, is_admin = is_admin, len_products = len_products)
except Exception as error:
    print(error)