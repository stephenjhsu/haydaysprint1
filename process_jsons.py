import glob
import json
import sys

#initialize the files and the destination to put in the well-formatted jsons
files = glob.glob('/srv/runme/'+sys.argv[1]+'*')
destination = '/srv/runme/' + str(sys.argv[1]) + '.txt'

def good_json(filename):
   """
   good_json is a function that:
      1. takes in the path of a file
      2. uses multiple control flows to get only the proper json "blobs"
      3. returns the jsons that are properly formatted
   """
   with open(filename, 'r') as f:
       lines = f.read().strip().split('\n')
       jsons = []
       for line in lines:
            if str(line).count('age') == 1 and str(line).count('name') == 1:
                try:
                   j = json.loads(str(line))
                   try:
                       #try to make sure the name and age columns are properly formatted
                       if ((j.get('name') != None) 
                           and (j.get('name') != '')
                           and (j.get('prop').get('age') != None) 
                           and (j.get('prop').get('age') != '')) 
                           and (j.get('prop').get('age') >=0):
                           jsons.append(j)
                   except AttributeError:
                       print('error occured with the age and name field')
                       continue    
                except ValueError:
                   print('error occured with the format of the json blob')
                   continue
   return jsons

with open(destination, 'w+') as f:
   #for each file, read it in using the good_json function and write the good results onto the destination file
   for filenames in files:
      json_list = good_json(filenames)
      for blob in json_list:
         f.write(blob.get('name')+'\t'+str(blob.get('prop').get('age'))+'\n') 
