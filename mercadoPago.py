#!/usr/bin/python
#-*- coding: utf-8 -*-
from Users import Users
class mercadoPago(Users):
    def __init__(self,idP,nombreUsuario,idMerP,nombreAdmin,correoAdmin):
        Users.__init__(self,idP,nombreUsuario)
        self.idMerP = idMerP
        self.nombreAdmin = nombreAdmin
        self.correoAdmin = correoAdmin

    def verificarUsuario(self):
        print("Revisa si existe el usuario")

    def getTipoAdmin(self ):
        return self.nombreAdmin

    def getCorreo(self, ):
        return self.correo

    def getNombre(self, ):
        return nombreAdmin

    def __toString__(self):
        return Users.__toString__(self)+"idMercP:{} Nombre admin: {}  correoAdmin".format(self.idMerP,self.nombreAdmin,self.correoAdmin)
