import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
from datetime import datetime
#"crear ventana principal"
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Libro pacientes y doctores")
ventanaPrincipal.geometry("900x900")
#crear contenedores notebook(pestañas)
pestañas=ttk.Notebook(ventanaPrincipal)
#crear frames(uno por pestañas)
frame_pacientes=ttk.Frame(pestañas)
#agregar pestañas al notebook
pestañas.add(frame_pacientes,text="Pacientes")
#mostrar las pestañas en la ventana
pestañas.pack(expand=True,fill="both")
#Función para enmascarar fecha
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit,texto))
    formato_final=""
    if len (limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len (limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio      
    if fechaN.get()!=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0,formato_final)
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year- fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
#funcion guardar archivo 
def guardar_en_archivo():
    with open ("pacientePeso.txt","w",encoding="utf-8")as archivo: # la "w"es modo de paertura del archivo para guardar(write) 
        for paciente in paciente_data:
            archivo.write(
                f"{paciente['Nombre']}|"
                f"{paciente['Fecha de nacimiento']} |"
                f"{paciente['Edad']}|"
                f"{paciente['Genero']}|{paciente['Grupo Sanguineo']}|"
                f"{paciente['Peso']}|"
                f"{paciente['Tipo de seguro']}|{paciente['Centro médico']}\n"
            )
#CARGAR DESDE ARCHIVO 
def cargar_desde_archivo_pacientes():
    try:
        with open("pacientePeso.txt","r",encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==8:
                    paciente={
                        "Nombre":datos[0],
                        "Fecha de nacimiento":datos[1],
                        "Edad":datos[2],
                        "Genero":datos[3],
                        "Peso":datos[4],
                        "Grupo Sanguineo":datos[5],
                        "Tipo de seguro":datos[6],
                        "Centro médico":datos[7]
                   }                    
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("pacientePeso.txt","w",encoding="utf-8").close()
#Funcion para eliminar paciente
def eliminarPaciente():
    seleccionado=treeview.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar Paciente", f"¿Esta seguro de eliminar el paciente'{treeview.item(id_item,'values')[0]}'?"):del paciente_data[indice]
        guardar_en_archivo() #guardar los cambios en el archivo
        cargar_treeview()
        messagebox.showinfo("Eliminar Paciente","Paciente eliminado exitosamente.")       
    else:
           messagebox.showwarning("Eliminar Paciente","No se ha seleccionado ningun paciente.")
           return
#Lista de pacientes (inicialmente vacía)
paciente_data=[]
#función pra registrar paciente
def registrarPaciente():
    paciente={
        "Nombre": nombreP.get(),
        "Fecha de nacimiento":fechaN.get(),
        "Edad":edadVar.get(),
        "Genero":genero.get(),
        "Peso":peso.get(),
        "Grupo Sanguineo":entryGrupoSanguineo.get(),
        "Tipo de seguro":tipo_seguro.get(),
        "Centro médico":centro_medico.get()
         }
    #agregar a la lista
    paciente_data.append(paciente)
    guardar_en_archivo()
    #Cargar el treeview
    cargar_treeview()
def cargar_treeview():
     #limpiar el treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
#insertar cada paciente
    for i, item in enumerate(paciente_data):
        treeview.insert(
           "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de nacimiento"],
                item["Edad"],
                item["Genero"],
                item["Peso"],
                item["Grupo Sanguineo"],
                item["Tipo de seguro"],
                item["Centro médico"]
            )
        )
