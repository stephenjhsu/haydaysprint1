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
	
	ssh.exec_command('python haydaysprint1/app.py')

    # ssh.exec_command('contrab -e')
	# ssh.exec_command('(crontab - l 2> dev/null;echo "*/2 * * * * cp -a Raw.txt Raw.txt-$(date +%Y-%m-%d_%H_%M_%S)\n*/2 * * * * cp -a proc.txt proc.txt-$(date +%Y-%m-%d_%H_%M_%S)\n*/2 * * * * rm Raw.txt\n*/2 * * * * rm proc.txt" | crontab -')
    #ssh.exec_command('mkdir -p /home/testtest/srv/runme/%s' % prefix)
	ssh.close()


path_to_ssh_key_private_key = '/home/chris/cadong/1BigData/haydaysprint1/sprint_hayday.pem'
server_address = 'ec2-34-217-148-56.us-west-2.compute.amazonaws.com'
prefix = 'cookie'

deploy(path_to_ssh_key_private_key, server_address, prefix)