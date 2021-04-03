from flask import g

def login_requeried(func):
    def wrapper(*args,**kwargs):
        if g.user_id is not None and g.is_refresh == False:
            return func(*args,**kwargs)
        else:
            return {"message":"Inalid token"}
    return wrapper