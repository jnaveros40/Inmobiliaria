from sre_parse import State
import tkinter as tk
from tkinter import LEFT, ttk
from tkinter import messagebox
#from tkcalendar import DateEntry
from model.facturacion_dao import crear_tabla_facturacion, borrar_tabla_facturacion, editar, guardar, Facturacion, listar_facturacion, eliminar 
from model.inquilino_dao import listar_inquilino
from model.apartamento_dao import listar_apartamento

def barra_menu_facturacion(root):
    barra_menu = tk.Menu(root)
       
    root.config(menu = barra_menu, width=300, height = 300)
    
    menu_apartamento = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'Apartamentos', menu=menu_apartamento)
    menu_apartamento.add_command(label='Crear base de datos', command=crear_tabla_facturacion)
    menu_apartamento.add_command(label='Eliminar base de datos', command= borrar_tabla_facturacion)
    
    barra_menu.add_command(label='Salir', command=root.destroy)

class Frame_facturacion (tk.Frame):
    def __init__ (self, root = None):
        super().__init__(root,width=650, height=1020)
        self.root = root

        self.pack()
        
        self.ID_FACTURACION = None

        self.campos_agregar_facturacion()
        self.desabilitar_campos()
        self.tabla_facturacion()
        self.tabla_datos_inquilino()
        #self.tabla_datos_apartamentos()

    def campos_agregar_facturacion(self):
        self.borrar_espacios = tk.StringVar()
        
        #agregar los label

        self.label_Recibido_de = tk.Label(self, text = "    RECIBO DE ALQUILER")
        self.label_Recibido_de.config(font=('Times New Roman',20,"bold"))
        self.label_Recibido_de.grid(row=0,column=0, columnspan=2)

        self.label_Recibido_de = tk.Label(self, text = " Recibido de: ")
        self.label_Recibido_de.config(font=('Times New Roman',12,"bold"))
        self.label_Recibido_de.grid(row=1,column=0)

        self.label_Nombre_de = tk.Label(self, text = " Nombre: ")
        self.label_Nombre_de.config(font=('Times New Roman',12,"bold"))
        self.label_Nombre_de.grid(row=2,column=0)
        self.mi_Nombre_de = tk.StringVar()
        self.entry_Nombre_de = tk.Entry(self, textvariable=self.mi_Nombre_de)
        self.entry_Nombre_de.config(width=60) #, state='disable' #para desabilitar
        self.entry_Nombre_de.grid(row=2, column=1, columnspan=2) #, columnspan=2

        self.label_Apellido_de = tk.Label(self, text = " Apellido: ")
        self.label_Apellido_de.config(font=('Times New Roman',12,"bold"))
        self.label_Apellido_de.grid(row=3,column=0)
        self.mi_Apellido_de = tk.StringVar()
        self.entry_Apellido_de = tk.Entry(self, textvariable=self.mi_Apellido_de)
        self.entry_Apellido_de.config(width=60)
        self.entry_Apellido_de.grid(row=3, column=1, columnspan=2)

        self.label_vacio2 = tk.Label(self, text = "")
        self.label_vacio2.config(font=('Times New Roman',3))
        self.label_vacio2.grid(row=4,column=0)        

        self.label_Direccion = tk.Label(self, text = " Direccion: ")
        self.label_Direccion.config(font=('Times New Roman',12,"bold"))
        self.label_Direccion.grid(row=5,column=0)
        self.mi_Direccion = tk.StringVar()
        self.entry_Direccion = tk.Entry(self, textvariable=self.mi_Direccion)
        self.entry_Direccion.config(width=60)
        self.entry_Direccion.grid(row=5, column=1, columnspan=2)

        self.label_Numero_apartamento = tk.Label(self, text = " Apartamento: ")
        self.label_Numero_apartamento.config(font=('Times New Roman',12,"bold"))
        self.label_Numero_apartamento.grid(row=6,column=0)
        self.mi_Numero_apartamento = tk.StringVar()
        self.entry_Numero_apartamento = tk.Entry(self, textvariable=self.mi_Numero_apartamento)
        self.entry_Numero_apartamento.config(width=20)
        self.entry_Numero_apartamento.grid(row=6, column=1)        

        self.label_Direccion = tk.Label(self, text = "")
        self.label_Direccion.config(font=('Times New Roman',3))
        self.label_Direccion.grid(row=7,column=0) 

        self.label_Recibido_por = tk.Label(self, text = " Recibido por: ")
        self.label_Recibido_por.config(font=('Times New Roman',12,"bold"))
        self.label_Recibido_por.grid(row=8,column=0)

        self.label_Nombre_por = tk.Label(self, text = " Nombre: ")
        self.label_Nombre_por.config(font=('Times New Roman',12,"bold"))
        self.label_Nombre_por.grid(row=9,column=0)
        self.mi_Nombre_por = tk.StringVar()
        self.entry_Nombre_por = tk.Entry(self, textvariable=self.mi_Nombre_por)
        self.entry_Nombre_por.config(width=60) #, state='disable' #para desabilitar
        self.entry_Nombre_por.grid(row=9, column=1, columnspan=2) #, columnspan=2

        self.label_Apellido_por = tk.Label(self, text = " Apellido: ")
        self.label_Apellido_por.config(font=('Times New Roman',12,"bold"))
        self.label_Apellido_por.grid(row=10,column=0)
        self.mi_Apellido_por = tk.StringVar()
        self.entry_Apellido_por = tk.Entry(self, textvariable=self.mi_Apellido_por)
        self.entry_Apellido_por.config(width=60)
        self.entry_Apellido_por.grid(row=10, column=1, columnspan=2)

        self.label_vacio = tk.Label(self, text = "")
        self.label_vacio.config(font=('Times New Roman',3))
        self.label_vacio.grid(row=11,column=0)                

        self.label_Fecha_actual = tk.Label(self, text = "    Fecha: ")
        self.label_Fecha_actual.config(font=('Times New Roman',15,"bold"))
        self.label_Fecha_actual.grid(row=0,column=3)
        self.mi_Fecha_actual = tk.StringVar()
        self.entry_Fecha_actual = tk.Entry(self, textvariable=self.mi_Fecha_actual)
        self.entry_Fecha_actual.config(width=15)
        self.entry_Fecha_actual.grid(row=0, column=4)
        
        self.label_Periodo = tk.Label(self, text = " Periodo (dd/mm/aaaa)")
        self.label_Periodo.config(font=('Times New Roman',12,"bold"))
        self.label_Periodo.grid(row=1,column=3, columnspan=2)

        self.label_Fecha_inicio = tk.Label(self, text = " Fecha inicio: ")
        self.label_Fecha_inicio.config(font=('Times New Roman',12,"bold"))
        self.label_Fecha_inicio.grid(row=2,column=3)
        self.mi_Fecha_inicio = tk.StringVar()
        self.entry_Fecha_inicio = tk.Entry(self, textvariable=self.mi_Fecha_inicio)
        self.entry_Fecha_inicio.config(width=20)
        self.entry_Fecha_inicio.grid(row=2, column=4)

        self.label_Fecha_final = tk.Label(self, text = " Fecha final: ")
        self.label_Fecha_final.config(font=('Times New Roman',12,"bold"))
        self.label_Fecha_final.grid(row=3,column=3)
        self.mi_Fecha_final = tk.StringVar()
        self.entry_Fecha_final = tk.Entry(self, textvariable=self.mi_Fecha_final)
        self.entry_Fecha_final.config(width=20)
        self.entry_Fecha_final.grid(row=3, column=4)

        self.label_Valor = tk.Label(self, text = " Valor")
        self.label_Valor.config(font=('Times New Roman',20,"bold"))
        self.label_Valor.grid(row=6,column=3, columnspan=2, rowspan=2)
        self.label_Valor = tk.Label(self, text = "    COP  $")
        self.label_Valor.config(font=('Times New Roman',18,"bold"))
        self.label_Valor.grid(row=7,column=3, rowspan=3)        
        self.mi_Valor = tk.StringVar()
        self.entry_Valor = tk.Entry(self, textvariable=self.mi_Valor)
        self.entry_Valor.config(width=8,font=('Times New Roman',18,"bold"))
        self.entry_Valor.grid(row=7, column=4, padx=10, rowspan=3)

        self.mi_Id_inquilino = tk.StringVar()
        self.entry_Id_inquilino = tk.Entry(self, textvariable=self.mi_Id_inquilino)
        self.entry_Id_inquilino.config (width=1)
        self.entry_Id_inquilino.grid(row=0, column=7)

        self.mi_Id_apartamento = tk.StringVar()
        self.entry_Id_apartamento = tk.Entry(self, textvariable=self.mi_Id_apartamento)
        self.entry_Id_apartamento.config(width=1)
        self.entry_Id_apartamento.grid(row=1, column=7)                

        #CREACION DE LOS BOTONES
        self.boton_Nuevo = tk.Button(self, text='Nuevo', command= self.habilitar_campos)
        self.boton_Nuevo.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#158645',
                                                cursor='hand2', activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=2,column=5,rowspan=2, padx=10,pady=10)

        self.boton_Guardar = tk.Button(self, text = 'Guardar',command = self.guardar_datos)
        self.boton_Guardar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='blue',
                                                cursor='hand2', activebackground='blue')
        self.boton_Guardar.grid(row=4,column=5, rowspan=2, padx=10,pady=10)        

        self.boton_Cancelar = tk.Button(self, text='Cancelar', command= self.desabilitar_campos)
        self.boton_Cancelar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#BD152E',
                                                cursor='hand2', activebackground='#E15370')
        self.boton_Cancelar.grid(row=6,column=5,rowspan=2, padx=10,pady=10)

    def habilitar_campos(self):
        #self.id_apartamento=None
        self.entry_Id_inquilino.config(state='normal')
        self.entry_Nombre_de.config(state='normal')
        self.entry_Apellido_de.config(state='normal')
        self.entry_Id_apartamento.config(state='normal')
        self.entry_Direccion.config(state='normal')
        self.entry_Numero_apartamento.config(state='normal')
        self.entry_Nombre_por.config(state='normal')
        self.entry_Apellido_por.config(state='normal')
        self.entry_Fecha_actual.config(state='normal')
        self.entry_Fecha_inicio.config(state='normal')
        self.entry_Fecha_final.config(state='normal')
        self.entry_Valor.config(state='normal')

        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')

    def desabilitar_campos(self):
        self.ID_FACTURACION=None
        self.mi_Id_inquilino.set('')
        self.mi_Nombre_de.set('')
        self.mi_Apellido_de.set('')
        self.mi_Id_apartamento.set('')
        self.mi_Direccion.set('')
        self.mi_Numero_apartamento.set('')
        self.mi_Nombre_por.set('')
        self.mi_Apellido_por.set('')
        self.mi_Fecha_actual.set('')
        self.mi_Fecha_inicio.set('')
        self.mi_Fecha_final.set('')
        self.mi_Valor.set('')
         
        self.entry_Id_inquilino.config(state='disabled')
        self.entry_Nombre_de.config(state='disabled')
        self.entry_Apellido_de.config(state='disabled')
        self.entry_Id_apartamento.config(state='disabled')
        self.entry_Direccion.config(state='disabled')
        self.entry_Numero_apartamento.config(state='disabled')
        self.entry_Nombre_por.config(state='disabled')
        self.entry_Apellido_por.config(state='disabled')
        self.entry_Fecha_actual.config(state='disabled')
        self.entry_Fecha_inicio.config(state='disabled')
        self.entry_Fecha_final.config(state='disabled')
        self.entry_Valor.config(state='disabled')

        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')

    def guardar_datos(self):
        facturacion = Facturacion(
            self.mi_Id_inquilino.get(),
            self.mi_Nombre_de.get(),
            self.mi_Apellido_de.get(),
            self.mi_Id_apartamento.get(),
            self.mi_Direccion.get(),
            self.mi_Numero_apartamento.get(),
            self.mi_Nombre_por.get(),
            self.mi_Apellido_por.get(),
            self.mi_Fecha_actual.get(),
            self.mi_Fecha_inicio.get(),
            self.mi_Fecha_final.get(),
            self.mi_Valor.get()
        )
        if self.ID_FACTURACION == None:
            guardar(facturacion)
        else:
            editar(facturacion, self.ID_FACTURACION)    

        self.tabla_facturacion()
        self.desabilitar_campos()

    def tabla_facturacion(self):
        self.lista_facturacion = listar_facturacion()
        self.lista_facturacion.reverse()

        self.tabla = ttk.Treeview(self, height=5,
        column = ('ID_INQUILINO','NOMBRE_INQUILINO', 'APELLIDO_INQUILINO','ID_APARTAMENTO', 'DIRECCION', 'APARTAMENTO', 'NOMBRE_PROPIETARIO', 'APELLIDO_PROPIETARIO', 'FECHA', 'FECHA_INICIO', 'FECHA_FINAL', 'VALOR'))
        
        self.tabla.grid(row=12, column=0, columnspan=7, sticky='nse')
        self.tabla.column('#0', width=35)
        self.tabla.column('ID_INQUILINO', width=25)
        self.tabla.column('NOMBRE_INQUILINO',width=120)
        self.tabla.column('APELLIDO_INQUILINO',width=120)
        self.tabla.column('ID_APARTAMENTO', width=25)
        self.tabla.column('DIRECCION',width=120)
        self.tabla.column('APARTAMENTO',width=80)
        self.tabla.column('NOMBRE_PROPIETARIO',width=120)
        self.tabla.column('APELLIDO_PROPIETARIO',width=120)
        self.tabla.column('FECHA',width=120)
        self.tabla.column('FECHA_INICIO',width=120)
        self.tabla.column('FECHA_FINAL',width=120)
        self.tabla.column('VALOR',width=120)
        
        self.scroll=ttk.Scrollbar(self,
        orient='vertical', command= self.tabla.yview)
        self.scroll.grid(row=12, column=7, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='ID INQUILINO')
        self.tabla.heading('#2', text='NOMBRE INQUILINO')
        self.tabla.heading('#3', text='APELLIDO INQUILINO')
        self.tabla.heading('#4', text='ID APARTAMENTO')
        self.tabla.heading('#5', text='DIRECCION')
        self.tabla.heading('#6', text='APARTAMENTO')
        self.tabla.heading('#7', text='NOMBRE PROPIETARIO')
        self.tabla.heading('#8', text='APELLIDO PROPIETARIO')
        self.tabla.heading('#9', text='FECHA')
        self.tabla.heading('#10', text='FECHA INICIO')
        self.tabla.heading('#11', text='FECHA FINAL')
        self.tabla.heading('#12', text='VALOR')
        
        #iterar la lista de facturacion
        for a in self.lista_facturacion:
            self.tabla.insert('',0,text=a[0],
            values=(a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12]))

        #CREACION DE LOS BOTONES
        self.boton_Editar = tk.Button(self, text='Editar', command=self.editar_datos)
        self.boton_Editar.config(width=13, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#158645',
                                                cursor='hand2', activebackground='#35BD6F')
        self.boton_Editar.grid(row=20,column=0, padx=10,pady=10)

        self.boton_Eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.boton_Eliminar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#BD152E',
                                                cursor='hand2', activebackground='#E15370')
        self.boton_Eliminar.grid(row=20,column=1, padx=10,pady=10) 

        self.boton_ir_apartamentos = tk.Button(self, text='Menu Principal', command=self.Menu_principal)
        self.boton_ir_apartamentos.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='blue',
                                                cursor='hand2', activebackground='blue')
        self.boton_ir_apartamentos.grid(row=20,column=3, padx=10,pady=10)        

    def Menu_principal(self):
        self.destroy()       

    def editar_datos(self):
        try:
            self.ID_FACTURACION = self.tabla.item(self.tabla.selection())['text']
            self.id_inquilino = self.tabla.item(self.tabla.selection())['values'][0]
            self.nombre_de_facturacion = self.tabla.item(self.tabla.selection())['values'][1]
            self.apellido_de_facturacion = self.tabla.item(self.tabla.selection())['values'][2]
            self.id_apartamento = self.tabla.item(self.tabla.selection())['values'][3]
            self.direccion_facturacion = self.tabla.item(self.tabla.selection())['values'][4]
            self.numero_apartamento_facturacion = self.tabla.item(self.tabla.selection())['values'][5]
            self.nombre_por_facturacion = self.tabla.item(self.tabla.selection())['values'][6]
            self.apellido_por_facturacion = self.tabla.item(self.tabla.selection())['values'][7]
            self.fecha_actual_facturacion = self.tabla.item(self.tabla.selection())['values'][8]
            self.fecha_inicio_facturacion = self.tabla.item(self.tabla.selection())['values'][9]
            self.fecha_final_facturacion = self.tabla.item(self.tabla.selection())['values'][10]
            self.valor_facturacion = self.tabla.item(self.tabla.selection())['values'][11]

            self.habilitar_campos()
            self.entry_Id_inquilino.insert(0, self.id_inquilino)
            self.entry_Nombre_de.insert(0, self.nombre_de_facturacion)
            self.entry_Apellido_de.insert(0, self.apellido_de_facturacion)
            self.entry_Id_apartamento.insert(0, self.id_apartamento)
            self.entry_Direccion.insert(0, self.direccion_facturacion)
            self.entry_Numero_apartamento.insert(0, self.numero_apartamento_facturacion)
            self.entry_Nombre_por.insert(0, self.nombre_por_facturacion)
            self.entry_Apellido_por.insert(0, self.apellido_por_facturacion)
            self.entry_Fecha_actual.insert(0, self.fecha_actual_facturacion)
            self.entry_Fecha_inicio.insert(0, self.fecha_inicio_facturacion)
            self.entry_Fecha_final.insert(0, self.fecha_final_facturacion)
            self.entry_Valor.insert(0, self.valor_facturacion)
                 
        except:
            titulo = 'Editar un registro'
            mensaje= 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)       

    def eliminar_datos(self):
        
        try:
            self.ID_FACTURACION = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.ID_FACTURACION)
            self.tabla_facturacion()
            self.ID_FACTURACION = None

        except:
           titulo = 'Eliminar un registro'
           mensaje= 'No ha seleccionado ningun registro'
           messagebox.showerror(titulo, mensaje)    

    def tabla_datos_inquilino(self):
        self.lista_inquilinos = listar_inquilino()
        self.lista_inquilinos.reverse()

        self.tabla1 = ttk.Treeview(self, height=5,
        column = ('NOMBRE', 'APELLIDOS','CEDULA','ID_APARTAMENTO','DIRECCION','APARTAMENTO','VALOR'))
        self.tabla1.grid(row=26, column=1, columnspan=3, sticky='nse')
        
        self.tabla1.column('#0', width=35)
        self.tabla1.column('NOMBRE', width=120)
        self.tabla1.column('APELLIDOS', width=120)
        self.tabla1.column('CEDULA', width=120)
        self.tabla1.column('ID_APARTAMENTO', width=35)
        self.tabla1.column('DIRECCION', width=120)
        self.tabla1.column('APARTAMENTO', width=120)
        self.tabla1.column('VALOR', width=120)

        #Scrollbar
        self.scroll=ttk.Scrollbar(self,
        orient='vertical', command= self.tabla1.yview)
        self.scroll.grid(row=26, column=3, sticky='nse')
        self.tabla1.configure(yscrollcommand=self.scroll.set)
        
        #encabezados
        self.tabla1.heading('#0', text='ID')
        self.tabla1.heading('#1', text='NOMBRE')
        self.tabla1.heading('#2', text='APELLIDOS')
        self.tabla1.heading('#3', text='CEDULA')
        self.tabla1.heading('#4', text= 'ID_APARTAMENTO')
        self.tabla1.heading('#5', text='DIRECCION')
        self.tabla1.heading('#6', text='APARTAMENTO')
        self.tabla1.heading('#7', text='VALOR')
        
        #iterar la lista de peliculas
        for a in self.lista_inquilinos:
            self.tabla1.insert('',0,text=a[0],
            values=(a[1],a[2],a[3],a[11], a[12], a[13], a[14]))

        #CREACION DE LOS BOTONES
        self.boton_Editar = tk.Button(self, text='Seleccionar', command=self.seleccionar_inquilino)
        self.boton_Editar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#158645',
                                                cursor='hand2', activebackground='#35BD6F')
        self.boton_Editar.grid(row=28,column=1, padx=10,pady=10)

    def seleccionar_inquilino(self):
        try:
            self.id_inquilino = self.tabla1.item(self.tabla1.selection())['text']
            self.nombre_inquilino = self.tabla1.item(self.tabla1.selection())['values'][0]
            self.apellidos_inquilino = self.tabla1.item(self.tabla1.selection())['values'][1]
            self.id_apartamento = self.tabla1.item(self.tabla1.selection())['values'][3]
            self.direccion_apartamento = self.tabla1.item(self.tabla1.selection())['values'][4]
            self.apartamento_apartamento = self.tabla1.item(self.tabla1.selection())['values'][5]
            self.valor = self.tabla1.item(self.tabla1.selection())['values'][6]
                            
            self.habilitar_campos()
            self.entry_Id_inquilino.insert(0, self.id_inquilino)
            self.entry_Nombre_de.insert(0, self.nombre_inquilino)
            self.entry_Apellido_de.insert(0,self.apellidos_inquilino)
            self.entry_Id_apartamento.insert(0, self.id_apartamento)
            self.entry_Direccion.insert(0, self.direccion_apartamento)
            self.entry_Numero_apartamento.insert(0, self.apartamento_apartamento)
            self.entry_Valor.insert(0, self.valor)
                
        except:
            titulo = 'Editar un registro'
            mensaje= 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)

    def tabla_datos_apartamentos(self):
        self.lista_apartamentos = listar_apartamento()
        self.lista_apartamentos.reverse()

        self.tabla2 = ttk.Treeview(self, height=5, 
        column = ('Direccion', 'Numero_Apartamento'))
        self.tabla2.grid(row=26, column=2, columnspan=4, sticky='nse')

        self.tabla2.column('#0', width=35)

        self.scroll=ttk.Scrollbar(self,
        orient='vertical', command= self.tabla2.yview)
        self.scroll.grid(row=26, column=6, sticky='nse')
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
        self.boton_Editar.grid(row=28,column=4, padx=10,pady=10)    

    def seleccionar_apartamento(self):
        try:
            self.id_apartamento = self.tabla2.item(self.tabla2.selection())['text']
            self.direccion_apartamento = self.tabla2.item(self.tabla2.selection())['values'][0]
            self.numero_apartamento_apartamento = self.tabla2.item(self.tabla2.selection())['values'][1]
                    
            self.habilitar_campos()
            self.entry_Id_apartamento.insert(0, self.id_apartamento)
            self.entry_Direccion.insert(0, self.direccion_apartamento)
            self.entry_Numero_apartamento.insert(0,self.numero_apartamento_apartamento)
            
        except:
            titulo = 'Editar un registro'
            mensaje= 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)       
            