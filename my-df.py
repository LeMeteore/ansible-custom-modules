#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import json

space = []

df = subprocess.Popen(["df", "-P", "-k"], stdout=subprocess.PIPE)
output = df.communicate()[0]

for l in output.split("\n")[1:]:
    if len(l):
        try:
            device, size, used, available, percent, mountpoint = l.split()
            space.append({'mountpoint': mountpoint, 'available': available})
        except:
            pass
print json.dumps(dict(space=space), indent=4)
