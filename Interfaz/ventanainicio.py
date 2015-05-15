from tkinter import * 
from ventanainiciosesion import *
from ventanainvitado import *
from ventanaregistrousu import *



v0 = Tk() # Tk() Es la ventana principal
v0.config(bg="white") # Le da color al fondo
v0.geometry("500x590") # Cambia el tamaño de la ventana
imagen0=PhotoImage(file="logocofradia.gif")
Label(v0,image=imagen0).pack()
b0=Button(v0,text="INICIAR SESION",command=lambda: inicioSesion(v0)).pack()   #  grid(row=17,column=2)
b01=Button(v0,text="REGISTRARSE",command=lambda: crearUsuario(v0)).pack() #grid(row=17,column=4)
b02=Button(v0,text="INVITADO",command=lambda: inicioInvitado(v0)).pack()  # grid(row=17,column=3)


v0.mainloop() # Es el evento que llama al inicio de nuestro programa. Siempre lo lleva la ventana principal.