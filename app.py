from flask import Flask, abort, request 
from flask import render_template # finds and renders files under */templates/
# from deploy_sprint2 import prefix
prefix = 'cccc'
# Initialization 
# Create an application instance (an object of class Flask)  which handles all requests.
application = Flask(__name__)

@application.route('/')
def index():
    return "Hello World"

import requests
import glob
import json
import sys

def good_json(filename):
	with open(filename, 'r') as f:
	   lines = f.read().strip().split('\n')
	   jsons = []
	   for line in lines:
		if str(line).count('age') == 1 and str(line).count('name') == 1:
		    try:
		       j = json.loads(str(line))
		       try:        
			   if ((j.get('name') != None) and (j.get('name') != '')
			       and (j.get('prop').get('age') != None) and (j.get('prop').get('age') != '')) and (j.get('prop').get('age') >=0):
			       jsons.append(j)
		       except AttributeError:
			   continue    
		    except ValueError:
		       continue
	return jsons

import os




# filename = '/srv/runme/' + prefix + '/Raw.txt' 
filename = "/home/testtest/testing.txt"
with open(filename, 'a+') as fa:
    fa.write('hi')




@application.route('/foo', methods=['POST']) 
def foo():
    	with open('/srv/runme/' + prefix + '/Raw.txt', 'w') as f:
		f.write(request.data)
		# f.write('hi')

		return "Succesfully received"

json_list = good_json('/srv/runme/' + prefix + '/Raw.txt')
with open('/srv/runme/' + prefix + '/proc.txt', 'w') as f2:
    for blob in json_list:
    	f2.write(blob.get('name')+'\t'+str(blob.get('prop').get('age'))+'\n') 




#Ensure that the development web server is started only when the script is executed directly.
application.run(host="localhost",port=8080,debug=True)
