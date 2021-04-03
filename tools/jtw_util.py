"""
1. jwt组成
    header,payload,signature
    a. header 头部
"""

from flask import current_app
import jwt
def generate_jwt(payload,expiry,secret=None):
    """

    :param payload: dict 载荷
    :param expiry: datetime 过期时间
    :param sercre: 密钥
    :return:
    """
    _payload = {'exp':expiry}
    _payload.update(payload)

    if not secret:
        secret = current_app.config['JWT_SECRET']

    token = jwt.decode(_payload,secret,algorithm='HS256')
    return token.decode()

def verify_jwt(token,secret=None):
    """
    
    :param token: 
    :param secret: 
    :return: 
    """
    if not secret:
        secret = current_app.config['JWT_SECRET']

    try:
        payload = jwt.decode(token,secret,algorithms=['HS256'])
    except jwt.PyJWTError:
        payload = None

    return payload