
from django.shortcuts import redirect
import time

# Convert the middleware to a decorator
def auth_middleware(view_func):
    
    def wrapper(request, *args, **kwargs):
        # Custom authentication logic
        if (request.path == '/home/' or request.path == '/profile/' or request.path == '/cust_home/') and request.session.get('id') is None:
            return redirect('/accounts/login/')

        if (request.path == '/accounts/login/' or request.path == '/accounts/register/') and request.session.get('id') is not None:
            return redirect('/profile/')

        # Store last login time if it doesn't exist
        # if request.session.get('id') is not None and request.session.get('last_login_time') is None:
        #     request.session['last_login_time'] = time.strftime('%Y-%m-%d %H:%M:%S')

        # Call the view function
        response = view_func(request, *args, **kwargs)

        # Optionally, pass the login time in the response header
        # if request.session.get('id'):
        #     response['X-Last-Login-Time'] = request.session.get('last_login_time')

        return response

    return wrapper


