# haydaysprint1

Team Members: David Kes, Chris Dong, Cara Qin, Nicha Ruchirawat, Stephen Hsu

--------SPRINT 1----------------

In the Sprint 1 project, the goal is to write a Python script which can deploy our code to an AWS server. 

The current Github repo contains the script that we will call from deploy.py to 

  1. Clone the Github into an AWS instance
  2. Create a cron task to run myscript.py every 5 minutes
  3. Logout
  
--------UPDATE: SPRINT 2-------

In the Sprint 2 project, the goal is to build a web interface that will receive and process JSON objects. 

The modified files include: 
  app.py - Creates an application instance (an object of class Flask)  which handles all POST requests
  deploy_sprint2.py - Deploys the correct files into an EC2 instance
  my_script.py - Processes the JSON inputs and writes them to specific files
  
  Note: deploy.py is left on from Sprint 1 but is not used in Sprint 2
