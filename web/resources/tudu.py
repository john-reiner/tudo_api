from datetime import datetime
from flask import Flask, json, jsonify, request
from flask_restful import Resource
import bson

from pymongo import MongoClient

client = MongoClient("mongodb://db:27017")
db = client.ListDB
lists = db["lists"]


