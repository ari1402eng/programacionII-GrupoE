#spinbox de numeros del 1 al 10
import tkinter as tk 
from tkinter import messagebox
ventana=tk.Tk()
ventana.geometry("500x500")
ventana.configure(bg="lightBlue")
labelEdad=tk.Label(ventana, text="Edad:")
labelEdad.grid(row=0, column=0, padx=10, pady=10, sticky="w")
spin=tk.Spinbox(ventana, from_=1, to=99)
spin.grid(row=0, column=1, padx=10, pady=10)
def mostrarEdad():
    messagebox.showinfo("Edad", f"La edad seleccionada es : {spin.get()}")
boton=tk.Button(ventana, text="Obtener valor", command=mostrarEdad)
boton.grid(row=1, column=1, padx=10, pady=10)
#genero 
labelGenero=tk.Label(ventana, text="Genero:")
labelGenero.grid(row=2,column=0, padx=10, pady=10, sticky="w")
#spinbox de texto para genero
genero=tk.Spinbox(ventana, values=("Maculino", "Femenino", "Otro"))
genero.grid(row=2, column=1, padx=10, pady=10)
def mostrarGenero():
    messagebox.showinfo("Genero", f"El genero seleccionado es : {genero.get()}")
botonGenero=tk.Button(ventana, text="Obtener genero", command=mostrarGenero)
botonGenero.grid(row=3, column=1, padx=10,pady=10)


ventana.mainloop()