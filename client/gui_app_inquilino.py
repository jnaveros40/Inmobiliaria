from sre_parse import State
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model.inquilino_dao import crear_tabla_inquilino, borrar_tabla_inquilino, editar, guardar, Inquilino, listar_inquilino, eliminar 
from model.apartamento_dao import listar_apartamento

def barra_menu_inquilino(root):
    barra_menu = tk.Menu(root)
       
    root.config(menu = barra_menu, width=300, height = 300)
    
    menu_inquilino = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'Inquilino', menu=menu_inquilino)
    menu_inquilino.add_command(label='Crear base de datos', command=crear_tabla_inquilino)
    menu_inquilino.add_command(label='Eliminar base de datos', command= borrar_tabla_inquilino)
    
    barra_menu.add_command(label='Salir', command=root.destroy)

class Frame_inquilino (tk.Frame):
    def __init__ (self, root = None):
        super().__init__(root,width=650, height=720)
        self.root = root
        self.pack()
        
        self.ID_INQUILINO = None

        self.campos_agregar_inquilino()
        self.desabilitar_campos()
        self.tabla_inquilino()
        self.tabla_datos_apartamentos()

    def campos_agregar_inquilino(self):
        self.borrar_espacios = tk.StringVar()
        
        #agregar los label
        self.label_arrendatario = tk.Label(self, text=" ARRENDATARIO ")
        self.label_arrendatario.config(font=('Times New Roman',12,"bold"))
        self.label_arrendatario.grid(row=0,column=0, columnspan=3)

        self.label_co_arrendatario = tk.Label(self, text=" CO - ARRENDATARIO ")
        self.label_co_arrendatario.config(font=('Times New Roman',12,"bold"))
        self.label_co_arrendatario.grid(row=0,column=3, columnspan=3)
        
        self.label_Nombre = tk.Label(self, text= "Nombre: ")
        self.label_Nombre.config(font=('Times New Roman',12,"bold"))
        self.label_Nombre.grid(row=1, column=0)
        self.mi_Nombre = tk.StringVar()
        self.entry_Nombre = tk.Entry(self, textvariable=self.mi_Nombre)
        self.entry_Nombre.config(width=50)
        self.entry_Nombre.grid(row=1, column=1, columnspan=2)
        
        self.label_Apellidos = tk.Label(self, text= "Apellidos: ")
        self.label_Apellidos.config(font=('Times New Roman',12,"bold"))
        self.label_Apellidos.grid(row=2, column=0)
        self.mi_Apellidos = tk.StringVar()
        self.entry_Apellidos = tk.Entry(self, textvariable=self.mi_Apellidos)
        self.entry_Apellidos.config(width=50)
        self.entry_Apellidos.grid(row=2, column=1, columnspan=2)

        self.label_Cedula = tk.Label(self, text= "Cedula: ")
        self.label_Cedula.config(font=('Times New Roman',12,"bold"))
        self.label_Cedula.grid(row=3, column=0)
        self.mi_Cedula = tk.StringVar()
        self.entry_Cedula = tk.Entry(self, textvariable=self.mi_Cedula)
        self.entry_Cedula.config(width=50)
        self.entry_Cedula.grid(row=3, column=1, columnspan=2)

        self.label_Telefono = tk.Label(self, text= "Telefono: ")
        self.label_Telefono.config(font=('Times New Roman',12,"bold"))
        self.label_Telefono.grid(row=4, column=0)
        self.mi_Telefono = tk.StringVar()
        self.entry_Telefono = tk.Entry(self, textvariable=self.mi_Telefono)
        self.entry_Telefono.config(width=50)
        self.entry_Telefono.grid(row=4, column=1, columnspan=2)

        self.label_Correo = tk.Label(self, text= "Correo: ")
        self.label_Correo.config(font=('Times New Roman',12,"bold"))
        self.label_Correo.grid(row=5, column=0)
        self.mi_Correo = tk.StringVar()
        self.entry_Correo = tk.Entry(self, textvariable=self.mi_Correo)
        self.entry_Correo.config(width=50)
        self.entry_Correo.grid(row=5, column=1, columnspan=2)

        self.label_Direccion = tk.Label(self, text = " Direccion: ")
        self.label_Direccion.config(font=('Times New Roman',12,"bold"))
        self.label_Direccion.grid(row=6,column=0)
        self.mi_Direccion = tk.StringVar()
        self.entry_Direccion = tk.Entry(self, textvariable=self.mi_Direccion)
        self.entry_Direccion.config(width=50)
        self.entry_Direccion.grid(row=6, column=1, columnspan=2)

        self.label_Apartamento = tk.Label(self, text = " Apartamento: ")
        self.label_Apartamento.config(font=('Times New Roman',12,"bold"))
        self.label_Apartamento.grid(row=6,column=2)
        self.mi_Apartamento = tk.StringVar()
        self.entry_Apartamento = tk.Entry(self, textvariable=self.mi_Apartamento)
        self.entry_Apartamento.config(width=30)
        self.entry_Apartamento.grid(row=6, column=3) 

        self.label_Valor = tk.Label(self, text = " Valor: ")
        self.label_Valor.config(font=('Times New Roman',12,"bold"))
        self.label_Valor.grid(row=6,column=4)
        self.mi_Valor = tk.StringVar()
        self.entry_Valor = tk.Entry(self, textvariable=self.mi_Valor)
        self.entry_Valor.config(width=30)
        self.entry_Valor.grid(row=6, column=5)                

        self.label_co_Nombre = tk.Label(self, text= "Nombre: ")
        self.label_co_Nombre.config(font=('Times New Roman',12,"bold"))
        self.label_co_Nombre.grid(row=1, column=3)
        self.mi_co_Nombre = tk.StringVar()
        self.entry_co_Nombre = tk.Entry(self, textvariable=self.mi_co_Nombre)
        self.entry_co_Nombre.config(width=50)
        self.entry_co_Nombre.grid(row=1, column=4, columnspan=2, padx=10)
        
        self.label_co_Apellido = tk.Label(self, text= "Apellidos: ")
        self.label_co_Apellido.config(font=('Times New Roman',12,"bold"))
        self.label_co_Apellido.grid(row=2, column=3)
        self.mi_co_Apellido = tk.StringVar()
        self.entry_co_Apellido = tk.Entry(self, textvariable=self.mi_co_Apellido)
        self.entry_co_Apellido.config(width=50)
        self.entry_co_Apellido.grid(row=2, column=4, columnspan=2, padx=10)

        self.label_co_Cedula = tk.Label(self, text= "Cedula: ")
        self.label_co_Cedula.config(font=('Times New Roman',12,"bold"))
        self.label_co_Cedula.grid(row=3, column=3)
        self.mi_co_Cedula = tk.StringVar()
        self.entry_co_Cedula = tk.Entry(self, textvariable=self.mi_co_Cedula)
        self.entry_co_Cedula.config(width=50)
        self.entry_co_Cedula.grid(row=3, column=4, columnspan=2, padx=10)

        self.label_co_Telefono = tk.Label(self, text= "Telefono: ")
        self.label_co_Telefono.config(font=('Times New Roman',12,"bold"))
        self.label_co_Telefono.grid(row=4, column=3)
        self.mi_co_Telefono = tk.StringVar()
        self.entry_co_Telefono = tk.Entry(self, textvariable=self.mi_co_Telefono)
        self.entry_co_Telefono.config(width=50)
        self.entry_co_Telefono.grid(row=4, column=4, columnspan=2, padx=10)

        self.label_co_Correo = tk.Label(self, text= "Correo: ")
        self.label_co_Correo.config(font=('Times New Roman',12,"bold"))
        self.label_co_Correo.grid(row=5, column=3)
        self.mi_co_Correo = tk.StringVar()
        self.entry_co_Correo = tk.Entry(self, textvariable=self.mi_co_Correo)
        self.entry_co_Correo.config(width=50)
        self.entry_co_Correo.grid(row=5, column=4, columnspan=2, padx=10)         

        self.mi_Id_apartamento = tk.StringVar()
        self.entry_Id_apartamento = tk.Entry(self, textvariable=self.mi_Id_apartamento)
        self.entry_Id_apartamento.config(width=1)
        self.entry_Id_apartamento.grid(row=1, column=7)

        #CREACION DE LOS BOTONES
        self.boton_Nuevo = tk.Button(self, text='Nuevo', command= self.habilitar_campos)
        self.boton_Nuevo.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#158645',
                                                cursor='hand2', activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=7,column=1, padx=10,pady=10)

        self.boton_Guardar = tk.Button(self, text = 'Guardar',command = self.guardar_datos)
        self.boton_Guardar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='blue',
                                                cursor='hand2', activebackground='blue')
        self.boton_Guardar.grid(row=7,column=2, padx=10,pady=10)        

        self.boton_Cancelar = tk.Button(self, text='Cancelar', command= self.desabilitar_campos)
        self.boton_Cancelar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#BD152E',
                                                cursor='hand2', activebackground='#E15370')
        self.boton_Cancelar.grid(row=7,column=3, padx=10,pady=10)

    def habilitar_campos(self):
        #self.ID_INQUILINO=None
        self.entry_Nombre.config(state='normal')
        self.entry_Apellidos.config(state='normal')
        self.entry_Cedula.config(state='normal')
        self.entry_Telefono.config(state='normal')
        self.entry_Correo.config(state='normal')
        self.entry_co_Nombre.config(state='normal')
        self.entry_co_Apellido.config(state='normal')
        self.entry_co_Cedula.config(state='normal')
        self.entry_co_Telefono.config(state='normal')
        self.entry_co_Correo.config(state='normal')
        self.entry_Id_apartamento.config(state='normal')
        self.entry_Direccion.config(state='normal')
        self.entry_Apartamento.config(state='normal')
        self.entry_Valor.config(state='normal')                        

        
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')

    def desabilitar_campos(self):
        self.ID_INQUILINO=None
        self.mi_Nombre.set('')
        self.mi_Apellidos.set('')
        self.mi_Cedula.set('')
        self.mi_Telefono.set('')
        self.mi_Correo.set('')
        self.mi_co_Nombre.set('')
        self.mi_co_Apellido.set('')
        self.mi_co_Cedula.set('')
        self.mi_co_Telefono.set('')
        self.mi_co_Correo.set('')
        self.mi_Id_apartamento.set('')
        self.mi_Direccion.set('')
        self.mi_Apartamento.set('')
        self.mi_Valor.set('')

        self.entry_Nombre.config(state='disabled')
        self.entry_Apellidos.config(state='disabled')
        self.entry_Cedula.config(state='disabled')
        self.entry_Telefono.config(state='disabled')
        self.entry_Correo.config(state='disabled')
        self.entry_co_Nombre.config(state='disabled')
        self.entry_co_Apellido.config(state='disabled')
        self.entry_co_Cedula.config(state='disabled')
        self.entry_co_Telefono.config(state='disabled')
        self.entry_co_Correo.config(state='disabled')
        self.entry_Id_apartamento.config(state='disabled')
        self.entry_Direccion.config(state='disabled')
        self.entry_Apartamento.config(state='disabled')
        self.entry_Valor.config(state='disabled')

        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')

    def guardar_datos(self):
        inquilino = Inquilino(
            self.mi_Nombre.get(),
            self.mi_Apellidos.get(),
            self.mi_Cedula.get(),
            self.mi_Telefono.get(),
            self.mi_Correo.get(),
            self.mi_co_Nombre.get(),
            self.mi_co_Apellido.get(),
            self.mi_co_Cedula.get(),
            self.mi_co_Telefono.get(),
            self.mi_co_Correo.get(),
            self.mi_Id_apartamento.get(),
            self.mi_Direccion.get(),
            self.mi_Apartamento.get(),
            self.mi_Valor.get()
        )
        if self.ID_INQUILINO == None:
            guardar(inquilino)
        else:
            editar(inquilino, self.ID_INQUILINO)    

        self.tabla_inquilino()
        self.desabilitar_campos()

    def tabla_inquilino(self):
        self.lista_inquilinos = listar_inquilino()
        self.lista_inquilinos.reverse()

        self.tabla = ttk.Treeview(self, 
        column = ('NOMBRE', 'APELLIDOS', 'CEDULA','TELEFONO','CORREO', 'CO_NOMBRE', 'CO_APELLIDOS', 'CO_CEDULA','CO_TELEFONO','CO_CORREO','ID_APARTAMENTO', 'DIRECCION','APARTAMENTO','VALOR'))
        self.tabla.grid(row=9, column=0, columnspan=10, sticky='nse')
        
        self.tabla.column('#0', width=35)
        self.tabla.column('NOMBRE', width=100)
        self.tabla.column('APELLIDOS', width=100)
        self.tabla.column('CEDULA', width=100)
        self.tabla.column('TELEFONO', width=100)
        self.tabla.column('CORREO', width=110)
        self.tabla.column('CO_NOMBRE', width=100)
        self.tabla.column('CO_APELLIDOS', width=100)
        self.tabla.column('CO_CEDULA', width=100)
        self.tabla.column('CO_TELEFONO', width=100)
        self.tabla.column('CO_CORREO', width=110)
        self.tabla.column('ID_APARTAMENTO', width=35)
        self.tabla.column('DIRECCION', width=100)
        self.tabla.column('APARTAMENTO', width=100)
        self.tabla.column('VALOR', width=100)

        #Scrollbar
        self.scroll=ttk.Scrollbar(self,
        orient='vertical', command= self.tabla.yview)
        self.scroll.grid(row=9, column=9, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)
        
        #encabezados
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='APELLIDOS')
        self.tabla.heading('#3', text='CEDULA')
        self.tabla.heading('#4', text='TELEFONO')
        self.tabla.heading('#5', text='CORREO')
        self.tabla.heading('#6', text='CO_NOMBRE')
        self.tabla.heading('#7', text='CO_APELLIDOS')
        self.tabla.heading('#8', text='CO_CEDULA')
        self.tabla.heading('#9', text='CO_TELEFONO')
        self.tabla.heading('#10', text='CO_CORREO')
        self.tabla.heading('#11', text='ID_APARTAMENTO')
        self.tabla.heading('#12', text='DIRECCION')
        self.tabla.heading('#13', text='APARTAMENTO')
        self.tabla.heading('#14', text='VALOR')

        #iterar la lista de peliculas
        for a in self.lista_inquilinos:
            self.tabla.insert('',0,text=a[0],
            values=(a[1],a[2],a[3],a[4],a[5], a[6],a[7],a[8],a[9], a[10], a[11], a[12], a[13], a[14]))

        #CREACION DE LOS BOTONES
        self.boton_Editar = tk.Button(self, text='Editar', command=self.editar_datos)
        self.boton_Editar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#158645',
                                                cursor='hand2', activebackground='#35BD6F')
        self.boton_Editar.grid(row=15,column=0, padx=10,pady=10)

        self.boton_Eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.boton_Eliminar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#BD152E',
                                                cursor='hand2', activebackground='#E15370')
        self.boton_Eliminar.grid(row=15,column=1, padx=10,pady=10)

        self.boton_ir_apartamentos = tk.Button(self, text='Menu Principal', command=self.Menu_principal)
        self.boton_ir_apartamentos.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='blue',
                                                cursor='hand2', activebackground='blue')
        self.boton_ir_apartamentos.grid(row=15,column=5, padx=10,pady=10)        

    def Menu_principal(self):
        self.destroy()
    
    def editar_datos(self):
        
        try:
            self.ID_INQUILINO = self.tabla.item(self.tabla.selection())['text']
            self.nombre_inquilino = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellidos_inquilino = self.tabla.item(self.tabla.selection())['values'][1]
            self.cedula_inquilino = self.tabla.item(self.tabla.selection())['values'][2]
            self.telefono_inquilino = self.tabla.item(self.tabla.selection())['values'][3]
            self.correo_inquilino = self.tabla.item(self.tabla.selection())['values'][4]
            self.co_nombre_inquilino = self.tabla.item(self.tabla.selection())['values'][5]
            self.co_apellido_inquilino = self.tabla.item(self.tabla.selection())['values'][6]
            self.co_cedula_inquilino = self.tabla.item(self.tabla.selection())['values'][7]
            self.co_telefono_inquilino = self.tabla.item(self.tabla.selection())['values'][8]
            self.co_correo_inquilino = self.tabla.item(self.tabla.selection())['values'][9]
            self.id_apartamento = self.tabla.item(self.tabla.selection())['values'][10]
            self.direccion_apartamento = self.tabla.item(self.tabla.selection())['values'][11]
            self.apartamento_apartamento = self.tabla.item(self.tabla.selection())['values'][12]
            self.valor_apartamento = self.tabla.item(self.tabla.selection())['values'][13]


            self.habilitar_campos()
            self.entry_Nombre.insert(0, self.nombre_inquilino)
            self.entry_Apellidos.insert(0,self.apellidos_inquilino)
            self.entry_Cedula.insert(0,self.cedula_inquilino)
            self.entry_Telefono.insert(0,self.telefono_inquilino)
            self.entry_Correo.insert(0,self.correo_inquilino)
            self.entry_co_Nombre.insert(0, self.co_nombre_inquilino)
            self.entry_co_Apellido.insert(0,self.co_apellido_inquilino)
            self.entry_co_Cedula.insert(0,self.co_cedula_inquilino)
            self.entry_co_Telefono.insert(0,self.co_telefono_inquilino)
            self.entry_co_Correo.insert(0,self.co_correo_inquilino)
            self.entry_Id_apartamento.insert(0, self.id_apartamento)
            self.entry_Direccion.insert(0,self.direccion_apartamento)
            self.entry_Apartamento.insert(0,self.apartamento_apartamento)
            self.entry_Valor.insert(0,self.valor_apartamento)
            
        
        except:
            titulo = 'Editar un registro'
            mensaje= 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)       
        
    def eliminar_datos(self):
        
        try:
            self.ID_INQUILINO = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.ID_INQUILINO)
            self.tabla_inquilino()
            self.ID_INQUILINO = None

        except:
           titulo = 'Eliminar un registro'
           mensaje= 'No ha seleccionado ningun registro'
           messagebox.showerror(titulo, mensaje)  

    def tabla_datos_apartamentos(self):
        self.lista_apartamentos = listar_apartamento()
        self.lista_apartamentos.reverse()

        self.tabla2 = ttk.Treeview(self, height=5, 
        column = ('Direccion', 'Numero_Apartamento'))
        self.tabla2.grid(row=26, column=0, columnspan=4, sticky='nse')

        self.tabla2.column('#0', width=35)

        self.scroll=ttk.Scrollbar(self,
        orient='vertical', command= self.tabla2.yview)
        self.scroll.grid(row=26, column=3, sticky='nse')
        self.tabla2.configure(yscrollcommand=self.scroll.set)

        self.tabla2.heading('#0', text='ID')
        self.tabla2.heading('#1', text='DIRECCION')
        self.tabla2.heading('#2', text='APARTAMENTO')
                
        #iterar la lista de peliculas
        for a in self.lista_apartamentos:
            self.tabla2.insert('',0,text=a[0],
            values=(a[1],a[2]))

        #CREACION DE LOS BOTONES
        self.boton_Editar = tk.Button(self, text='Seleccionar', command=self.seleccionar_apartamento)
        self.boton_Editar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#158645',
                                                cursor='hand2', activebackground='#35BD6F')
        self.boton_Editar.grid(row=28,column=1, padx=10,pady=10)    

    def seleccionar_apartamento(self):
        try:
            self.id_apartamento = self.tabla2.item(self.tabla2.selection())['text']
            self.direccion_apartamento = self.tabla2.item(self.tabla2.selection())['values'][0]
            self.apartamento_apartamento = self.tabla2.item(self.tabla2.selection())['values'][1]
                    
            self.habilitar_campos()
            self.entry_Id_apartamento.insert(0, self.id_apartamento)
            self.entry_Direccion.insert(0, self.direccion_apartamento)
            self.entry_Apartamento.insert(0,self.apartamento_apartamento)
            
        except:
            titulo = 'Editar un registro'
            mensaje= 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)       
                         

