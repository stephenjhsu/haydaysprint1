import paramiko
import os

def deploy(path_to_ssh_key_private_key, server_address, prefix):
	pem = paramiko.RSAKey.from_private_key_file(path_to_ssh_key_private_key)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server_address, username="testtest", pkey=pem)

	#     ssh.exec_command('sudo yum install git -y')

	ssh.exec_command('cd; rm -rf haydaysprint1 || true')
	ssh.exec_command('git clone https://github.com/stephenjhsu/haydaysprint1.git')
	ssh.exec_command('mkdir -p /home/testtest/srv/runme/%s' % (prefix))
	ssh.exec_command('touch srv/runme/%s/proc.txt srv/runme/%s/Raw.txt' % (prefix, prefix))
	# ssh.exec_command('(crontab - l 2> dev/null; echo "*/1 * * * * python /home/testtest/haydaysprint1/app.py')
	ssh.exec_command('(crontab - l 2> dev/null; echo "*/1 * * * * python /home/testtest/haydaysprint1/app.py\n*/1 * * * * bash /home/testtest/haydaysprint1/copy.sh %s") | crontab -' % (prefix))
	
	ssh.close()


path_to_ssh_key_private_key = '/home/chris/cadong/1BigData/haydaysprint1/sprint_hayday.pem'
server_address = 'ec2-34-217-148-56.us-west-2.compute.amazonaws.com'
prefix = 'cccc'

deploy(path_to_ssh_key_private_key, server_address, prefix)