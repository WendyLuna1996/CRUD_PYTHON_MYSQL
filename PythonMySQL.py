
import tkinter as tk


#Importar los modulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Clientes import *

from Conexion import *


class FormularioClientes:
 
    global base
    base=None

    global textBoxId
    texBoxId =None 

    global texBoxNombres
    texBoxNombre =None

    global texBoxApellidos
    texBoxApellidos =None

    global combo
    combo =None

    global groupBox
    groupBox =None

    global tree
    tree =None

def actualizarTreeview():
 
     try:
        #Borrar todos los elementos actuales del TreeView
        tree.delete(*tree.get_children())

        #Obtener los nuevos datos que deseamos mostrar
        datos = CClientes.mostrarClientes()

        #Insertar los nuevos datos en el TreeView
        for row in CClientes.mostrarClientes():
           tree.insert("","end",values=row)

     except ValueError as error:
        print ("Error al actualizar tabla {}".format(error))


def guardarRegistros():
  
     global texBoxNombres,texBoxApellidos,combo,groupBox

     try:
        #Verificar si los widgets estan inicializados
       if texBoxNombres is None or texBoxApellidos is None or combo is None:
        print("Los widgets no estan inicializados")
        return

             
       nombres= texBoxNombres.get()
       apellidos = texBoxApellidos.get()
       sexo = combo.get()

       CClientes.ingresarClientes(nombres,apellidos,sexo)
       messagebox.showinfo("Informacion","Los datos fueron guardados")

       actualizarTreeview()
     
       #Limpiamos los campos

       texBoxNombres.delete(0,END)
       texBoxApellidos.delete(0,END)

     except ValueError as error:
        print("Error al ingresar los Datos{}".format(error)) 
 
  
def modificarRegistros(idUsuario,nombres,apellidos,sexo):
   
  global texBoxId,texBoxNombres,texBoxApellidos,combo,groupBox

  try:
    #Verificar si los widgets estan inicializados
    if texBoxId is None or texBoxNombres is None or texBoxApellidos is None or combo is None:
     print("Los widgets no estan inicializados")
     return
    

    IdUsuario = texBoxId.get() 
    nombres = texBoxNombres.get()
    apellidos = texBoxApellidos.get()
    sexo = combo.get()


    CClientes.modificarClientes(IdUsuario,nombres,apellidos,sexo)
    messagebox.showinfo("Informacion","Los datos fueron actualizados")

    actualizarTreeview()

    #Limpiamos los campos
    texBoxId.delete(0,END)
    texBoxNombres.delete(0,END)
    texBoxApellidos.delete(0,END)


  except ValueError as error:
        print("Error al modificar los Datos{}".format(error))    

def eliminarRegistros():

  global texBoxId,texBoxNombres,texBoxApellidos

  try:
    #Verificar si los widgets estan inicializados
    if texBoxId is None:
       print("Los widgets no estan inicializados")
       return 
      
 
    IdUsuarios = texBoxId.get()
    
    CClientes.EliminarClientes(IdUsuarios)
    messagebox.showinfo("Informacion","Los datos fueron eliminados")

    actualizarTreeview()

    #Limpiamos los campos
    texBoxId.delete(0,END)
    texBoxNombres.delete(0,END)
    texBoxApellidos.delete(0,END)
  

  except ValueError as error:
      print("Error al modificar los datos {}".format(error))

def seleccionarRegistro(event):
 

 try:
    itemSeleccionado = tree.focus()

    if itemSeleccionado:
      #Obtener los valores por columna 
      values = tree.item(itemSeleccionado)['values']

      #Establecer los valores en los widgets Entry

      texBoxId.delete(0,END)
      texBoxId.insert(0,values[0])
      texBoxNombres.delete(0,END)
      texBoxNombres.insert(0,values[1])
      texBoxApellidos.delete(0,END)
      texBoxApellidos.insert(0,values[2])
      combo.set(values[3])

 except ValueError as error:
     print("Error al seleccinar registro{}".format(error))

     
def Formulario():

  global texBoxId
  global texBoxNombres
  global texBoxApellidos
  global combo
  global base
  global groupBox
  global tree


try:
    base = Tk()
    base.geometry("1200x300")
    base.title("Formulario Python")

    groupBox = LabelFrame(base,text="Datos del Personal",padx=5,pady=5)
    groupBox.grid(row=0,column=0,padx=10,pady=10)

    labelId=Label(groupBox,text="Id:",width=13,font=("Arial",12)).grid(row=0,column=0)
    texBoxId = Entry(groupBox)
    texBoxId.grid(row=0,column=1)

    labelNombres=Label(groupBox,text="Nombres:",width=13,font=("Arial",12)).grid(row=1,column=0)
    texBoxNombres = Entry(groupBox)
    texBoxNombres.grid(row=1,column=1)

    labelApellidos=Label(groupBox,text="Apellidos:",width=13,font=("Arial",12)).grid(row=2,column=0)
    texBoxApellidos = Entry(groupBox)
    texBoxApellidos.grid(row=2,column=1)

    LabelSexo=Label(groupBox,text="Sexo:",width=13,font=("Arial",12)).grid(row=3,column=0)
    seleccionSexo = tk.StringVar()
    combo=ttk.Combobox(groupBox,values=["Maculino","Femenino"],textvariable=seleccionSexo)
    combo.grid(row=3,column=1)
    seleccionSexo.set("Masculino")

    Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=4,column=0)
    Button(groupBox,text="Modificar",width=10,command=modificarRegistros).grid(row=4,column=1)
    Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=4,column=2)

    groupBox = LabelFrame(base,text="Lista del Personal",padx=5,pady=5)
    groupBox.grid(row=0,column=1,padx=5,pady=5)
    
    #Crear Un TreeView

    #Configurar las columnas

    tree = ttk.Treeview()
    ttk.Treeview(groupBox,columns=("Id,","Nombres","Apellidos","Sexo"),show='headings',height=5,)
    tree.column("# 1",anchor=CENTER)
    tree.heading("# 1",text="Id")
    tree.column("# 2",anchor=CENTER)
    tree.heading("# 2",text="Nombres")
    tree.column("# 3",anchor=CENTER)
    tree.heading("# 3",text="Apellidos")
    tree.column("# 4",anchor=CENTER)
    tree.heading("# 4",text="Sexo")

     #Agregar los datos a la tabla
     # Mostrar la tabla

    for row in CClientes.mostrarClientes():
     tree.insert("","end",values=row)

     #Ejecutar la funcion de hacer click y mostrar el resultado en los Entry

     tree.bind("<<TreeviewSelect>>",seleccionarRegistro)


     tree.pack()


     base.mainloop()
    
except ValueError as error:
  print("Error al mostrar la interfaz,error: {}".format(error)) 
            
          
          
Formulario()


































