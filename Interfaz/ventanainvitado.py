from tkinter import *

def volverinicio(vd,vo):
	vd.destroy()
	vo.deiconify()

def inicioinvitado(v):
	v2=Toplevel(v) # Crea una ventana hija
	v.withdraw()
	lb_categoria=Label(v2,text="Seleccione categoria")
	lb_categoria.grid(row=1,column=2)
	b2=Button(v2,text="VOLVER",command=lambda: volverinicio(v2,v)).grid(row=2,column=2)



 

 

 


	
