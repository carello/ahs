#!/usr/bin/env python

import ssl
import requests
import os
requests.packages.urllib3.disable_warnings()

# working area to set env for lab
tk_inp = os.getenv('TOKEN_INPUT')
dt_inp = os.getenv('DESIRED_TENANT_INPUT')
rm_inp = os.getenv('ROOM_ID_INPUT')
ur_inp = os.getenv('APIC_URL_INPUT')
lg_inp = os.getenv('APIC_LOGIN_INPUT')
ps_inp = os.getenv('APIC_PASSWRD_INPUT')


# TEST ENV's
#print tk_inp
#print dt_inp
#print rm_inp
#print ur_inp
#print lg_inp
#print ps_inp


def cred():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
     pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context


def apic_GetArgs():
    # enter in your credentials for your APIC
    url = ur_inp
    login = lg_inp
    password = ps_inp
    return url, login, password

def spark_GetArgs():
    token = tk_inp
    dt = dt_inp
    roomId = rm_inp
    return token, dt, roomId

