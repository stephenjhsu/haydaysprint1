import glob
import json
import sys


files = glob.glob('/home/testtest/srv/runme/'+sys.argv[1]+'*')
destination = '/home/testtest/srv/runme/something3.txt'

def json_parser(filename):
   with open(filename, 'r') as f:

        j = json.load(f)
        print j
        print('got to end')
        return j.get('name')+' '+str(j.get('prop').get('age'))

with open(destination, 'w+') as f:
   for filenames in files:
        f.write(json_parser(filenames))
