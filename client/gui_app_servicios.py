from sre_parse import State
import tkinter as tk
from tkinter import LEFT, ttk
from tkinter import messagebox
#from tkcalendar import DateEntry
from model.servicios_dao import crear_tabla_servicios, borrar_tabla_servicios, editar, guardar, Servicios, listar_servicios, eliminar 
from model.inquilino_dao import listar_inquilino
from model.apartamento_dao import listar_apartamento

def barra_menu_servicios(root):
    barra_menu = tk.Menu(root)
       
    root.config(menu = barra_menu, width=300, height = 300)
    
    menu_apartamento = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'Servicios Publicos', menu=menu_apartamento)
    menu_apartamento.add_command(label='Crear base de datos', command=crear_tabla_servicios)
    menu_apartamento.add_command(label='Eliminar base de datos', command= borrar_tabla_servicios)
    
    barra_menu.add_command(label='Salir', command=root.destroy)

class Frame_servicios (tk.Frame):
    def __init__ (self, root = None):
        super().__init__(root,width=650, height=1020)
        self.root = root

        self.pack()
        
        self.ID_SERVICIO = None

        self.campos_agregar_servicio()
        self.desabilitar_campos()
        self.tabla_servicio()
        #self.tabla_datos_inquilino()
        self.tabla_datos_apartamentos()

    def campos_agregar_servicio(self):
        self.borrar_espacios = tk.StringVar()
        
        #agregar los label

        self.label_Recibido_de = tk.Label(self, text = "    GASTOS EN SERVICIOS PUBLICOS")
        self.label_Recibido_de.config(font=('Times New Roman',20,"bold"))
        self.label_Recibido_de.grid(row=0,column=0, columnspan=2)

        self.label_Tipo = tk.Label(self, text = " Tipo: ")
        self.label_Tipo.config(font=('Times New Roman',12,"bold"))
        self.label_Tipo.grid(row=2,column=0)
        self.mi_Tipo = tk.StringVar()
        self.entry_Tipo = tk.Entry(self, textvariable=self.mi_Tipo)
        self.entry_Tipo.config(width=60)
        self.entry_Tipo.grid(row=2, column=1, columnspan=2)

        self.label_Codigo = tk.Label(self, text = " Codigo: ")
        self.label_Codigo.config(font=('Times New Roman',12,"bold"))
        self.label_Codigo.grid(row=3,column=0)
        self.mi_Codigo = tk.StringVar()
        self.entry_Codigo = tk.Entry(self, textvariable=self.mi_Codigo)
        self.entry_Codigo.config(width=60)
        self.entry_Codigo.grid(row=3, column=1, columnspan=2)

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

        self.label_vacio = tk.Label(self, text = "")
        self.label_vacio.config(font=('Times New Roman',3))
        self.label_vacio.grid(row=7,column=0) 

        self.label_vacio = tk.Label(self, text = "")
        self.label_vacio.config(font=('Times New Roman',3))
        self.label_vacio.grid(row=11,column=0)                

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
        self.label_Valor.grid(row=4,column=3, columnspan=2, rowspan=2)
        self.label_Valor = tk.Label(self, text = "    COP  $")
        self.label_Valor.config(font=('Times New Roman',18,"bold"))
        self.label_Valor.grid(row=5,column=3, rowspan=3)        
        self.mi_Valor = tk.StringVar()
        self.entry_Valor = tk.Entry(self, textvariable=self.mi_Valor)
        self.entry_Valor.config(width=8,font=('Times New Roman',18,"bold"))
        self.entry_Valor.grid(row=5, column=4, padx=10, rowspan=3)

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
        self.entry_Tipo.config(state='normal')
        self.entry_Codigo.config(state='normal')
        self.entry_Id_apartamento.config(state='normal')
        self.entry_Direccion.config(state='normal')
        self.entry_Numero_apartamento.config(state='normal')
        self.entry_Fecha_inicio.config(state='normal')
        self.entry_Fecha_final.config(state='normal')
        self.entry_Valor.config(state='normal')

        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')

    def desabilitar_campos(self):
        self.ID_SERVICIO=None
        self.mi_Tipo.set('')
        self.mi_Codigo.set('')
        self.mi_Id_apartamento.set('')
        self.mi_Direccion.set('')
        self.mi_Numero_apartamento.set('')
        self.mi_Fecha_inicio.set('')
        self.mi_Fecha_final.set('')
        self.mi_Valor.set('')
         
        self.entry_Tipo.config(state='disabled')
        self.entry_Codigo.config(state='disabled')
        self.entry_Id_apartamento.config(state='disabled')
        self.entry_Direccion.config(state='disabled')
        self.entry_Numero_apartamento.config(state='disabled')
        self.entry_Fecha_inicio.config(state='disabled')
        self.entry_Fecha_final.config(state='disabled')
        self.entry_Valor.config(state='disabled')

        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')

    def guardar_datos(self):
        servicio = Servicios(
            self.mi_Tipo.get(),
            self.mi_Codigo.get(),
            self.mi_Id_apartamento.get(),
            self.mi_Direccion.get(),
            self.mi_Numero_apartamento.get(),
            self.mi_Fecha_inicio.get(),
            self.mi_Fecha_final.get(),
            self.mi_Valor.get()
        )
        if self.ID_SERVICIO == None:
            guardar(servicio)
        else:
            editar(servicio, self.ID_SERVICIO)    

        self.tabla_servicio()
        self.desabilitar_campos()

    def tabla_servicio(self):
        self.lista_servicio = listar_servicios()
        self.lista_servicio.reverse()

        self.tabla = ttk.Treeview(self, height=5,
        column = ('TIPO_SERVICIO','CODIGO_SERVICIO','ID_APARTAMENTO', 'DIRECCION', 'APARTAMENTO', 'FECHA_INICIO', 'FECHA_FINAL', 'VALOR_SERVICIO'))
        
        self.tabla.grid(row=12, column=0, columnspan=7, sticky='nse')
        self.tabla.column('#0', width=35)
        self.tabla.column('TIPO_SERVICIO')
        self.tabla.column('CODIGO_SERVICIO')
        self.tabla.column('ID_APARTAMENTO', width=35)
        self.tabla.column('DIRECCION')
        self.tabla.column('APARTAMENTO',width=120)
        self.tabla.column('FECHA_INICIO',width=120)
        self.tabla.column('FECHA_FINAL',width=120)
        self.tabla.column('VALOR_SERVICIO',width=120)
        
        self.scroll=ttk.Scrollbar(self,
        orient='vertical', command= self.tabla.yview)
        self.scroll.grid(row=12, column=7, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='TIPO_SERVICIO')
        self.tabla.heading('#2', text='CODIGO_SERVICIO')
        self.tabla.heading('#3', text='ID APARTAMENTO')
        self.tabla.heading('#4', text='DIRECCION')
        self.tabla.heading('#5', text='APARTAMENTO')
        self.tabla.heading('#6', text='FECHA INICIO')
        self.tabla.heading('#7', text='FECHA FINAL')
        self.tabla.heading('#8', text='VALOR_SERVICIO')
        
        #iterar la lista de facturacion
        for a in self.lista_servicio:
            self.tabla.insert('',0,text=a[0],
            values=(a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8]))

        #CREACION DE LOS BOTONES
        self.boton_Editar = tk.Button(self, text='Editar', command=self.editar_datos_servicios)
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

    def editar_datos_servicios(self):
        try:
            self.ID_SERVICIO = self.tabla.item(self.tabla.selection())['text']
            self.tipo_servicio = self.tabla.item(self.tabla.selection())['values'][0]
            self.codigo_servicio = self.tabla.item(self.tabla.selection())['values'][1]
            self.id_apartamento = self.tabla.item(self.tabla.selection())['values'][2]
            self.direccion_servicio = self.tabla.item(self.tabla.selection())['values'][3]
            self.numero_apartamento_servicio = self.tabla.item(self.tabla.selection())['values'][4]
            self.fecha_inicio_servicio = self.tabla.item(self.tabla.selection())['values'][5]
            self.fecha_final_servicio = self.tabla.item(self.tabla.selection())['values'][6]
            self.valor_servicio = self.tabla.item(self.tabla.selection())['values'][7]

            self.habilitar_campos()
            self.entry_Tipo.insert(0, self.tipo_servicio)
            self.entry_Codigo.insert(0, self.codigo_servicio)
            self.entry_Id_apartamento.insert(0, self.id_apartamento)
            self.entry_Direccion.insert(0, self.direccion_servicio)
            self.entry_Numero_apartamento.insert(0, self.numero_apartamento_servicio)
            self.entry_Fecha_inicio.insert(0, self.fecha_inicio_servicio)
            self.entry_Fecha_final.insert(0, self.fecha_final_servicio)
            self.entry_Valor.insert(0, self.valor_servicio)
               
        except:
            titulo = 'Editar un registro'
            mensaje= 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)       

    def eliminar_datos(self):
        
        try:
            self.ID_SERVICIO = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.ID_SERVICIO)
            self.tabla_servicio()
            self.ID_SERVICIO = None

        except:
           titulo = 'Eliminar un registro'
           mensaje= 'No ha seleccionado ningun registro'
           messagebox.showerror(titulo, mensaje)    

    def tabla_datos_inquilino(self):
        self.lista_inquilinos = listar_inquilino()
        self.lista_inquilinos.reverse()

        self.tabla1 = ttk.Treeview(self, height=5,
        column = ('ID_APARTAMENTO','DIRECCION','APARTAMENTO'))
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
            self.id_apartamento = self.tabla1.item(self.tabla1.selection())['values'][3]
            self.direccion_apartamento = self.tabla1.item(self.tabla1.selection())['values'][4]
            self.apartamento_apartamento = self.tabla1.item(self.tabla1.selection())['values'][5]
            self.valor = self.tabla1.item(self.tabla1.selection())['values'][6]
                            
            self.habilitar_campos()
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
            self.numero_apartamento_apartamento = self.tabla2.item(self.tabla2.selection())['values'][1]
                    
            self.habilitar_campos()
            self.entry_Id_apartamento.insert(0, self.id_apartamento)
            self.entry_Direccion.insert(0, self.direccion_apartamento)
            self.entry_Numero_apartamento.insert(0,self.numero_apartamento_apartamento)
            
        except:
            titulo = 'Editar un registro'
            mensaje= 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)       
            