#!/usr/bin/env python

# rename this file to creds.py and enter in your date inputs.

import ssl
import requests
requests.packages.urllib3.disable_warnings()


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
    url = "http://url"
    login = "user name"
    password = "password"
    return url, login, password


def spark_GetArgs():
    token = "spark token"
    dt = "ACI Tenant name"
    roomId = "spark room id"
    return token, dt, roomId
