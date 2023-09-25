#!/usr/bin/env python


from lib.core.compat import xrange
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    retVal = payload

    if payload:
        retVal = ""

        for i in xrange(len(payload)):
            if payload[i] == '"':
                retVal += ' '
                continue

            retVal += payload[i]

    return retVal
