#importacion de librerias
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
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
#FUNCION PARA ENMASCARAR FECHA
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit, texto))
    formato_final=""
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
    if fechaN.get()!=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0, formato_final)
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year-fecha_nacimiento.year 
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
def guardar_en_archivo():
    with open("paciente.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(
            f"{paciente['Nombre']}|"
            f"{paciente['Fecha de Nacimiento']}|"
            f"{paciente['Edad']}|"
            f"{paciente['Genero']}|{paciente['Grupo Sanguineo']}|"
            f"{paciente['Tipo de Seguro']}|{paciente['Centro Medico']}\n"
        )
def cargar_desde_archivo_pacientes():
    try:
        with open("paciente.txt","r", encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==7:
                    paciente={
                        "Nombre":datos[0],
                        "Fecha de Nacimiento":datos[1],
                        "Edad":datos[2],
                        "Genero":datos[3],
                        "Grupo Sanguineo":datos[4],
                        "Tipo de seguro":datos[5],
                        "Centro médico":datos[6]
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("paciente.txt", "w", encoding="utf-8").close()
#LISTA DE PACIENTES(INICIALMENTE VACIA)
paciente_data=[]
#FUNCION PARA REGISTRAR PACIENTE
def registrarPaciente():
    #crear un diccionario con los datos ingresados
    paciente = {
        "Nombre": nombreP.get(),
        "Fecha de Nacimiento": fechaN.get(),
        "Edad": edadVar.get(),
        "Genero": genero.get(),
        "Grupo Sanguineo": entryGrupoSanguineo.get(),
        "Tipo de Seguro": tipo_seguro.get(),
        "Centro Medico": centro_medico.get()
    }
    #AGREGAR PACIENTE A LA LISTA
    paciente_data.append(paciente)
    guardar_en_archivo()
    #CARGAR AL TREEVIEW
    cargar_treeview()
def cargar_treeview():
    #Limpiear el treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #Insertar cada paciente 
    for i, item in enumerate(paciente_data):
        treeview.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Genero"],
                item["Grupo Sanguineo"],
                item["Tipo de Seguro"],
                item["Centro Medico"]
            )
        )
# #LISTA DE DOCTORES(INICIALMENTE VACIA)
# doctor_data=[]
# #FUNCION PARA REGISTRAR PACIENTE
# def registrarDoctor():
#     #crear un diccionario con los datos ingresados
#     doctor = {
#         "Nombre": nombreD.get(),
#         "Especialidad": especialidad.get(),
#         "Edad": spinEdadD.get(),
#         "Telefono": telefonoD.get(),
#     }
#     #AGREGAR PACIENTE A LA LISTA
#     doctor_data.append(doctor)
#     #CARGAR AL TREEVIEW
#     cargar_treeview()
# def cargar_treeview():
#     #Limpiear el treeview
#     for doctor in treeviewD.get_children():
#         treeviewD.delete(doctor)
#     #Insertar cada paciente 
#     for i, item in enumerate(doctor_data):
#         treeviewD.insert(
#             "", "end", iid=str(i),
#             values=(
#                 item["Nombre"],
#                 item["Especialidad"],
#                 item["Edad"],
#                 item["Telefono"]
#             )
#         )
    
#------------DOCTORES-------------------
#CREAR FRAMES(UNO POR PESTAÑAS)
# frame_doctores=ttk.Frame(pestañas)
#AGREGAR PESTAÑAS AL NOTEBOOK
# pestañas.add(frame_doctores, text="Doctores")
# #MOSTRAR LAS PESTAÑAS EN LA VENTANA
# pestañas.pack(expand=True, fill="both")

