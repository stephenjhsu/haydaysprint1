import glob
import json
import sys


files = glob.glob('/home/testtest/srv/runme/'+sys.argv[1]+'*')
destination = '/home/testtest/srv/runme/' + str(sys.argv[1]) + '.txt'

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
with open(destination, 'w+') as f:
   for filenames in files:
      json_list = good_json(filenames)
      for blob in json_list:
         f.write(blob.get('name')+'\t'+blob.get('prop').get('age'))      
f.close()
