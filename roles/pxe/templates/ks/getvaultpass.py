#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Hash import MD5
from Crypto.Cipher import AES
from base64 import b64decode
from requests import get
from socket import gethostname
from tempfile import mkstemp
import os

key = MD5.new(gethostname()).digest()
cipher = AES.new(key, AES.MODE_ECB)
base64enc = get("http://{{ serverfqdn }}:3000/vaultpass")
encrypted = b64decode(base64enc.content)
longpass = cipher.decrypt(encrypted)

fd, filename = mkstemp()
with open(filename, 'w+') as f:
  f.write(longpass.strip('x'))
os.close(fd)

print(filename)
