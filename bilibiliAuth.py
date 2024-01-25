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