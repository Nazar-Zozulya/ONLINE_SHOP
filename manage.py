try:
    import Shop
    import bot_app.main

    if __name__ == '__main__':
        Shop.shop_app.run(debug = True)
        # bot_app.main.run(debug = True)

except Exception as error:
    print(error)
    