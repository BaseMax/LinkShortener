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

@app.route('/link/', methods=['GET','POST'], defaults={'identifier':None})
@app.route('/link/<string:identifier>/',methods=['GET'])
def link(identifier):
	mainSite="http://asrez.base/"
	site="http://asrez.base/link/"
	if identifier == None or identifier == '':
		if request.method == "GET":
			return render_template('link_index.html', error=False, method=request.method, random=uuid.uuid4().hex.upper()[0:7].lower(), site=site, mainSite=mainSite)
		else:
			url=request.form.get("url")
			identifier=request.form.get("identifier")
			if url and identifier:
				allow=True
				for item in linkRegistered:
					if identifier in item:
						allow=False
						break
				if allow:
					exists=collectionLink.count_documents({"identifier":identifier})
					if exists == False:
						mydict = {"url":url,"identifier":identifier}
						x = collectionLink.insert_one(mydict)
						if x.inserted_id:
							message="Success"
							status=True
							return render_template('link_index.html', error=False, message=message, method=request.method, identifier=identifier, status=status, site=site, mainSite=mainSite)
						else:
							status=False
							message="Problem occur in generate link!"
							return render_template('link_index.html', error=False, message=message, method=request.method, identifier=identifier, status=status, site=site, mainSite=mainSite)
					else:
						status=False
						message="Aleady Exists!"
						return render_template('link_index.html', error=False, message=message, method=request.method, identifier=identifier, status=status, site=site, mainSite=mainSite)
				else:
					status=False
					message="Identifier is not Allow!"
					return render_template('link_index.html', error=False, message=message, method=request.method, identifier=identifier, status=status, site=site, mainSite=mainSite)
			else :
				status=False
				message="Failed alert!"
				return render_template('link_index.html', error=False, message=message, method=request.method, identifier=identifier, status=status, site=site, mainSite=mainSite)
	elif identifier in linkRegistered:
		if identifier == "api":
			return render_template('link_api.html', site=site, mainSite=mainSite)
		else:
			return "Soon..."
	else:
		get=collectionLink.find_one({"identifier":identifier})
		if get != None:
			# return get["url"]
			return redirect(get["url"], code=302)
		else:
			message="Wrong link!"
			return render_template('link_index.html', error=True, message=message, identifier=identifier, site=site, mainSite=mainSite)
