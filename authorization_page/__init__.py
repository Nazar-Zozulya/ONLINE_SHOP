try:
    from .app import auth
    from .views import render_auth
except Exception as error:
    print(error)