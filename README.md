# ahs  (ACI tenant Healthscore - Spark)

### ahs1.py
The idea of this script is:  
1) Query the healthscore of a Tenant in ACI.  
2) Send periodic updates (tenant healthscore) to an existing spark room.  

The app can run in a docker container or native. I suppose a container is better running in the background. Dockerfile included; comment out the call the python version as needed.

Although I've coded the script to run only for 5 iterations for demonstrations purposes; the thought is it would run infinitely and send updates every 5 mins (or whatever interval you'd like).  

The app runs the [acitoolkit](https://github.com/datacenter/acitoolkit).  It's included in the container to make it portable.  
Acitoolkit API [documentation](https://acitoolkit.readthedocs.io/en/latest/modules.html)  


Documentation for [Spark APIs.](https://developer.ciscospark.com/getting-started.html) Provides a convenient demo mode as well.
 

###ahs2.py  
The idea of this version is:  
1) We monitor Tenant healthscores in APIC.  
2) If the healthscore is below a minimum threshold, (can be set in the program): the app will open up a Spark room, with an alert of the Tenant healthscore and add in team members.  
3) The alerts will continue to be sent until an upper watermark it hit. For example when healthscore reaches 95, stop sending the alerts. 


Note: for demo purposes the app is set to loop for 3 iterations. In production, you'd probably want an infinite loop until a condition is false.

##Setup
The app is using a basic token for the Spark room. You'll need to add your own token, roomID and APIC credentials.  You can find your Spark token by logging into <http://developer.cisocpark.com> and selecting "My Apps" in the upper right hand corner of the page. To find your roomID: select Documentation, then "Rooms" from the left hand column and navigate from there. 

Once you have that you'll need to provide Environmental Variables to run ahs1.py and ahs2.py. Run ``source ahs_setup`` to provide the following: Spark Token, Spark Room ID, APIC URL, APIC password, APIC user, and Tenant (only for ahs1.py).  

###Docker Setup  

If building a docker container, you'll need to provide an environmental file at container run time: ``--env-file file_name``. I've provided and example file for reference.

#Vagrant  
Included are Vagrant configuration files. It uses a host VM (Ubuntu) to run docker. To setup: Run``vagrant up``in your main directory to start.  

You'll notice there's a directory called 'host'. if you``cd host``you'll be able to execute``vagrant ssh``to get access to the host. You can certainly configure the Ubuntu host for ssh directly. Take a look at the Vagrantfiles for the IP address. You can change the IP for your environment.

There are lot of environmental variables to this app. You'll find it easier to get started if you copy your ***docker env-file*** into the host directory. See "Docker Setup" above for details. This is convienent because it's a shared directory on the Ubuntu host.  

To run the container:

	1) ssh into your Ubuntu host.
	2) copy the file 'my_env' from the /vagrant directory into /home/vagrant
	3) enter 'docker images' to get the Docker "IMAGE ID"
	4) enter the docker run command to spin up the container.  
		For example: docker run -it --env-file <my_env> --name=<some_name> <IMAGE ID>









 


