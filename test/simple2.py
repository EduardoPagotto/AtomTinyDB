#!/usr/bin/env python3
'''
Created on 20200701
Update on 20200701
@author: Eduardo Pagotto
 '''

#pylint: disable=C0301, C0116, W0703, C0103, C0115

import os
import logging

from datetime import datetime
from bson.objectid import ObjectId

from tinydb import Query, where
from tinydb.operations import increment

from AtomTinyDb import AtomTinyDbConn#, AtomTinyDbLock

def main():

    if not os.path.exists('./data'):
        os.makedirs('./data')

    try:

        with AtomTinyDbConn('./data/db_teste2.json', sort_keys=True, indent=4, separators=(',', ': ')) as aDB:

            tbl = aDB.table('tbl01')

            # inserção dado
            val1 = tbl.insert({'id_data': str(ObjectId()),
                            'idade':10,
                            'status':0,
                            'nome':'Eduardo Pagotto',
                            'sexo':True,
                            'last':datetime.timestamp(datetime.now())})

            val2 = tbl.insert({'id_data': str(ObjectId()),
                        'status':0,
                        'idade':51,
                        'nome':'Eduardo Pagotto',
                        'sexo':True,
                        'last':datetime.timestamp(datetime.now())})

            val3 = tbl.insert({'id_data': str(ObjectId()),
                        'status':0,
                        'idade':55,
                        'nome':'Eduardo Pagotto',
                        'sexo':True,
                        'last':datetime.timestamp(datetime.now())})

            val4 = tbl.insert({'id_data': str(ObjectId()),
                        'status':0,
                        'nome':'Eduardo Pagotto',
                        'sexo':False,
                        'idade':30,
                        'last':datetime.timestamp(datetime.now())})

            # query com where
            result2 = tbl.search(where('sexo') == False)
            logging.debug(str(result2))

            for item in result2:
                tbl.update(increment('status'), where('id_data')==item['id_data'])

            # query
            dados = Query()

            result = tbl.search((dados.idade > 50) & (dados.sexo == True))
            logging.debug(str(result))

            ultimo = None
            for item in result:
                # update
                novo = {'last': datetime.timestamp(datetime.now()), 'status':3}
                tbl.update(novo, where('id_data')==item['id_data'])
                ultimo = item

            tbl.remove(dados.id_data == ultimo['id_data'])

            lista_existe = tbl.search(where('id_data') == ultimo['id_data'])

            # Mostra tudo
            result = tbl.all()

            logging.debug(str(result))

    except Exception as exp:
        logging.error('erro: %s', str(exp))

    logging.info('fim')

if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    main()