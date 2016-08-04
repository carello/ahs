## ahs  (ACI tenant Healthscore - Spark)

### ahs1.py
The idea of this script is:  
1) Query the healthscore of a Tenant in ACI.  
2) Send periodic updates (tenant healthscore) to an existing spark room.  

The app can run in a docker container or native. I suppose a container is better running in the background. Dockerfile included; comment out the call the python version as needed.

Although I've coded the script to run only for 5 iterations for demonstrations purposes; the thought is it would run infinitely and send updates every 5 mins (or whatever interval you'd like).  

The app runs the [acitoolkit](https://github.com/datacenter/acitoolkit).  It's included in the container to make it portable.  
Acitoolkit API [documentation](https://acitoolkit.readthedocs.io/en/latest/modules.html)  


Documentation for [Spark APIs.](https://developer.ciscospark.com/getting-started.html) Provides a convenient demo mode as well.

The app is using a basic token for the Spark room. You'll need to add your own token, roomID and APIC credentials. 
You can find your Spark token by logging into <http://developer.cisocpark.com> and selecting "My Apps" in the upper right hand corner of the page. To find your roomID, select Documentation, then "Rooms" from the left hand column and navigate from there.  

 

###ahs2.py  
The idea of this version is:  
1) We monitor Tenant healthscores in APIC.  
2) If the healthscore is below a minimum threshold, (can be set in the program): the app will open up a Spark room, with an alert of the Tenant healthscore and add in team members.  
3) The alerts will continue to be sent until an upper watermark it hit. For example when healthscore reaches 95, stop sending the alerts. 


Note: for demo purposes the app is set to loop for 3 iterations. In production, you'd probably want an infinite loop until a condition is false.

#Setup
You'll need to provide Environmental Variables to run ahs1.py and ahs2.py. run ``source ahs_setup`` to provde the:	 Spark Token, Spark Room ID, APIC URL, APIC password, APIC user, and Tenant (only for ahs1.py).

 


