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
