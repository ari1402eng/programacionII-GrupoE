#importacion de librerias
import tkinter as tk
from tkinter import ttk, messagebox
#CREAR VENTANA PRINCIPAL
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("400x600")
ventana_principal.configure(bg="#FA8072")
#CREAR CONTENEDOR NOTEBOOK(PESTAÑAS)
pestañas=ttk.Notebook(ventana_principal)
#CREAR FRAMES(UNO POR PESTAÑAS)
frame_pacientes=ttk.Frame(pestañas)

#------------PACIENTES------------------
#AGREGAR PESTAÑAS AL NOTEBOOK
pestañas.add(frame_pacientes, text="Pacientes")
#MOSTRAR LAS PESTAÑAS EN LA VENTANA
pestañas.pack(expand=True, fill="both")

#------------DOCTORES-------------------
#CREAR FRAMES(UNO POR PESTAÑAS)
frame_doctores=ttk.Frame(pestañas)
#AGREGAR PESTAÑAS AL NOTEBOOK
pestañas.add(frame_doctores, text="Doctores")
#MOSTRAR LAS PESTAÑAS EN LA VENTANA
pestañas.pack(expand=True, fill="both")

#-----------WIDGETS------------
#Nombre
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo:")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)
#fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes, text="Fecha de Nacimiento:")
labelFechaN.grid(row=1, column=0, sticky="w", pady=5, padx=5)
fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1, column=1, sticky="w", pady=5, padx=5)
#EDAD (solo lectura)
labelEdad=tk.Label(frame_pacientes, text="Edad:")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadP=tk.Entry(frame_pacientes, state="readonly")
edadP.grid(row=2, column=1, sticky="w", pady=5, padx=5)
#GENERO(RADIOBUTTON)
labelGenero=tk.Label(frame_pacientes, text="Genero:")
labelGenero.grid(row=3, column=0, pady=5, padx=5, sticky="w")
genero=tk.StringVar()
genero.set("Masculino")
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=3, column=2, sticky="w", padx=5)
#GRUPOSANGUINEO
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=4, column=0, sticky="w", pady=5, padx=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=4, column=1, sticky="w", padx=5, pady=5)
#TIPO DE SEGURO
labelTipoSeguro=tk.Label(frame_pacientes, text="Tipo de Seguro:")
labelTipoSeguro.grid(row=5, column=0, sticky="w", padx=5, pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Publico", "Privado","Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5, column=1, sticky="w", padx=5, pady=5)
#CENTRO MEDICO
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de salud:")
labelCentroMedico.grid(row=6, column=0, sticky="w", padx=5, pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central","Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=6, column=1, sticky="w", padx=5, pady=5)



ventana_principal.mainloop()