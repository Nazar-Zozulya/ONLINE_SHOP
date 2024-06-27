try:
    from .app import home
    from .views import render_home
except Exception as error:
    print(error)