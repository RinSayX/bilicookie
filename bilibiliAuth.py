import asyncio
import base64
import hashlib
import json
import time
import urllib.parse
from copy import deepcopy
from typing import Optional


class biliAuth():
    def __init__(self):
        self.username = None

    def catch(self):
        self.catch = None

    def auth(self):
        self.username = None
        self.password = None


def getMyloginfo(username, password):
    for n in username:
        if n == None:
            return "Wrong Username"
        else:
            un = username
