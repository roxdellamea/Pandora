from tkinter import *
import tkinter.ttk as ttk

def volverinicio(vc,vo):
	vc.destroy()
	vo.deiconify()

def listaCategorias(v,vc):
	v2=Toplevel() # Crea una ventana hija
	vc.withdraw()
	Label(v2,text="Seleccione categoria").pack()
	
	cbx = ttk.Combobox(values=["uno", "dos", "tres", "cuatro", "cinco"])
	cbx.set("uno")
	cbx.configure()
	
	cbx.pack()
	cbx.master.title("ttk widgets")
	b2=Button(v2,text="BUCSCAR",command=lambda: volverinicio(v2)).pack()
	
	cbx.mainloop()