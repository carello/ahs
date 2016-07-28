# ahs  
####(ACI tenant Healthscore - Spark)

The idea of this script is:  
1) Query the healthscore of a Tenant in ACI.  
2) Send periodic updates (tenant healthscore) to an existing spark room.  

The app can run in a docker container or native. I suppose a container is better running in the background. Dockerfile included.  

Although I've coded the script to run only for 5 iterations for demonstrations purposes; the thought is it would run infinitely and send updates every 5 mins (or whatever interval you'd like).  

The app runs the acitoolkit: <https://github.com/datacenter/acitoolkit> .  It's included in the container to make it portable.  
Acitoolkit API documentation is here: <https://acitoolkit.readthedocs.io/en/latest/modules.html>  


Documentation for Spark APIs can be found here.    
<https://developer.ciscospark.com/getting-started.html>  
Provides a convenient demo mode as well.

The app is using a basic token for the Spark room. You'll need to add your own token, roomID and APIC credentials. Copy the ****creds-template.py**** to ****creds.py****  and update your data/credentials. 

***ToDo - add more robust authentication***  

 


