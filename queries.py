#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import json
import ansible.runner

hostlist = ["vm1"]

runner = ansible.runner.Runner(
    module_path='.',
    module_name='my-sql',
    module_args='',
    remote_user='patrick',
    host_list='hosts',
    private_key_file='/home/nsukami/.ssh/id_rsa_kratos',
    remote_port='1080',
    pattern=':'.join(hostlist),
    )

response = runner.run()

if 'dark' in response:
    if len(response['dark']) > 0:
        print "contact failure: "
        for host, reason in response['dark'].iteritems():
            print " {0} {1}".format(host, reason['msg'])


total = 0.0

for host, res in response['contacted'].iteritems():
    print res['msg'].split('\r\n')[0]
