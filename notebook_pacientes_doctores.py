#importacion de librerias
import tkinter as tk
from tkinter import ttk, messagebox
#CREAR VENTANA PRINCIPAL
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("800x600")
ventana_principal.configure(bg="#FA8072")
#CREAR CONTENEDOR NOTEBOOK(PESTAÑAS)
pestañas=ttk.Notebook(ventana_principal)

#------------PACIENTES------------------
#CREAR FRAMES(UNO POR PESTAÑAS)
frame_pacientes=ttk.Frame(pestañas)
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
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)
#GRUPOSANGUINEO
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", pady=5, padx=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5, column=1, sticky="w", padx=5, pady=5)
#TIPO DE SEGURO
labelTipoSeguro=tk.Label(frame_pacientes, text="Tipo de Seguro:")
labelTipoSeguro.grid(row=6, column=0, sticky="w", padx=5, pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Publico", "Privado","Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6, column=1, sticky="w", padx=5, pady=5)
#CENTRO MEDICO
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de salud:")
labelCentroMedico.grid(row=7, column=0, sticky="w", padx=5, pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central","Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5)
#FRAME PARA LOS BOTONES
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=8, column=0, columnspan=2, pady=5, sticky="w")
#BOTON REGISTRAR
btn_registrar=tk.Button(btn_frame, text="Registrar", command="")
btn_registrar.grid(row=8, column=0, padx=5)
#BOTON ELIMINAR
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.grid(row=8, column=1, padx=5)
#CREAR TREEVIEW PARA MOSTRAR PACIENTES
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS","TipoS", "CentroM"), show="headings")
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Sangiuineo")
treeview.heading("CentroM", text="Centro Medico")
#DEFINIR ANCHOS DE COLUMNAS
treeview.column("Nombre", width=120) 
treeview.column("FechaN", width=120) 
treeview.column("Edad", width=50, anchor="center") 
treeview.column("Genero", width=60, anchor="center") 
treeview.column("GrupoS", width=100, anchor="center") 
treeview.column("TipoS", width=100, anchor="center") 
treeview.column("CentroM", width=120)
#UBICAR EL TREEVIEW EN LA CUADRICULA
treeview.grid(row=10, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")
#SCROLBAR VERTICAL
scroll_y=ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
scroll_y.grid(row=10, column=2, sticky="ns")


#DOCTORES(TODO)
#------------DOCTORES-------------------
#-----------WIDGETS------------
#Nombre
labelNombre=tk.Label(frame_doctores, text="Nombre Completo:")
labelNombre.grid(row=0, column=0, sticky="w", pady=10, padx=5)
nombreP=tk.Entry(frame_doctores)
nombreP.grid(row=0, column=1, sticky="w", pady=10, padx=5)
#ESPECIALIDAD
labelEspecialidad=tk.Label(frame_doctores, text="Especialidad:")
labelEspecialidad.grid(row=1, column=0, sticky="w", padx=5, pady=10)
especialidad=tk.StringVar()
especialidad.set("Neurologia")
comboEspecialidad=ttk.Combobox(frame_doctores, values=["Neurologia","Cardiologia","Pediatria", "Traumatologia"], textvariable=especialidad)
comboEspecialidad.grid(row=1, column=1, sticky="w", padx=5, pady=10)
#EDAD 
labelEdad=tk.Label(frame_doctores, text="Edad:")
labelEdad.grid(row=2, column=0, padx=5, pady=10, sticky="w")
spinEdad=ttk.Spinbox(frame_doctores, from_=0, to=99)
spinEdad.grid(row=2, column=1, padx=5, pady=10, sticky="w")
#TELEFONO
labelTelefono=tk.Label(frame_doctores, text="Telefono:")
labelTelefono.grid(row=3, column=0, sticky="w", pady=10, padx=5)
telefonoP=tk.Entry(frame_doctores)
telefonoP.grid(row=3, column=1, sticky="w", pady=10, padx=5)
#FRAME PARA LOS BOTONES
btn_frame=tk.Frame(frame_doctores)
btn_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")
#BOTON REGISTRAR
btn_registrar=tk.Button(btn_frame, text="Registrar", command="")
btn_registrar.grid(row=4, column=0, padx=5)
#BOTON ELIMINAR
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.grid(row=4, column=1, padx=5)
#CREAR TREEVIEW PARA MOSTRAR DOCTORES
treeview=ttk.Treeview(frame_doctores,columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("Especialidad", text="Especialidad")
treeview.heading("Edad", text="Edad")
treeview.heading("Telefono", text="Telefono")
#DEFINIR ANCHOS DE COLUMNAS
treeview.column("Nombre", width=120) 
treeview.column("Especialidad", width=120) 
treeview.column("Edad", width=50, anchor="center") 
treeview.column("Telefono", width=60, anchor="center") 
treeview.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")
#SCROLBAR VERTICAL
scroll_y=ttk.Scrollbar(frame_doctores, orient="vertical", command=treeview.yview)
scroll_y.grid(row=5, column=2, sticky="nsew")



ventana_principal.mainloop()