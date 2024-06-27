try:
    from .app import shop
    from . views import render_shop
except Exception as error:
    print(error)