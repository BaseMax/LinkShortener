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

app = flaskLocal(__name__)

#app.config.SERVER_NAME = 'asrez.base:80'
#app.config

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/single')
def single():
	return render_template('single.html')

@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about')
def about():
	return 'The about page'


# doc_count = col.count_documents(filter, skip=skip)
# results = col.find(filter).sort(sort).skip(skip).limit(limit)

linkRegistered= [
	"api",
	"login",
	"register",
	"exit",
	"signin",
	"signout",
]
