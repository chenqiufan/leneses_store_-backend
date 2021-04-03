from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
# from flask_wtf import CSRFProtect
from flask_cors import CORS
from apps.config import REDIS_HOST,REDIS_POST
from flask_session import Session

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

# 初始化 redis 存储对象
redis_store = StrictRedis(host=REDIS_HOST,port=REDIS_POST)

# 开启CSRF保护
# CSRFProtect(app)

# 设置session 保存到redis
Session(app)

CORS(app)

from apps.db_api_v1 import models
from apps import views

