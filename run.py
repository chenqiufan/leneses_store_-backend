from apps import app
from tools.middlewares import verify_token

app.before_request(verify_token)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='59003')
