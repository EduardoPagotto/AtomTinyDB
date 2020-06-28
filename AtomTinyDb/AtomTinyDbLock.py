#!/usr/bin/env python3
'''
Created on 20200627
Update on 20200627
@author: Eduardo Pagotto
 '''

#pylint: disable=C0301, C0116, W0703, C0103, C0115

import logging
import threading

from AtomTinyDb.ProxyCall import ProxyCall

class AbortSignal(Exception):
    pass

def abort():
    raise AbortSignal

class AtomTinyDbLock(object):

    serial = 0
    mutex_serial = threading.Lock()

    def __init__(self, table):

        with AtomTinyDbLock.mutex_serial:

            self.count = AtomTinyDbLock.serial
            AtomTinyDbLock.serial += 1

            self.mutex_access = table[0]
            self.table = table[1]
            self.log = logging.getLogger('AtomTinyDb')
            self.log.debug('Transaction %d', self.count)

    def __enter__(self):
        self.log.debug('acquire %d', self.count)
        self.mutex_access.acquire()
        self.log.debug('acquired %d', self.count)
        return self

    def __exit__(self, type, value, traceback):
        #if not traceback: # FIXME: ver como se comporta no crash
        self.mutex_access.release()
        self.log.debug('release %d', self.count)
        return isinstance(value, AbortSignal)

    def __getattr__(self, name):
        if name == '__iter__':
            return None

        return ProxyCall(name, self.table, self.count)