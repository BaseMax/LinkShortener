from flask import Flask
from flask import Response
from flask import render_template
from flask import Blueprint
# from flask import request
from flask import request, jsonify
import uuid
import json
# from app import app, mongo
from pymongo import MongoClient
from bson import json_util
from flask import redirect

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'Asrez'
COLLECTION_LINK="Link"

class flaskLocal(Flask):
	def process_response(self, response):
		# response.headers
		return(response)
