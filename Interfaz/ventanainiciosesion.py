from tkinter import *
from ventanacategorias import *

def volverinicio(vd,vo):
	vd.destroy()
	vo.deiconify()

def inicioSesion(v):
	v1=Toplevel(v) # Crea una ventana hija
	v.withdraw()
	v1.title('Inicio Sesion')
	
	usuario=Label(v1,text="Usuario : ")
	usuario.grid(row=2,column=2)
	usuario_nombre = StringVar()
	caja_usuario = Entry(v1,textvariable=usuario_nombre)
	caja_usuario.grid(row=2,column=3)

	clave=Label(v1,text="Contraseña : ")
	clave.grid(row=4,column=2)
	clave_nombre = StringVar()
	caja_clave = Entry(v1,textvariable=usuario_nombre)
	caja_clave.grid(row=4,column=3)

	b0=Button(v1,text="INICIAR",command=lambda: listaCategorias(v,v1)).grid(row=6,column=2)
	b1=Button(v1,text="VOLVER",command=lambda: volverinicio(v1,v)).grid(row=6,column=3)
