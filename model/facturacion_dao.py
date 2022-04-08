from .conexion_db import ConexionDB
from tkinter import messagebox


def crear_tabla_facturacion ():
    conexion = ConexionDB ()

    sql='''
    CREATE TABLE FACTURACION(
        ID_FACTURACION INTEGER,
	    NOMBRE_INQUILINO VARCHAR(50),
	    APELLIDO_INQUILINO	VARCHAR(50),
	    DIRECCION VARCHAR(50),
	    APARTAMENTO VARCHAR(50),
        NOMBRE_PROPIETARIO VARCHAR(50),
        APELLIDO_PROPIETARIO VARCHAR(50),
        FECHA VARCHAR(50),
        FECHA_INICIO VARCHAR(50),
        FECHA_FINAL VARCHAR(50),
        VALOR VARCHAR(50),
        PRIMARY KEY(ID_FACTURACION AUTOINCREMENT)
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


def borrar_tabla_facturacion():
    conexion = ConexionDB()

    sql = 'DROP TABLE FACTURACION' 

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

class Facturacion:
    def __init__(self, NOMBRE_INQUILINO, APELLIDO_INQUILINO, DIRECCION, APARTAMENTO, NOMBRE_PROPIETARIO, APELLIDO_PROPIETARIO, FECHA, FECHA_INICIO, FECHA_FINAL, VALOR):
        self.ID_FACTURACION = None
        self.NOMBRE_INQUILINO = NOMBRE_INQUILINO
        self.APELLIDO_INQUILINO = APELLIDO_INQUILINO
        self.DIRECCION = DIRECCION
        self.APARTAMENTO = APARTAMENTO
        self.NOMBRE_PROPIETARIO = NOMBRE_PROPIETARIO
        self.APELLIDO_PROPIETARIO = APELLIDO_PROPIETARIO
        self.FECHA = FECHA
        self.FECHA_INICIO = FECHA
        self.FECHA_FINAL = FECHA_FINAL
        self.VALOR =VALOR

    def __str__(self):
        return f'Facturacion[{self.NOMBRE_INQUILINO},{self.APELLIDO_INQUILINO},{self.DIRECCION},{self.APARTAMENTO},{self.NOMBRE_PROPIETARIO},{self.APELLIDO_PROPIETARIO},{self.FECHA},{self.FECHA_INICIO},{self.FECHA_FINAL},{self.VALOR}]'              

def guardar(facturacion):
    conexion = ConexionDB()

    sql= f"""INSERT INTO FACTURACION (NOMBRE_INQUILINO, APELLIDO_INQUILINO, DIRECCION, APARTAMENTO, NOMBRE_PROPIETARIO, APELLIDO_PROPIETARIO, FECHA, FECHA_INICIO, FECHA_FINAL, VALOR)
    VALUES( '{facturacion.NOMBRE_INQUILINO}',
            '{facturacion.APELLIDO_INQUILINO}',
            '{facturacion.DIRECCION}',
            '{facturacion.APARTAMENTO}',
            '{facturacion.NOMBRE_PROPIETARIO}',
            '{facturacion.APELLIDO_PROPIETARIO}',
            '{facturacion.FECHA}',
            '{facturacion.FECHA_INICIO}',
            '{facturacion.FECHA_FINAL}',
            '{facturacion.VALOR}'
            )"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo='Conexion al registro'
        mensaje='La tabla APARTAMENTOS no esta creada en la base de datos'
        messagebox.showerror(titulo,mensaje)

def listar_facturacion():
    conexion = ConexionDB()

    lista_facturacion=[]

    sql = 'SELECT * FROM FACTURACION'

    try:    
        conexion.cursor.execute(sql)
        lista_facturacion = conexion.cursor.fetchall()
        conexion.cerrar()

    except:
        titulo='Conexion al registro'
        mensaje='Crea la base de datos'
        messagebox.showwarning(titulo,mensaje)

    return lista_facturacion    

def editar(facturacion, ID_FACTURACION):
    conexion = ConexionDB()

    sql = f"""UPDATE FACTURACION
    SET NOMBRE_INQUILINO = '{facturacion.NOMBRE_INQUILINO}',
        APELLIDO_INQUILINO = '{facturacion.APELLIDO_INQUILINO}',
        DIRECCION = '{facturacion.DIRECCION}',
        APARTAMENTO = '{facturacion.APARTAMENTO}',
        NOMBRE_PROPIETARIO = '{facturacion.NOMBRE_PROPIETARIO}',
        APELLIDO_PROPIETARIO = '{facturacion.APELLIDO_PROPIETARIO}',
        FECHA = '{facturacion.FECHA}',
        FECHA_INICIO = '{facturacion.FECHA_INICIO}',
        FECHA_FINAL = '{facturacion.FECHA_FINAL}',
        VALOR = '{facturacion.VALOR}'
    WHERE ID_FACTURACION = {ID_FACTURACION}     
    """
    try:    
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo='Edicion de datos'
        mensaje='No se ha podido editar este registro'
        messagebox.showwarning(titulo,mensaje)

def eliminar(ID_FACTURACION):
    conexion = ConexionDB()
    sql = f'DELETE FROM FACTURACION WHERE ID_FACTURACION = {ID_FACTURACION}'

    try:    
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo='Eliminar datos'
        mensaje='No se ha podido eliminar este registro'
        messagebox.showwarning(titulo,mensaje)
