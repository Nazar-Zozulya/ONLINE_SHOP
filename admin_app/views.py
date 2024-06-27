try:       
        import flask 
        from shop_page.models import *
        import os
        from Shop.settings import DATABASE
        from flask_login import current_user
        def render_admin():
                # подулаем cookies
                cookies = flask.request.cookies.get('product')
                if cookies:
                        cookies = cookies.split(' ')
                        cookies = len(cookies)
                else:
                        cookies = 0
                # робимо умову якщо кнопка нажата
                if flask.request.method == "POST":
                        # якщо кнопки del нажата видаляємл продукт
                        if flask.request.form.get('del'):
                                product_id = int(flask.request.form['del'])
                                product_delete = Product.query.get(product_id)
                                if product_delete is not None:
                                    DATABASE.session.delete(product_delete)
                                    DATABASE.session.commit()
                                    path = os.path.abspath(__file__ + f'/../../shop_page/static/image/{product_delete.name}.png')
                                    os.remove(path)
                        

                        # якщо кнопки submit-change нажата то змінюємл данні продукту і обновляємо його з новими данними і сохраняємо у баззу данних
                        elif flask.request.form.get("submit-change"):
                                list_data = flask.request.form['submit-change'].split('-')
                                product = Product.query.get(int(list_data[1]))
                                path = os.path.abspath(__file__ + f"/../../shop_page/static/image/{product.name}.png")
                                print("edit data")
                                # якшо ио вибрали name от ми змінюємо назву подукту а також змінюмо назву картинки цього продукту
                                if "name" == list_data[0]:
                                        product_name = flask.request.form['name']
                                        path_image = os.path.abspath(__file__ + f"/../../shop_page/static/image/{product_name}.png")
                                        os.rename(path,  path_image)
                                        product.name =  product_name
                                        DATABASE.session.commit()
                                # якшо ми змінємо картинку то  додаємо нову картинку а стару увидаляємо
                                elif "image" == list_data[0]:
                                        os.remove(path)
                                        img = flask.request.files["image"]
                                        img.save(path)
                                # якощо ми змінюємо ціну то ми змінюємо ціну на ту яку ми вказали в полі 
                                elif "price" == list_data[0]:
                                        product_price = flask.request.form['price']
                                        product.price =  product_price
                                        DATABASE.session.commit()
                                # якощо ми змінюємо скидку то ми змінюємо скидку на ту яку ми вказали в полі 
                                elif "sale" == list_data[0]:
                                        product_sale = flask.request.form['sale']
                                        product.sale = product_sale
                                        DATABASE.session.commit()
                                # якощо ми змінюємо стару ціну то ми змінюємо стару ціну на ту яку ми вказали в полі 
                                elif "previous_price" == list_data[0]:
                                        product_previous_price = flask.request.form['previous_price']
                                        product.previous_price = product_previous_price
                                        DATABASE.session.commit()

                        else:
                                product = Product(
                                        name = flask.request.form['name'],
                                        price = flask.request.form['price'],
                                        sale = flask.request.form['sale'],
                                        count = flask.request.form['count'],
                                        previous_price = flask.request.form['previous_price'],
                                )
                                DATABASE.session.add(product)
                                DATABASE.session.commit()
                                image = flask.request.files['image']
                                image.save(os.path.abspath(__file__ + f"/../../shop_page/static/image/{product.name}.png"))
                # робимо перевірку на являється цей юзер адміном
                is_name = False
                is_authenticated = False
                is_admin = False
                if current_user.is_authenticated:
                        is_admin = current_user.is_admin
                        is_authenticated = True
                        is_name = current_user.name
                # якщо від адмін виводемо цю сторвнку
                if is_admin:
                        return flask.render_template(
                        template_name_or_list = "admin.html", products = Product.query.all(), cookies = cookies, is_name = is_name, is_authenticated = is_authenticated, is_admin = is_admin
                )
                # якщо не кидажмо йог она головну
                else:
                        return flask.redirect('/')
except Exception as error:
        print(error)
        
