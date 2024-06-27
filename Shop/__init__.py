try:
    from .urls import *
    from .settings import shop_app
    from .login_maneger import *
except Exception as error:
    print(error)