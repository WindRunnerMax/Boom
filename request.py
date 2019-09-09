#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import random
import socket
import struct
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh-TW;q=0.8,zh;q=0.6,en;q=0.4,ja;q=0.2",
    "cache-control": "max-age=0",
    "X-Requested-With": "XMLHttpRequest"
}

IP = socket.inet_ntoa(struct.pack(">I", random.randint(1, 0xffffffff)))
headers["X-FORWARDED-FOR"] = IP
headers["CLIENT-IP"] = IP
headers["X-REAL-IP"] = IP
headers["X-CLIENT-TIME"] = str(int(time.time() * 1000))
session = requests.Session()

res = session.get("https://www.baidu.com", headers=headers, timeout=5)
res.encoding = "utf-8"
print(res.text[:100])
