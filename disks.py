#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import json
import ansible.runner

hostlist = ["vm1"]

def gigs(kibs):
    return float(kibs) / 1024.0 / 1024.0

runner = ansible.runner.Runner(
    module_path='.',
    module_name='my-df',
    module_args='',
    remote_user='patrick',
    host_list='hosts',
    private_key_file='/home/nsukami/.ssh/id_rsa_kratos',
    remote_port='1080',
    pattern=':'.join(hostlist),
    )

response = runner.run()
#print response

if 'dark' in response:
    if len(response['dark']) > 0:
        print "contact failure: "
        for host, reason in response['dark'].iteritems():
            print " {0} {1}".format(host, reason['msg'])


total = 0.0

for host, res in response['contacted'].iteritems():
    #print res
    for fs in res['space']:
        gb = gigs(fs['available'])
        total += gb
        print " %-30s %10.2f" % (fs['mountpoint'], gb)

print "total space over %d hosts: %.2f GB" % (len(response['contacted']), total)
