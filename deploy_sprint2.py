import paramiko
import os

def deploy(path_to_ssh_key_private_key, server_address, prefix):
    pem = paramiko.RSAKey.from_private_key_file(path_to_ssh_key_private_key)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_address, username="testtest", pkey=pem)

    #     ssh.exec_command('sudo yum install git -y')
    ssh.exec_command('cd; git clone https://github.com/stephenjhsu/haydaysprint1.git')
    
    # ssh.exec_command('contrab -e')
    ssh.exec_command('(crontab - l 2> dev/null; echo "*/2 * * * * python /home/testtest/haydaysprint1/app.py | cp -a /home/testtest/srv/runme/%s/Raw.txt "/home/testtest/srv/runme/%s/Raw.txt-$(date +"%Y-%m-%dT%H%M%S%:z")" | crontab -' % (prefix, prefix))
    ssh.exec_command('mkdir -p /home/testtest/srv/runme/%s' % prefix)
    ssh.close()


path_to_ssh_key_private_key = '/home/chris/cadong/1BigData/haydaysprint1/sprint_hayday.pem'
server_address = 'ec2-52-39-4-245.us-west-2.compute.amazonaws.com'
prefix = 'cookie'

deploy(path_to_ssh_key_private_key, server_address, prefix)