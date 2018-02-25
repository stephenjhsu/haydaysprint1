from flask import Flask, request

import requests
import glob
import json
import sys

application = Flask(__name__)

@application.route('/')
def index():
    return "Hello World"

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
if not os.path.exists('proc.txt'):
	open('proc.txt', 'w').close()

if not os.path.exists('Raw.txt'):
	open('Raw.txt', 'w').close()

@application.route('/foo', methods=['POST']) 
def foo():
	with open('Raw.txt', 'w') as f:
		f.write(request.data)

    	return "Succesfully received"

json_list = good_json('Raw.txt')
with open('proc.txt', 'w') as f2:
	# f2.write('hello')
	for blob in json_list:
		f2.write(blob.get('name')+'\t'+str(blob.get('prop').get('age'))+'\n') 
application.run(host='0.0.0.0',port=8080,debug=True)
