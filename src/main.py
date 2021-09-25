from flask import Flask

from src.config import init
from src.controllers import routes

app = Flask(__name__)
app.config.from_object('settings')
app.register_blueprint(routes)

if __name__ == '__main__':
    init()
    app.run(host='0.0.0.0', port=3000)
