#!/usr/bin/env python3
'''
Created on 20200324
Update on 20201025
@author: Eduardo Pagotto
 '''

import os
import time
import logging
import threading

from datetime import datetime
#from bson.objectid import ObjectId

from AtomTinyDb import AtomTinyDbConn, AtomTinyDbLock

class Thread_Test(object):
    def __init__(self, table_access, idVal, delay, espera):
        self.table_access = table_access
        self.id = idVal
        self.log = logging.getLogger('Test')
        self.delay = delay
        self.espara = espera

    def get_name(self):
        return 'th_{0}'.format(self.id)

    def __call__(self, *args, **kargs):

        self.log.debug('Begin: %d', self.id)

        #time.sleep(self.delay)

        try:
            with AtomTinyDbLock(self.table_access) as db:
                time.sleep(self.espara)

                self.log.debug('Executa insert %d', self.id)

                db.insert({'id_data': self.id,#str(ObjectId()),
                           'idade':10,
                           'status':0,
                           'nome':'Eduardo Pagotto',
                           'sexo':True,
                           'last':datetime.timestamp(datetime.now())})

        except Exception as exp:
            self.log.error('erro %d: %s', self.id, str(exp))

        #time.sleep(10)

        self.log.debug('End: %d', self.id)

def main():

    if not os.path.exists('./data'):
        os.makedirs('./data')

    aDb = AtomTinyDbConn('./data/db_threads.json')

    log = logging.getLogger('Test')

    log.info('Iniciado')

    lista_classes = []
    lista_threads = []

    for indice in range(5):
        lista_classes.append(Thread_Test(aDb.table('tabela01'), indice, 1, 5))

    for item in lista_classes:
        lista_threads.append(threading.Thread(target=item, name=item.get_name()))

    for item in lista_threads:
        item.start()

    while len(lista_threads) != 0:
        for item in lista_threads:
            item.join()
            lista_threads.remove(item)
            break
        time.sleep(1)

        log.info('Finalizado')

if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    main()
