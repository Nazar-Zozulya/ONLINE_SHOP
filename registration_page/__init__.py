try:   
    from .app import reg
    from .views import render_reg
    from .models import User
except Exception as error:
    print(error)