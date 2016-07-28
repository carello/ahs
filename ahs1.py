#!/usr/bin python

import creds
import acitoolkit.acitoolkit as aci
import requests
import json
import sys

spark_api = "https://api.ciscospark.com/v1/messages"

def main():
    url, login, password = creds.apic_GetArgs()
    token, dt, roomId = creds.spark_GetArgs()

    session = aci.Session(url, login, password)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')
        sys.exit(0)

    seltenant = ""
    tenants = aci.Tenant.get(session)
    for t in tenants:
        if t.name == dt:
            seltenant = t.name
            print seltenant

        if seltenant == t.name:
            u = session.get("/api/node/mo/uni/tn-"+ dt +"/health.json")
            page = json.loads(u.content)
            healthscore =  page["imdata"][0]["healthInst"]['attributes']['twScore']
            message = "TENANT %s's  Score: %s" % (seltenant, healthscore)
            headers = {'Content-type': 'application/json', 'Authorization': token}
            data = {'roomId': roomId, 'text': message}
            requests.post(spark_api, headers=headers, data=json.dumps(data))
    if seltenant != dt:
        print "OUCH"
        sys.exit(0)



main()
