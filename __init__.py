import mercadoPago
import Users
import usuario

#self,idP,nombreUsuario,idUsuario,nombre,correo)
usuario1= usuario.usuario(1,"ing","1D","monro","monse@gmail.com")


print("====== MERCADO PAGO=========")
#print("Bienvenid@ usuario: ", usuario1.getNombre())

nom=input("Ingrese Nombre: ")
email= input("Ingrese correo: ")

usuario2 =usuario.usuario(1,nom,"1D",nom,email)
print("Bienvenid@ usuario: ", usuario2.getNombre())