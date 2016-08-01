#!/usr/bin python

import creds
import acitoolkit.acitoolkit as aci
import requests
import json
import sys
import time

# starting phase 1

spark_host = "https://api.ciscospark.com"
spark_api = "https://api.ciscospark.com/v1/messages"
token, dt, roomId = creds.spark_GetArgs()
email = "cp2carello@gmail.com"

spark_headers = {'Content-type': 'application/json', 'Authorization': token}

# Spark rooms setup
def setup_room():
    print "in setup room function"
    room_items = current_rooms()
    #print rooms

# Look for a room called "Alert Room"
    alert_room_id = ""
    for room in room_items:
        if room["title"] == "Alert Room":
            print("Found Room")
            alert_room_id = room["id"]
            return alert_room_id

# If alert room not found, create it
    if alert_room_id == "":
        alert_room = create_alert_room()
        alert_room_id = alert_room["id"]
        # pprint(demo_room)
    return alert_room_id


def create_alert_room():
    spark_r = spark_host + "/v1/rooms"
    spark_body = {"title":"Alert Room"}
    page = requests.post(spark_r, headers = spark_headers, json=spark_body)
    print "IN CREATE ALERT ROOM"
    print page
    room = page.json()
    return room

def current_rooms():
    spark_r = spark_host + "/v1/rooms"
    page = requests.get(spark_r, headers=spark_headers)
    rooms = page.json()
    #print rooms["items"][0]['title']
    return rooms["items"]


# Utility Add a user to the Alert Room
def add_email_alert_room(email, alert_room_id):
    member = get_membership_for_room(alert_room_id)
    personEmail_id = ""
    print "MEMBER"
    print alert_room_id
    print "X" * 20
    for k,v in member[0].items():
        if k == 'personEmail':
            personEmail_id = v
    print personEmail_id

    if personEmail_id != email:
        print "in add email alert room"
        spark_r = spark_host + "/v1/memberships"
        spark_body = {"personEmail": email, "roomId" : alert_room_id}
        page = requests.post(spark_r, headers = spark_headers, json=spark_body)
        membership = page.json()
        return membership
    else : return



def get_membership_for_room(alert_room_id):
    spark_r = spark_host + "/v1/memberships?roomId=%s" % (alert_room_id)
    page = requests.get(spark_r, headers = spark_headers)
    memberships = page.json()["items"]
    print "IN GET MEMBER FOR ROOM"
    #print memberships
    return memberships



def send_alert(alert_room_id, message):
    headers = {'Content-type': 'application/json', 'Authorization': token}
    data = {'roomId': alert_room_id, 'text': message}
    requests.post(spark_api, headers=headers, data=json.dumps(data))



def main():
    url, login, password = creds.apic_GetArgs()
    session = aci.Session(url, login, password)
    resp = session.login()

    if not resp.ok:
        print('%% Could not login to APIC')
        sys.exit(0)

    seltenant = ""
    lowtenant = ""
    tenants = aci.Tenant.get(session)
    timeo = 0
    message = ""

# orginal block of ahs1.py
#    while timeo < 3:
#        for t in tenants:
#            if t.name == dt:
#                seltenant = t.name
#                timeo += 1
#               print seltenant
#
#            if seltenant == t.name:
#                u = session.get("/api/node/mo/uni/tn-"+ dt +"/health.json")
#                page = json.loads(u.content)
#                healthscore =  page["imdata"][0]["healthInst"]['attributes']['twScore']
#                message = "TENANT %s's  Score: %s" % (seltenant, healthscore)
#                headers = {'Content-type': 'application/json', 'Authorization': token}
#                data = {'roomId': roomId, 'text': message}
#                requests.post(spark_api, headers=headers, data=json.dumps(data))
#                time.sleep(5)
#        if seltenant != dt:
#            print "OUCH"
#            sys.exit(0)


    for tt in tenants:
        if tt.name == "Ben-Ten1":
            lowtenant = tt.name
            print lowtenant

        if lowtenant == tt.name:
            u = session.get("/api/node/mo/uni/tn-"+ lowtenant +"/health.json")
            page = json.loads(u.content)
            healthscore =  page["imdata"][0]["healthInst"]['attributes']['twScore']
            message = "TENANT %s's  Score: %s" % (lowtenant, healthscore)
            print message
            #headers = {'Content-type': 'application/json', 'Authorization': token}
            #data = {'roomId': roomId, 'text': message}
            #requests.post(spark_api, headers=headers, data=json.dumps(data))
        if lowtenant != lowtenant:
            print "OUCH -  Tenatns don't match"
            sys.exit(0)



    alert_room_id = setup_room()
    add_email_alert_room(email, alert_room_id)
    send_alert(alert_room_id, message)

main()
