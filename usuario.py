#!/usr/bin/python
#-*- coding: utf-8 -*-
from Users import Users
class usuario(Users):
    def __init__(self,idP,nombreUsuario,idUsuario,nombre,correo):
        Users.__init__(self,idP,nombreUsuario)
        self.idUsuario = idUsuario
        self.nombre = nombreUsuario
        self.correo = correo

    def getCorreo(self ):
        return self.correo

    def crearCuenta(self, ):
        print("¿Desea crear una cuenta?")

    def accederCuenta(self):
        print("Puede acceder a su cuenta")

    def getNombre(self ):
        return self.nombre

    def __toString__(self):
        return Users.__toString__(self)+"idUsuario:{} Nombreusuario: {} Correo: {}".format(self.idUsuario,self.nombreUsuario,self.correo)
