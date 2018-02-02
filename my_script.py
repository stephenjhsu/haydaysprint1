import glob
import json
files = glob.glob('srv/runme/c*')

destination = 'srv/runme/something3.txt'

def json_parser(filename):
   with open(filename, 'r') as f:
   
	j = json.load(f)
	print j
	print('got to end')
	return j.get('name')+' '+str(j.get('prop').get('age'))

print files
with open(destination, 'w+') as f:
   for filenames in files:
		print 'hi'
		print filenames
		f.write(json_parser(filenames))
		# f.write('hi')