# #nombre
labelNombreP=tk.Label(frame_pacientes,text="Nombre")
labelNombreP.grid(row=0,column=0,sticky="w",padx=5,pady=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,padx=5,pady=5,sticky="w")
#fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes,text="Fecha de nacimiento:")
labelFechaN.grid(row=1,column=0,sticky="w",padx=5,pady=5)
#llamando ala funcion de enmascarar fecha
validacion_fecha=ventanaPrincipal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes,validate="key",validatecommand=(validacion_fecha,'%P'))
fechaN.grid(row=1,column=1,padx=5,pady=5,sticky="w") 
#edad(readonly)
labelEdad=tk.Label(frame_pacientes,text="Edad:")
labelEdad.grid(row=2,column=0,padx=5,pady=5,sticky="w")
edadVar=tk.StringVar()
edad=tk.Entry(frame_pacientes,state="readonly",textvariable=edadVar)
edad.grid(row=2,column=1,sticky="w",padx=5,pady=5)
#genero(radio button)
labelGenero=tk.Label(frame_pacientes,text="Genero")
labelGenero.grid(row=3,column=0,sticky="w",padx=5,pady=5)
genero=tk.StringVar()
genero.set("Maculino")#valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes,text="Mascuino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,sticky="w",padx=5,pady=5)
radioFemenino=ttk.Radiobutton(frame_pacientes,text="femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,padx=5,pady=5,sticky="w")
#peso
labelPeso=tk.Label(frame_pacientes,text="Peso:")
labelPeso.grid(row=5,column=0,sticky="w",padx=5,pady=5)
peso=tk.Entry(frame_pacientes)
peso.grid(row=5,column=1,padx=5,pady=5,sticky="w")
#Grupo Sanguíneo
labelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo sanguíneo")
labelGrupoSanguineo.grid(row=6,column=0,sticky="w",padx=5,pady=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=6,column=1,sticky="w",padx=5,pady=5)
#tipo de seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de seguro")
labelTipoSeguro.grid(row=7,column=0,sticky="w",padx=5,pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público")#valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes,values=["Público","Privado","Ninguno"],textvariable=tipo_seguro)
comboTipoSeguro.grid(row=7,column=1,sticky="w",padx=5,pady=5)
#centro medico
labelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud")
labelCentroMedico.grid(row=8,column=0,sticky="w",padx=5,pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital central")#valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes,values=["Hospital central","Centro Sur","Clínica Norte"],textvariable=centro_medico)
comboCentroMedico.grid(row=8,column=1,sticky="w",padx=5,pady=5)
#frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=9,column=0,columnspan=2,padx=5,pady=5,sticky="w")
#botomn registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command=registrarPaciente)
btn_registrar.grid(row=9,column=0,padx=5,pady=5)
btn_registrar.configure(bg="#48FF68",fg="white")
#boton eliminar
btn_eliminar=tk.Button(btn_frame,text="Eliminar", command=eliminarPaciente)
btn_eliminar.grid(row=9,column=1,padx=5)
btn_eliminar.configure(bg="#FF0014",fg="white")
#CREAR TREEVIEW PARA MOSTRAR PACIENTES
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre","FechaN","Edad","Genero","Peso","GrupoS","TipoS","CentroM"),show="headings")
#DEFINIR ENCABEZADOS
treeview.heading("Nombre",text="Nombre completo")
treeview.heading("FechaN",text="Fecha de nacimiento")
treeview.heading("Edad",text="Edad")
treeview.heading("Genero",text="Genero")
treeview.heading("Peso",text="Peso")
treeview.heading("GrupoS",text="Grupo Sanguíneo")
treeview.heading("TipoS",text="Tipo seguro")
treeview.heading("CentroM",text="Centro Médico")
#definir anchos de columnas
treeview.column("Nombre",width=120)
treeview.column("FechaN",width=120)
treeview.column("Edad",width=50,anchor="center")
treeview.column("Genero",width=60,anchor="center")
treeview.column("Peso",width=60,anchor="center")
treeview.column("GrupoS",width=100,anchor="center")
treeview.column("TipoS",width=100,anchor="center")
treeview.column("CentroM",width=120)
#ubicar treeview en cuadrícula
treeview.grid(row=10,column=0,columnspan=2,pady=10,sticky="nsew")
#scrobal vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
scroll_y.grid(row=10,column=2,sticky="ns")
cargar_desde_archivo_pacientes()
ventanaPrincipal.mainloop()
