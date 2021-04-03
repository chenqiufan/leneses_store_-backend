from tools.jtw_util import generate_jwt
from datetime import datetime,timedelta

def generate_token(user_id,refresh=True):
    expiry = datetime.utcnow() + timedelta(hours=2)
    token = generate_jwt({"user_id":user_id},expiry=expiry)


    if refresh:
        expiry = datetime.utcnow() + timedelta(days=14)
        refresh_token = generate_jwt({'user_id':user_id,'is_refresh':True},expiry=expiry)
    else:
        refresh_token = None

    return token,refresh_token

