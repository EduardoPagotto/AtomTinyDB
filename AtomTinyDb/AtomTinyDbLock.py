#!/usr/bin/env python3
'''
Created on 20200627
Update on 20200710
@author: Eduardo Pagotto
 '''

#pylint: disable=C0301, C0116, W0703, C0103, C0115

import logging
from threading import Lock

from typing import Union, Tuple

from tinydb.table import Table

from AtomTinyDb.Abort import AbortSignal
from AtomTinyDb.ProxyCall import ProxyCall

class AtomTinyDbLock(object):
    """[Trava e acesso a tabela]
    Args:
        object ([type]): [description]
    Returns:
        [type]: [description]
    """

    serial: int = 0
    mutex_serial: Lock = Lock()

    def __init__(self, table: Tuple[Lock, Table]):
        """[Acesso ad db de forma atomica]
        Args:
            table (Tuple[Lock, Table]): [description]
        """
        with AtomTinyDbLock.mutex_serial:

            self.count: int = AtomTinyDbLock.serial
            AtomTinyDbLock.serial += 1

            self.mutex_access: Lock = table[0]
            self.table = table[1]
            self.log = logging.getLogger('AtomTinyDb')
            #self.log.debug('Transaction %d', self.count)

    def __enter__(self):
        #self.log.debug('acquire %d', self.count)
        self.mutex_access.acquire()
        #self.log.debug('acquired %d', self.count)
        return self

    def __exit__(self, type, value, traceback) -> bool:
        #if not traceback: # FIXME: ver como se comporta no crash
        self.mutex_access.release()
        #self.log.debug('release %d', self.count)
        return isinstance(value, AbortSignal)

    def __getattr__(self, name: str) -> Union[None, ProxyCall]:
        if name == '__iter__':
            return None

        return ProxyCall(name, self.table, self.count)
