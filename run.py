from apps import app
from tools.middlewares import verify_token

app.before_request(verify_token)
@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='59003')
