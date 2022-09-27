#!/usr/bin/python
#-*- coding: utf-8 -*-

class Users(object):
    def __init__(self,idP,nombreUsuario):
        self.idP = idP
        self.nombreUsuario = nombreUsuario
        

    def __toString__(self):
        return "idP:{} Nombre usuario: {} ".format(self.idP,self.nombreUsuario)

