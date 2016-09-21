# -*- coding: utf-8 -*-
from flask import render_template , request ,g ,jsonify
from flask.ext.login import current_user
import os

from . import main

@main.before_request
def before_request():
    g.user = current_user

@main.app_errorhandler(404)
def page_not_found(e):
	s = request.url.split('/')
	dataPath = "data/"+s[len(s)-1]+".txt"
	if not os.path.exists(dataPath):
		return "NO Your Want File"
	else:
		with open(dataPath,'rt') as f:
			json = f.read().decode('utf-8', 'ignore')
			return json
		

@main.app_errorhandler(500)
def internal_server_error(e):
	return jsonify({"500":"500"})