from flask import Flask, jsonify, request
from flask_restful import Api
from resources.home import Home
from resources.list import List, Lists

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/home')
api.add_resource(Lists, '/lists')
api.add_resource(List, '/list/<list_id>')


if __name__ == "__main__":
    app.run(host="0.0.0.0")