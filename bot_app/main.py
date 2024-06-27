try:
    import os
    import sqlite3
    import telebot
    from registration_page.models import User
    import Shop
    from Shop.settings import DATABASE
    from shop_page.models import Product
    import flask
    from cart_page.models import Cart
    import threading

    db = sqlite3.connect(database = os.path.abspath(__file__ + "/../../Shop/data.db"))
    cursor = db.cursor()

    token = "7237016951:AAGrWiHW83Jti-EJKwquFgQTtIMaRIdG1eI"
    bot = telebot.TeleBot(token = token)

    button_get_users = telebot.types.InlineKeyboardButton(text = "GET USERS", callback_data = "get_users")
    button_get_cart = telebot.types.InlineKeyboardButton(text = "GET CART", callback_data = "get_cart")
    button_get_product = telebot.types.InlineKeyboardButton(text = "GET PRODUCT", callback_data = "get_product")
    button_add_product = telebot.types.InlineKeyboardButton(text = "ADD PRODUCT", callback_data = "add_product")
    keyboard_main = telebot.types.InlineKeyboardMarkup(keyboard = [[button_get_users], [button_get_cart], [button_get_product], [button_add_product]])

    products = {
                    'name': '',
                    'price': '',
                    'sale': '',
                    'previous_price': '',
                    'image': ''
                }
    user_action = {}
    product_db = {}

    @bot.message_handler(commands= ["start"])
    def start_message(message : telebot.types.Message):
        bot.send_message(message.chat.id, text = "Я працюююю!", reply_markup = keyboard_main)

    @bot.callback_query_handler(func = lambda call: True)
    def call_back(callback: telebot.types.CallbackQuery):
        with Shop.settings.shop_app.app_context():
            for user in User.query.all():
                # callback_data_remove_admin = f"remove_admin_{user.id}"
                button_remove_admin = telebot.types.InlineKeyboardButton(text = "REMOVE ADMIN ⛔", callback_data = f"remove_admin_{user.id}")
                button_add_admin = telebot.types.InlineKeyboardButton(text = "ADD ADMIN ✅", callback_data = f"add_admin_{user.id}")
                button_delete_user = telebot.types.InlineKeyboardButton(text = "DELETE USER 🗑️", callback_data = f"delete_user_{user.id}")
                keyboard_manage_user = telebot.types.InlineKeyboardMarkup(keyboard = [[button_remove_admin, button_add_admin], [button_delete_user]])
                # callback_data_remove_admin.split('_')[2]
                if callback.data == f"remove_admin_{user.id}":
                    user_id = int(callback.data.split('_')[2])
                    user_admin_delete = User.query.get(user_id)
                    user_admin_delete.is_admin = False
                    bot.edit_message_text(text = f"ID: {user.id}\nName: {user.name}\nPassword: {user.password}\n➡️is_admin: {user.is_admin}", chat_id = callback.message.chat.id, message_id = callback.message.message_id, reply_markup = keyboard_manage_user)

                    DATABASE.session.commit()
                    print(f"delete admin {user_id}")

                if callback.data == f"add_admin_{user.id}":
                    user_id = int(callback.data.split('_')[2])
                    user_admin_add = User.query.get(user_id)
                    user_admin_add.is_admin = True
                    bot.edit_message_text(text = f"ID: {user.id}\nName: {user.name}\nPassword: {user.password}\n➡️is_admin: {user.is_admin}", chat_id = callback.message.chat.id, message_id = callback.message.message_id, reply_markup = keyboard_manage_user)
                    DATABASE.session.commit()
                    print(f"add admin {user_id}")

                if callback.data == f"delete_user_{user.id}":
                    user_id = int(callback.data.split('_')[2])
                    user_delete = User.query.get(user_id)
                    DATABASE.session.delete(user_delete)
                    DATABASE.session.commit()
                    bot.delete_message(chat_id = -1002207494698, message_id = callback.message.id)
                    print(f"user delete {user_delete}")

                if callback.data == "get_users":
                    bot.send_message(chat_id = -1002207494698, message_thread_id = 4, text = f"ID: {user.id}\nName: {user.name}\nPassword: {user.password}\n➡️is_admin: {user.is_admin}", reply_markup = keyboard_manage_user)
            
            for product in Product.query.all():

                button_delete_product = telebot.types.InlineKeyboardButton(text = "DELETE PRODUCT 🗑️", callback_data = f"delete_product_{product.id}")
                keyboard_manage_product = telebot.types.InlineKeyboardMarkup(keyboard = [[button_delete_product]])

                if callback.data == "get_product":
                    bot.send_message(chat_id = -1002207494698, message_thread_id = 50, text = f"Product id: {product.id}\nName: {product.name}\nCount: {product.count}pcs\nPrice: {product.price}$\nSale: {product.sale}%\nPrevious price: {product.previous_price}$", reply_markup = keyboard_manage_product)
                
                if callback.data == f"delete_product_{product.id}":
                    product_id = int(callback.data.split('_')[2])
                    product_delete = Product.query.get(product_id)
                    DATABASE.session.delete(product_delete)
                    DATABASE.session.commit()
                    bot.delete_message(chat_id = -1002207494698, message_id = callback.message.id)
                    print(f"product delete {product_delete}")
                    
            
            if "add_product" in callback.data:
                bot.send_message(chat_id = -1002207494698, message_thread_id = 92, text = "Введіть назву товару:")
                user_action[-1002207494698] = 'name'
                print(1222222222222)
            
            for cart in Cart.query.all():
                button_order_done = telebot.types.InlineKeyboardButton(text = "Замовлення виконано ✅", callback_data = f"order_done_{cart.id}")
                keyboard_cart = telebot.types.InlineKeyboardMarkup(keyboard = [[button_order_done]])
                if callback.data == "get_cart":
                    bot.send_message(chat_id = -1002207494698, message_thread_id = 386, text = f"Замовлення№{cart.id}:\nНазва продукту - {product.name}\nЦіна - {product.price}грн\nКількість {product.count}шт  \n\nІм'я - {cart.name}\nПрізвище - {cart.surname}\nТелефон - {cart.number}\nЕмейл - {cart.email}\nМісто - {cart.city}\nВідділення Нової пошти - {cart.post_office}\nДодаткові Побажання - {cart.additional_wish}\n\nСтатус замовлення - {cart.status}", reply_markup = keyboard_cart)
                    
                if callback.data == f"order_done_{cart.id}":
                    order_id = int(callback.data.split('_')[2])
                    get_order = Cart.query.get(order_id)
                    get_order.status = True
                    bot.edit_message_text(text = f"Замовлення№{cart.id}:\nНазва продукту - {product.name}\nЦіна - {product.price}грн\nКількість {product.count}шт  \n\nІм'я - {cart.name}\nПрізвище - {cart.surname}\nТелефон - {cart.number}\nЕмейл - {cart.email}\nМісто - {cart.city}\nВідділення Нової пошти - {cart.post_office}\nДодаткові Побажання - {cart.additional_wish}\n\nСтатус замовлення - {cart.status}", chat_id = callback.message.chat.id, message_id = callback.message.message_id)
                    DATABASE.session.commit()
                
    @bot.message_handler(func = lambda message : message.chat.id in user_action, content_types = ["text", "photo"])
    def add_product(message):
        global products
        chat_id = -1002207494698
        text = message.text
        step = user_action[chat_id]
        if step == 'name':
            products["name"] = text
            bot.send_message(chat_id, message_thread_id = 92 , text = "Введіть ціну товару:")
            user_action[chat_id] = 'price'
        if step == 'price':
            products["price"] = text
            bot.send_message(chat_id, message_thread_id = 92, text = "Введіть знижку товару:")
            user_action[chat_id] = 'discount'
        if step == 'discount':
            products["sale"] = text
            bot.send_message(chat_id, message_thread_id = 92, text = "Введіть попередню ціну товару:")
            user_action[chat_id] = 'previous_price'
        if step == 'previous_price':
            products["previous_price"] = text
            bot.send_message(chat_id, message_thread_id = 92, text = "Надішліть зображення товару\n(в стислому форматі)")
            user_action[chat_id] = 'image'
        if step == 'image':
            file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            path = os.path.abspath(__file__ + f"/../../shop_page/static/image/{products['name']}.png")

            with open(path, 'wb') as new_file:
                new_file.write(downloaded_file)

            bot.reply_to(message, "Фото завантажено!") 
            bot.send_message(chat_id, message_thread_id = 92, text = f"Товар був успішно доданий!")
            user_action[chat_id] = None
        
            with Shop.settings.shop_app.app_context():
                product = Product(name = products["name"], price = products["price"], sale = products["sale"], previous_price = products["previous_price"])
                DATABASE.session.add(product)
                DATABASE.session.commit()
    threading.Thread(target = lambda: bot.polling(skip_pending = True)).start()
    # bot.polling()
except Exception as error:
    print(error)