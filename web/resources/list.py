from datetime import datetime
from flask import Flask, json, jsonify, request
from flask_restful import Resource
import bson

from pymongo import MongoClient

client = MongoClient("mongodb://db:27017")
db = client.ListDB
lists = db["lists"]

def check_if_list_exists(id):

    if not bson.objectid.ObjectId.is_valid(id):
        return False

    list_to_check = lists.find({"_id": bson.objectid.ObjectId(id)})

    if list_to_check is None:
        return False

    return list_to_check

class List(Resource):
    def get(self, list_id):

        get_list = check_if_list_exists(list_id)

        if not get_list:
            return jsonify({
                "status" : 301,
                "message": "list not found"
            })

        data = []
        for list in get_list:
            data.append({"name" : list["name"], "date": list["date"], "id": str(list["_id"])})

        return jsonify(data)

    def put(self, list_id):

        put_list = check_if_list_exists(list_id)

        if not put_list:
            return jsonify({"message" : "list not found"})

class Lists(Resource):

    def get(self):
        data = []
        for list in lists.find():
            data.append({"name" : list["name"], "date": list["date"], "id": str(list["_id"])})

        return jsonify(data)

    def post(self):

        posted_data = request.get_json()
        list_name = posted_data["name"]
        if len(list_name) == 0:
            return_json = {
                "status": 301,
                "message": "List must have a name"
            }

            return jsonify(return_json)        

        new_list_id = lists.insert(
            {
                "name": list_name,
                "date": datetime.utcnow()
            })

        data = []
        for list in lists.find({"_id": new_list_id}):
            data.append({"name" : list["name"], "date": list["date"], "id": str(new_list_id)})

        return_json = {
            "status": 200,
            "message": "List " + list_name + " created!",
            "data" : data
        }

        return jsonify(return_json)