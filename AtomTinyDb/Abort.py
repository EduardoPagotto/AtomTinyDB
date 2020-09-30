'''
Created on 20200701
Update on 20200928
@author: Eduardo Pagotto
 '''

class AbortSignal(Exception):
    pass

def abort() -> AbortSignal:
    raise AbortSignal
