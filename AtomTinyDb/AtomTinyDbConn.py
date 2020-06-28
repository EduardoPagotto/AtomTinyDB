#!/usr/bin/env python3
'''
Created on 20200627
Update on 20200628
@author: Eduardo Pagotto
 '''

import logging
import threading
from tinydb import TinyDB

class AtomTinyDbConn(object):
    def __init__(self, *args, **kargs):
        self.db = TinyDB(*args, **kargs)
        self.mutex_access = threading.Lock()
        self.log = logging.getLogger('AtomTinyDb')

    def table(self, *args, **kwargs):
        return self.mutex_access, self.db.table(*args, **kwargs)