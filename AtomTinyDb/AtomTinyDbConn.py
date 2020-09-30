'''
Created on 20200627
Update on 20200928
@author: Eduardo Pagotto
 '''

from threading import Lock
from typing import Set, Tuple

from tinydb import TinyDB
from tinydb.table import Table

from AtomTinyDb.Abort import AbortSignal

class AtomTinyDbConn(object):
    """[Classe de DB e Travas de acesso]
    Args:
        object ([type]): [description]
    """
    def __init__(self, *args, **kargs):
        """[Paramentros dp TinyDB]
        """
        self.db = TinyDB(*args, **kargs)
        self.mutex_access = Lock()
        #self.log = logging.getLogger('AtomTinyDb')

    def table(self, *args, **kwargs) -> Tuple[Lock, Table]:
        """[Retorna Lock e objeto Tabela]
        Returns:
            Tuple[Lock, Table]: [description]
        """
        return self.mutex_access, self.db.table(*args, **kwargs)

    def tables(self) -> Set[str]:
        """[Retorna Lista de nomes de Tabelas]
        Returns:
            Set[str]: [Nome das tabelas existentes]
        """
        with self.mutex_access:
            return self.db.tables()

    def drop(self, table_name: str):
        """[Drop da tabela]
        Args:
            table_name (str): [Nome da tabela a dropar]
        """
        with self.mutex_access:
            self.db.drop_table(table_name)

    def close(self):
        """[Close do DB]
        """
        self.db.close()

    def __enter__(self) -> TinyDB:
        """[Entry do DB]
        Returns:
            TinyDB: [Retorna o proprio Banco]
        """
        self.mutex_access.acquire()
        #self.log.debug('enter')
        return self.db

    def __exit__(self, type_val, value, traceback) -> bool:
        """[summary]
        Args:
            type_val ([type]): [description]
            value ([type]): [description]
            traceback ([type]): [description]

        Returns:
            bool: [description]
        """
        self.mutex_access.release()
        #self.log.debug('exit')
        self.db.close()
        return isinstance(value, AbortSignal)
