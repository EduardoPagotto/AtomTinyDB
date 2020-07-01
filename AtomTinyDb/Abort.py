#!/usr/bin/env python3
'''
Created on 20200701
Update on 20200701
@author: Eduardo Pagotto
 '''

#pylint: disable=C0301, C0116, W0703, C0103, C0115

class AbortSignal(Exception):
    pass

def abort():
    raise AbortSignal