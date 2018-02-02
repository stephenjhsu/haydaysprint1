import json
import sys
import glob

files = glob.glob('srv/runme/'+sys.argv[1]+'*.json')
destination = 'srv/runme/'+sys.argv[1]
def json_parser(filename):
    with open(filename, 'r') as f:
        j = json.load(f)
    return j.get('name')+'\t'+str(j.get('prop').get('age'))
for filenames in files:
    with open(destination, 'w') as f:
        f.write(json_parser(filenames))