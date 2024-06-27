try:
    from .app import admin
    from .views import render_admin
except Exception as error:
    print(error)