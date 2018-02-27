import paramiko
import os

def deploy(path_to_ssh_key_private_key, server_address, prefix):
	"""
	deploy is a function that takes in
		1. path to the pem file
		2. a server address of the EC2 instance
		3. a prefix to read and write json blobs into
	and uses those inputs to create a working instance to read in jsons on an EC2 instance
	"""
	# connecting to EC2 instance under username 'testtest'
	pem = paramiko.RSAKey.from_private_key_file(path_to_ssh_key_private_key)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server_address, username="testtest", pkey=pem)
	
	# clone files from github to EC2 instance
	ssh.exec_command('cd; rm -rf haydaysprint1 || true')
	ssh.exec_command('git clone https://github.com/stephenjhsu/haydaysprint1.git')
	
	# makes directory and files on EC2 instance based on deploy attributes
	ssh.exec_command('mkdir -p /home/testtest/srv/runme/%s' % (prefix))
	ssh.exec_command('touch srv/runme/%s/proc.txt srv/runme/%s/Raw.txt' % (prefix, prefix))
	
	# schedule the deploy script every two minutes
	ssh.exec_command('(crontab - l 2> dev/null; echo "*/2 * * * * python /home/testtest/haydaysprint1/make_app.py %s\n*/2 * * * * bash /home/testtest/haydaysprint1/copy.sh %s") | crontab -' % (prefix, prefix))
	
	ssh.close()

# path_to_ssh_key_private_key = '/home/chris/cadong/1BigData/haydaysprint1/sprint_hayday.pem'
# server_address = 'ec2-34-217-148-56.us-west-2.compute.amazonaws.com'
# prefix = 'zzz'

# deploy(path_to_ssh_key_private_key, server_address, prefix)
