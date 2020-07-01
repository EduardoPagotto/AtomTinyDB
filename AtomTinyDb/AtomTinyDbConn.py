#!/usr/bin/env python3
'''
Created on 20200627
Update on 20200107
@author: Eduardo Pagotto
 '''

#pylint: disable=C0301, C0116, W0703, C0103, C0115

import logging
import threading
from tinydb import TinyDB

from AtomTinyDb.Abort import AbortSignal

class AtomTinyDbConn(object):
    def __init__(self, *args, **kargs):
        self.db = TinyDB(*args, **kargs)
        self.mutex_access = threading.Lock()
        self.log = logging.getLogger('AtomTinyDb')

    def table(self, *args, **kwargs):
        return self.mutex_access, self.db.table(*args, **kwargs)

    def tables(self):
        with self.mutex_access:
            return self.db.tables()

    def drop(self, table_name):
        with self.mutex_access:
            self.db.drop_table(table_name)

    def close(self):
         self.db.close()

    def __enter__(self):
        self.mutex_access.acquire()
        #self.log.debug('enter')
        return self.db

    def __exit__(self, type, value, traceback):
        self.mutex_access.release()
        #self.log.debug('exit')
        self.db.close()
        return isinstance(value, AbortSignal)