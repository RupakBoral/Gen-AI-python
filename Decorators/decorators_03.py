from functools import wraps

def authorization(check_auth):
    @wraps(check_auth)
    def wrapper(role):
        if(role == 'admin'):
            check_auth(role)
            return None
        else:
            print("Permission denied")
            return None
        
    return wrapper


@authorization
def check_permission(role='user'):
    print("Access granted!")

def user_role():
    role = str(input("Enter your role: "))
    check_permission(role)

user_role()