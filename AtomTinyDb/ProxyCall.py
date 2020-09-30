'''
Created on 20200627
Update on 20200928
@author: Eduardo Pagotto
 '''

from typing  import Any

class ProxyCall(object):
    def __init__(self, function, table, count):
        self.function = function
        self.table = table
        #self.log = logging.getLogger('AtomTinyDb')
        self.count = count

    def __call__(self, *args, **kargs) -> Any:
        #self.log.debug('ProxyCall %d: func: %s, args: %s, kargs:%s', self.count, str(self.function), str(args), str(kargs))
        function = getattr(self.table, self.function)
        return function(*args, **kargs)
