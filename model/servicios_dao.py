from .conexion_db import ConexionDB
from tkinter import messagebox


def crear_tabla_servicios ():
    conexion = ConexionDB ()

    sql='''
    CREATE TABLE SERVICIOS(
        ID_SERVICIO INTEGER,
        TIPO_SERVICIO VARCHAR(50),
        CODIGO_SERVICIO VARCHAR(50),
        ID_APARTAMENTO INTEGER,
	    DIRECCION VARCHAR(50),
	    APARTAMENTO VARCHAR(50),
        FECHA_INICIO VARCHAR(50),
        FECHA_FINAL VARCHAR(50),
        VALOR_SERVICIO VARCHAR(50),
        PRIMARY KEY(ID_SERVICIO AUTOINCREMENT)
    )'''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

        titulo= 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = 'Crerar Registro'
        mensaje= 'La tabla ya exite'
        messagebox.showerror(titulo, mensaje)


def borrar_tabla_servicios():
    conexion = ConexionDB()

    sql = 'DROP TABLE SERVICIOS' 

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo= 'Eliminar Registro'
        mensaje = 'Se elimino la tabla de la base de datos'
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = 'Eliminar Registro'
        mensaje= 'La tabla no exite'
        messagebox.showerror(titulo, mensaje)

class Servicios:
    def __init__(self, TIPO_SERVICO, CODIGO_SERVICIO, ID_APARTAMENTO, DIRECCION, APARTAMENTO, FECHA_INICIO, FECHA_FINAL, VALOR_SERVICIO):
        self.ID_SERVICIO = None
        self.TIPO_SERVICIO = TIPO_SERVICO
        self.CODIGO_SERVICIO = CODIGO_SERVICIO
        self.ID_APARTAMENTO = ID_APARTAMENTO
        self.DIRECCION = DIRECCION
        self.APARTAMENTO = APARTAMENTO
        self.FECHA_INICIO = FECHA_INICIO
        self.FECHA_FINAL = FECHA_FINAL
        self.VALOR_SERVICIO =VALOR_SERVICIO

    def __str__(self):
        return f'Servicio[{self.TIPO_SERVICIO},{self.CODIGO_SERVICIO},{self.ID_APARTAMENTO},{self.DIRECCION},{self.APARTAMENTO},{self.FECHA_INICIO},{self.FECHA_FINAL},{self.VALOR}]'              

def guardar(servicio):
    conexion = ConexionDB()

    sql= f"""INSERT INTO SERVICIOS (TIPO_SERVICIO, CODIGO_SERVICIO, ID_APARTAMENTO, DIRECCION, APARTAMENTO, FECHA_INICIO, FECHA_FINAL, VALOR_SERVICIO)
    VALUES( '{servicio.TIPO_SERVICIO}',
            '{servicio.CODIGO_SERVICIO}',
            '{servicio.ID_APARTAMENTO}',
            '{servicio.DIRECCION}',
            '{servicio.APARTAMENTO}',
            '{servicio.FECHA_INICIO}',
            '{servicio.FECHA_FINAL}',
            '{servicio.VALOR_SERVICIO}'
            )"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo='Conexion al registro'
        mensaje='La tabla SERVICOS PUBLICOS no esta creada en la base de datos'
        messagebox.showerror(titulo,mensaje)

def listar_servicios():
    conexion = ConexionDB()

    lista_facturacion=[]

    sql = 'SELECT * FROM SERVICIOS'

    try:    
        conexion.cursor.execute(sql)
        lista_facturacion = conexion.cursor.fetchall()
        conexion.cerrar()

    except:
        titulo='Conexion al registro'
        mensaje='Crea la base de datos'
        messagebox.showwarning(titulo,mensaje)

    return lista_facturacion    

def editar(servicio, ID_SERVICIO):
    conexion = ConexionDB()

    sql = f"""UPDATE SERVICIOS
    SET TIPO_SERVICIO = '{servicio.TIPO_SERVICIO}',
        CODIGO_SERVICIO = '{servicio.CODIGO_SERVICIO}',
        ID_APARTAMENTO = '{servicio.ID_APARTAMENTO}',
        DIRECCION = '{servicio.DIRECCION}',
        APARTAMENTO = '{servicio.APARTAMENTO}',
        FECHA_INICIO = '{servicio.FECHA_INICIO}',
        FECHA_FINAL = '{servicio.FECHA_FINAL}',
        VALOR_SERVICIO = '{servicio.VALOR_SERVICIO}'
    WHERE ID_SERVICIO = {ID_SERVICIO}     
    """
    try:    
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo='Edicion de datos'
        mensaje='No se ha podido editar este registro'
        messagebox.showwarning(titulo,mensaje)

def eliminar(ID_SERVICIO):
    conexion = ConexionDB()
    sql = f'DELETE FROM SERVICIOS WHERE ID_SERVICIO = {ID_SERVICIO}'

    try:    
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo='Eliminar datos'
        mensaje='No se ha podido eliminar este registro'
        messagebox.showwarning(titulo,mensaje)
