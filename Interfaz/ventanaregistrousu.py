from tkinter import *
from ventanacategorias import *

def volverinicio(vd,vo):
	vd.destroy()
	vo.deiconify()

def crearUsuario(v):
	v_usu=Toplevel(v) # Crea una ventana hija
	v.withdraw()
	v_usu.geometry("300x230")
	v_usu.title('Registar Usuario')
	
	nombre=Label(v_usu,text="Nombre : ").grid(row=2,column=1)
	nom_nombre = StringVar()
	caja_nombre = Entry(v_usu,textvariable=nom_nombre).grid(row=2,column=2)

	apellido=Label(v_usu,text="Apellido : ").grid(row=3,column=1)
	ap_nombre = StringVar()
	caja_apellido = Entry(v_usu,textvariable=ap_nombre).grid(row=3,column=2)

	mail=Label(v_usu,text="Correo : ").grid(row=4,column=1)
	mail_nombre = StringVar()
	caja_clave = Entry(v_usu,textvariable=mail_nombre).grid(row=4,column=2)

	usuario=Label(v_usu,text="Usuario : ").grid(row=5,column=1)
	usuario_nombre = StringVar()
	caja_usuario = Entry(v_usu,textvariable=usuario_nombre).grid(row=5,column=2)

	clave=Label(v_usu,text="Contraseña : ").grid(row=6,column=1)
	clave_nombre = StringVar()
	caja_clave = Entry(v_usu,textvariable=clave_nombre).grid(row=6,column=2)

	reclave=Label(v_usu,text="Repetir Contraseña : ").grid(row=7,column=1)
	reclave_nombre = StringVar()
	caja_reclave = Entry(v_usu,textvariable=reclave_nombre).grid(row=7,column=2)

	direccion=Label(v_usu,text="Direction : ").grid(row=8,column=1)
	direccion_nombre = StringVar()
	direccion_clave = Entry(v_usu,textvariable=direccion_nombre).grid(row=8,column=2)

	clave=Label(v_usu,text=" : ").grid(row=9,column=1)
	clave_nombre = StringVar()
	caja_clave = Entry(v_usu,textvariable=usuario_nombre).grid(row=9,column=2)

	espacio=Label(v_usu,text="").grid(row=10,column=1)

	b0=Button(v_usu,text="GUARDAR",command=lambda: listaCategorias(v,v_usu)).grid(row=11,column=1)
	b1=Button(v_usu,text="CANCELAR",command=lambda: volverinicio(v_usu,v)).grid(row=11,column=2)

	v_usu.mainloop()