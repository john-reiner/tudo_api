from flask import Flask, jsonify
from flask_restful import Resource

class Home(Resource):
    def get(self):
        
        return_json = {
            "status": 200,
            "message": "Hello World"
        }

        message = return_json['message']

        return jsonify(return_json)