#-----------WIDGETS------------
#Nombre
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo:")
labelNombre.grid(row=0, column=0, sticky="w", pady=5, padx=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)
#fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes, text="Fecha de Nacimiento:")
labelFechaN.grid(row=1, column=0, sticky="w", pady=5, padx=5)
validacion_fecha=ventana_principal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes, validate="key", validatecommand=(validacion_fecha, '%P'))
fechaN.grid(row=1, column=1, sticky="w", pady=5, padx=5)
#EDAD (solo lectura)
labelEdad=tk.Label(frame_pacientes, text="Edad:")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadVar=tk.StringVar()
edadP=tk.Entry(frame_pacientes, textvariable=edadVar,state="readonly")
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
btn_registrar=tk.Button(btn_frame, text="Registrar", command=registrarPaciente, bg="green", fg="white")
btn_registrar.grid(row=8, column=0, padx=5)
#BOTON ELIMINAR
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="", bg="red", fg="white")
btn_eliminar.grid(row=8, column=1, padx=5)
#CREAR TREEVIEW PARA MOSTRAR PACIENTES
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS","TipoS", "CentroM"), show="headings")
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Seguro")
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


# #------------DOCTORES-------------------
# #-----------WIDGETS------------
# #TITULO
# labelTitulo=tk.Label(frame_doctores, text="Registro de Doctores")
# labelTitulo.grid(row=0, column=0, sticky="w", pady=10, padx=120)
# #Nombre
# labelNombreD=tk.Label(frame_doctores, text="Nombre Completo:")
# labelNombreD.grid(row=1, column=0, sticky="w", pady=10, padx=5)
# nombreD=tk.Entry(frame_doctores)
# nombreD.grid(row=1, column=1, sticky="w", pady=10, padx=5)
# #ESPECIALIDAD
# labelEspecialidad=tk.Label(frame_doctores, text="Especialidad:")
# labelEspecialidad.grid(row=2, column=0, sticky="w", padx=5, pady=10)
# especialidad=tk.StringVar()
# especialidad.set("Neurologia")
# comboEspecialidad=ttk.Combobox(frame_doctores, values=["Neurologia","Cardiologia","Pediatria", "Traumatologia"], textvariable=especialidad)
# comboEspecialidad.grid(row=2, column=1, sticky="w", padx=5, pady=10)
# #EDAD 
# labelEdadD=tk.Label(frame_doctores, text="Edad:")
# labelEdadD.grid(row=3, column=0, padx=5, pady=10, sticky="w")
# spinEdadD=ttk.Spinbox(frame_doctores, from_=0, to=99)
# spinEdadD.grid(row=3, column=1, padx=5, pady=10, sticky="w")
# #TELEFONO
# labelTelefono=tk.Label(frame_doctores, text="Telefono:")
# labelTelefono.grid(row=4, column=0, sticky="w", pady=10, padx=5)
# telefonoD=tk.Entry(frame_doctores)
# telefonoD.grid(row=4, column=1, sticky="w", pady=10, padx=5)
# #FRAME PARA LOS BOTONES
# btn_frame=tk.Frame(frame_doctores)
# btn_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky="w")
# #BOTON REGISTRAR
# btn_registrar=tk.Button(btn_frame, text="Registrar", command=registrarDoctor, bg="green", fg="white")
# btn_registrar.grid(row=5, column=0, padx=5)
# #BOTON ELIMINAR
# btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="", bg="red", fg="white")
# btn_eliminar.grid(row=5, column=1, padx=5)
# #CREAR TREEVIEW PARA MOSTRAR DOCTORES
# treeviewD=ttk.Treeview(frame_doctores,columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
# treeviewD.heading("Nombre", text="Nombre Completo")
# treeviewD.heading("Especialidad", text="Especialidad")
# treeviewD.heading("Edad", text="Edad")
# treeviewD.heading("Telefono", text="Telefono")
# #DEFINIR ANCHOS DE COLUMNAS
# treeviewD.column("Nombre", width=120) 
# treeviewD.column("Especialidad", width=120) 
# treeviewD.column("Edad", width=50, anchor="center") 
# treeviewD.column("Telefono", width=60, anchor="center") 
# treeviewD.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")
# #SCROLBAR VERTICAL
# scroll_y=ttk.Scrollbar(frame_doctores, orient="vertical", command=treeviewD.yview)
# scroll_y.grid(row=6, column=2, sticky="nsew")

    
cargar_desde_archivo_pacientes()
ventana_principal.mainloop()