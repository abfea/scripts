#!/bin/python
# -*- coding: utf-8 -*-
# 读取 vocabulary 中的单词并添加至欧陆辞典生词本

import json
import requests
import os

basedir = os.path.dirname(__file__) + '/'

with open(basedir + 'assets/token', 'r') as tk:
    token = tk.readline().strip()

url = 'https://api.frdic.com/api/open/v1/studylist/words'
header = { "content-type": "application/json", "Authorization": token }

data = {"id": "0", "language": "en", "words": []}

with open(basedir + 'assets/vocabulary', 'r') as v:
    for line in v.readlines():
        data['words'].append(line.strip())

r = requests.post(url, data=json.dumps(data), headers=header)
print(r.json().get('message'))
