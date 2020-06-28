#!/usr/bin/env python3
'''
Created on 20200323
Update on 20200627
@author: Eduardo Pagotto
 '''

import os
import logging

from datetime import datetime
from bson.objectid import ObjectId

from tinydb import Query, where
from tinydb.operations import increment

#from ZeroDB.ZeroTransaction import ZeroTransaction, ZeroTinyDB

from AtomTinyDb.AtomTinyDbConn import AtomTinyDbConn
from AtomTinyDb.AtomTinyDbLock import AtomTinyDbLock

def main():

    if not os.path.exists('./data'):
        os.makedirs('./data')

    # criação
    aDB = AtomTinyDbConn('./data/db_teste1.json', sort_keys=True, indent=4, separators=(',', ': '))
    aDB.log.info('Iniciado')

    #table = aDB.table('tabela01')

    try:

        with AtomTinyDbLock(aDB.table('tabela01')) as db:

            # inserção dado
            val1 = db.insert({'id_data': str(ObjectId()),
                            'idade':10,
                            'status':0,
                            'nome':'Eduardo Pagotto',
                            'sexo':True,
                            'last':datetime.timestamp(datetime.now())})

            val2 = db.insert({'id_data': str(ObjectId()),
                        'status':0,
                        'idade':51,
                        'nome':'Eduardo Pagotto',
                        'sexo':True,
                        'last':datetime.timestamp(datetime.now())})

            val3 = db.insert({'id_data': str(ObjectId()),
                        'status':0,
                        'idade':55,
                        'nome':'Eduardo Pagotto',
                        'sexo':True,
                        'last':datetime.timestamp(datetime.now())})

            val4 = db.insert({'id_data': str(ObjectId()),
                        'status':0,
                        'nome':'Eduardo Pagotto',
                        'sexo':False,
                        'idade':30,
                        'last':datetime.timestamp(datetime.now())})

            # query com where
            result2 = db.search(where('sexo') == False)
            aDB.log.debug(str(result2))

            for item in result2:
                db.update(increment('status'), where('id_data')==item['id_data'])

            # query
            dados = Query()

            result = db.search((dados.idade > 50) & (dados.sexo == True))
            aDB.log.debug(str(result))

            ultimo = None
            for item in result:
                # update
                novo = {'last': datetime.timestamp(datetime.now()), 'status':3}
                db.update(novo, where('id_data')==item['id_data'])
                ultimo = item

            db.remove(dados.id_data == ultimo['id_data'])

            lista_existe = db.search(where('id_data') == ultimo['id_data'])

            # Mostra tudo
            result = db.all()
            aDB.log.debug(str(result))

    except Exception as exp:
        aDB.log.error('erro: %s', str(exp))

    aDB.log.info('fim')

if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    main()