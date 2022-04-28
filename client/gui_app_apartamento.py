from sre_parse import State
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model.apartamento_dao import crear_tabla_apartamento, borrar_tabla_apartamento, editar, guardar, Apartamento, eliminar, listar_apartamento 

def barra_menu_apartamento(root):
    barra_menu = tk.Menu(root)
       
    root.config(menu = barra_menu, width=300, height = 300)
    
    menu_apartamento = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'Apartamentos', menu=menu_apartamento)
    menu_apartamento.add_command(label='Crear base de datos', command=crear_tabla_apartamento)
    menu_apartamento.add_command(label='Eliminar base de datos', command= borrar_tabla_apartamento)
    
    barra_menu.add_command(label='Salir', command=root.destroy)

class Frame_apartamentos (tk.Frame):
    def __init__ (self, root = None):
        super().__init__(root,width=650, height=720)
        self.root = root
        self.pack()
        
        self.id_apartamento = None

        self.campos_agregar_apartamento()
        self.desabilitar_campos()
        self.tabla_apartamentos()

    def campos_agregar_apartamento(self):
        self.borrar_espacios = tk.StringVar()
        
        #agregar los label
        self.label_Direccion = tk.Label(self, text = "Direccion: ")
        self.label_Direccion.config(font=('Times New Roman',12,"bold"))
        self.label_Direccion.grid(row=0,column=0)
        self.mi_Direccion = tk.StringVar()
        self.entry_Direccion = tk.Entry(self, textvariable=self.mi_Direccion)
        self.entry_Direccion.config(width=60) #, state='disable' #para desabilitar
        self.entry_Direccion.grid(row=0, column=1, columnspan=2) #, columnspan=2

        self.label_Numero_Apartamento = tk.Label(self, text = "Numero de apartamento: ")
        self.label_Numero_Apartamento.config(font=('Times New Roman',12,"bold"))
        self.label_Numero_Apartamento.grid(row=1,column=0)
        self.mi_Numero_Apartamento = tk.StringVar()
        self.entry_Numero_Apartamento = tk.Entry(self, textvariable=self.mi_Numero_Apartamento)
        self.entry_Numero_Apartamento.config(width=60)
        self.entry_Numero_Apartamento.grid(row=1, column=1, columnspan=2)

        self.label_Matricula_inmobiliaria = tk.Label(self, text = "Matricula Inmobiliaria: ")
        self.label_Matricula_inmobiliaria.config(font=('Times New Roman',12,"bold"))
        self.label_Matricula_inmobiliaria.grid(row=2,column=0)
        self.mi_Matricula_inmobiliaria = tk.StringVar()
        self.entry_Matricula_inmobiliaria = tk.Entry(self, textvariable=self.mi_Matricula_inmobiliaria)
        self.entry_Matricula_inmobiliaria.config(width=60)
        self.entry_Matricula_inmobiliaria.grid(row=2, column=1, columnspan=2)

        self.label_Ficha_catastral = tk.Label(self, text = "Ficha Catastral: ")
        self.label_Ficha_catastral.config(font=('Times New Roman',12,"bold"))
        self.label_Ficha_catastral.grid(row=3,column=0)  
        self.mi_Ficha_catastral = tk.StringVar()
        self.entry_Ficha_catastral = tk.Entry(self, textvariable=self.mi_Ficha_catastral)
        self.entry_Ficha_catastral.config(width=60)
        self.entry_Ficha_catastral.grid(row=3, column=1, columnspan=2)             

        #CREACION DE LOS BOTONES
        self.boton_Nuevo = tk.Button(self, text='Nuevo', command= self.habilitar_campos)
        self.boton_Nuevo.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#158645',
                                                cursor='hand2', activebackground='#35BD6F')
        self.boton_Nuevo.grid(row=4,column=0, padx=10,pady=10)

        self.boton_Guardar = tk.Button(self, text = 'Guardar',command = self.guardar_datos)
        self.boton_Guardar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='blue',
                                                cursor='hand2', activebackground='blue')
        self.boton_Guardar.grid(row=4,column=1, padx=10,pady=10)        

        self.boton_Cancelar = tk.Button(self, text='Cancelar', command= self.desabilitar_campos)
        self.boton_Cancelar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#BD152E',
                                                cursor='hand2', activebackground='#E15370')
        self.boton_Cancelar.grid(row=4,column=2, padx=10,pady=10)

    def habilitar_campos(self):
        #self.id_apartamento=None
        self.entry_Direccion.config(state='normal')
        self.entry_Numero_Apartamento.config(state='normal')
        self.entry_Matricula_inmobiliaria.config(state='normal')
        self.entry_Ficha_catastral.config(state='normal')
        self.boton_Guardar.config(state='normal')
        self.boton_Cancelar.config(state='normal')

    def desabilitar_campos(self):
        self.id_apartamento=None
        self.mi_Direccion.set('')
        self.mi_Ficha_catastral.set('')
        self.mi_Matricula_inmobiliaria.set('')
        self.mi_Numero_Apartamento.set('')
        
        self.entry_Direccion.config(state='disabled')
        self.entry_Numero_Apartamento.config(state='disabled')
        self.entry_Matricula_inmobiliaria.config(state='disabled')
        self.entry_Ficha_catastral.config(state='disabled')
        self.boton_Guardar.config(state='disabled')
        self.boton_Cancelar.config(state='disabled')

    def guardar_datos(self):
        apartamento = Apartamento(
            self.mi_Direccion.get(),
            self.mi_Numero_Apartamento.get(),
            self.mi_Matricula_inmobiliaria.get(),
            self.mi_Ficha_catastral.get()
        )
        if self.id_apartamento == None:
            guardar(apartamento)
        else:
            editar(apartamento, self.id_apartamento)    

        self.tabla_apartamentos()
        self.desabilitar_campos()

    def tabla_apartamentos(self):
        self.lista_apartamentos = listar_apartamento()
        self.lista_apartamentos.reverse()

        self.tabla = ttk.Treeview(self, height=10,
        column = ('Direccion', 'Numero_Apartamento', 'Matricula_inmobiliaria','Ficha_Catastral'))
        self.tabla.grid(row=5, column=0, columnspan=4, sticky='nse')

        self.tabla.column('#0', width=35)

        self.scroll=ttk.Scrollbar(self,
        orient='vertical', command= self.tabla.yview)
        self.scroll.grid(row=5, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='DIRECCION')
        self.tabla.heading('#2', text='APARTAMENTO')
        self.tabla.heading('#3', text='MATRICULA INMOBILIARIA')
        self.tabla.heading('#4', text='FICHA CATASTRAL')

        #iterar la lista de peliculas
        for a in self.lista_apartamentos:
            self.tabla.insert('',0,text=a[0],
            values=(a[1],a[2],a[3],a[4]))

        #CREACION DE LOS BOTONES
        self.boton_Editar = tk.Button(self, text='Editar', command=self.editar_datos)
        self.boton_Editar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#158645',
                                                cursor='hand2', activebackground='#35BD6F')
        self.boton_Editar.grid(row=9,column=0, padx=10,pady=10)

        self.boton_Eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.boton_Eliminar.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='#BD152E',
                                                cursor='hand2', activebackground='#E15370')
        self.boton_Eliminar.grid(row=9,column=1, padx=10,pady=10) 

        self.boton_ir_apartamentos = tk.Button(self, text='Menu Principal', command=self.Menu_principal)
        self.boton_ir_apartamentos.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='blue',
                                                cursor='hand2', activebackground='blue')
        self.boton_ir_apartamentos.grid(row=9,column=3, padx=10,pady=10)        

    def Menu_principal(self):
        self.destroy()       

    def editar_datos(self):
        try:
            self.id_apartamento = self.tabla.item(self.tabla.selection())['text']
            self.direccion_apartamento = self.tabla.item(self.tabla.selection())['values'][0]
            self.numero_apartamento_apartamento = self.tabla.item(self.tabla.selection())['values'][1]
            self.matricula_apartamento = self.tabla.item(self.tabla.selection())['values'][2]
            self.ficha_catastral_apartamento = self.tabla.item(self.tabla.selection())['values'][3]
        
            self.habilitar_campos()
            self.entry_Direccion.insert(0, self.direccion_apartamento)
            self.entry_Numero_Apartamento.insert(0,self.numero_apartamento_apartamento)
            self.entry_Matricula_inmobiliaria.insert(0,self.matricula_apartamento)
            self.entry_Ficha_catastral.insert(0,self.ficha_catastral_apartamento)
        
        
        except:
            titulo = 'Editar un registro'
            mensaje= 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)       

    def eliminar_datos(self):
        
        try:
            self.id_apartamento = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_apartamento)
            self.tabla_apartamentos()
            self.id_apartamento = None

        except:
           titulo = 'Eliminar un registro'
           mensaje= 'No ha seleccionado ningun registro'
           messagebox.showerror(titulo, mensaje)    

