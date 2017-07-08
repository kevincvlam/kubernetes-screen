#!/usr/bin/env python
"""Determines to run a producer or consumer script based on environment
   variable.
"""
import os

NODETYPE = os.environ['NODETYPE']

if NODETYPE == 'producer':
    os.system("python producer.py")
elif NODETYPE == 'consumer':
    os.system("python consumer.py")
else:
    print "unknown type %s" % NODETYPE
