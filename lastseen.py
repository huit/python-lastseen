#!/usr/bin/python
# name:    lastseen.py
# version: .01
# author:  Tim Hartmann
# summary: Poll netmri for last seen data
# description "Poll NetMRI for Last Seen data and format it in such a way that it's useful to autoreg"

import urllib
import urllib2
import cookielib
import simplejson as json
import socket
import argparse
import os
import sys
import re
import requests
from netaddr import *

# Unset https_proxy env var
del os.environ['https_proxy']

parser = argparse.ArgumentParser(description='Update Last Seen Data from NetMRI API',
                    epilog='Example: lastseen.py --debug')
       
parser.add_argument('--debug', dest='DEBUG', action='store_true',
                    help='Echo debug output to stdout')

parser.add_argument('-H', '--host', dest='mri_url', action='store',
                    required='True', metavar='https://netmri.example.com',
                        help='Base URL for NetMRI')

parser.add_argument('-u', '--user', dest='mri_user', action='store',
                    required='True', metavar='username',
                        help='username that has API access')

parser.add_argument('-p', '--password', dest='mri_password', action='store',
                    required='True', metavar='Password1234',
                        help='username that has API access')
       
args = parser.parse_args()

