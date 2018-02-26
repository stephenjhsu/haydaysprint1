import paramiko


def deploy(path_to_ssh_key_private_key, server_address, prefix):
    pem = paramiko.RSAKey.from_private_key_file(path_to_ssh_key_private_key)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_address, username="testtest", pkey=pem)

    #     ssh.exec_command('sudo yum install git -y')
    ssh.exec_command('cd; git clone https://github.com/stephenjhsu/haydaysprint1.git')

    # ssh.exec_command('contrab -e')
    ssh.exec_command('(crontab - l 2> dev/null; echo "*/5 * * * * python /home/testtest/haydaysprint1/process_jsons.py ' + prefix + '") | crontab -')

    ssh.close()


path_to_ssh_key_private_key = '/Users/davidkes/licenses/sprint_hayday.pem'
server_address = 'ec2-52-36-212-198.us-west-2.compute.amazonaws.com'
prefix = 'cookie'

deploy(path_to_ssh_key_private_key, server_address, prefix)
