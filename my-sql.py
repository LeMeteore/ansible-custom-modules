#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import json

space = []
cmd = "mysql -u user -ppassword database -e 'sql query;'"
mysql = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = mysql.communicate()[0]

for l in output.split("\n")[1:]:
    if len(l):
        print l
