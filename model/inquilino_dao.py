from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla_inquilino ():
    conexion = ConexionDB ()

    sql='''
    CREATE TABLE INQUILINOS(
        ID_INQUILINO	INTEGER NOT NULL,
        NOMBRE VARCHAR(50),
        APELLIDOS VARCHAR(50),
        CEDULA VARCHAR(50),
        TELEFONO VARCHAR(50),
        CORREO VARCHAR(50),
        CO_NOMBRE VARCHAR(50),
        CO_APELLIDO VARCHAR(50),
        CO_CEDULA VARCHAR(50),
        CO_TELEFONO VARCHAR(50),
        CO_CORREO VARCHAR(50),
        PRIMARY KEY (ID_INQUILINO AUTOINCREMENT)
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


def borrar_tabla_inquilino():
    conexion = ConexionDB()

    sql = 'DROP TABLE INQUILINOS' 

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

class Inquilino:
    def __init__(self, NOMBRE, APELLIDOS, CEDULA, TELEFONO, CORREO, CO_NOMBRE, CO_APELLIDO, CO_CEDULA, CO_TELEFONO, CO_CORREO):
        self.ID_INQUILINO = None
        self.NOMBRE = NOMBRE
        self.APELLIDOS = APELLIDOS
        self.CEDULA = CEDULA
        self.TELEFONO=TELEFONO
        self.CORREO = CORREO
        self.CO_NOMBRE = CO_NOMBRE
        self.CO_APELLIDO = CO_APELLIDO
        self.CO_CEDULA = CO_CEDULA
        self.CO_TELEFONO = CO_TELEFONO
        self.CO_CORREO=CO_CORREO

    def __str__(self):
        return f'Inquilino[{self.NOMBRE},{self.APELLIDOS},{self.CEDULA},{self.TELEFONO},{self.CORREO},{self.CO_NOMBRE},{self.CO_APELLIDO},{self.CO_CEDULA},{self.CO_TELEFONO},{self.CO_CORREO}]'              

def guardar(inquilino):
    conexion = ConexionDB()

    sql= f"""INSERT INTO INQUILINOS (NOMBRE, APELLIDOS, CEDULA, TELEFONO, CORREO, CO_NOMBRE, CO_APELLIDO, CO_CEDULA, CO_TELEFONO, CO_CORREO)
    VALUES( '{inquilino.NOMBRE}',
            '{inquilino.APELLIDOS}',
            '{inquilino.CEDULA}',
            '{inquilino.TELEFONO}',
            '{inquilino.CORREO}',
            '{inquilino.CO_NOMBRE}',
            '{inquilino.CO_APELLIDO}',
            '{inquilino.CO_CEDULA}',
            '{inquilino.CO_TELEFONO}',
            '{inquilino.CO_CORREO}'
           )"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo='Conexion al registro'
        mensaje='La tabla de inquilinos no esta creada en la base de datos'
        messagebox.showerror(titulo,mensaje)

def listar_inquilino():
    conexion = ConexionDB()

    lista_apartamentos=[]

    sql = 'SELECT * FROM INQUILINOS'

    try:    
        conexion.cursor.execute(sql)
        lista_inquilinos = conexion.cursor.fetchall()
        conexion.cerrar()

    except:
        titulo='Conexion al registro'
        mensaje='Crea la base de datos'
        messagebox.showwarning(titulo,mensaje)

    return lista_inquilinos    

def editar(inquilino, ID_INQUILINO):
    conexion = ConexionDB()

    sql = f"""UPDATE INQUILINOS
    SET NOMBRE = '{inquilino.NOMBRE}',
        APELLIDOS = '{inquilino.APELLIDOS}',
        CEDULA = '{inquilino.CEDULA}',
        TELEFONO = '{inquilino.TELEFONO}',
        CORREO = '{inquilino.CORREO}',
        CO_NOMBRE = '{inquilino.CO_NOMBRE}',
        CO_APELLIDO = '{inquilino.CO_APELLIDO}',
        CO_CEDULA = '{inquilino.CO_CEDULA}',
        CO_TELEFONO = '{inquilino.CO_TELEFONO}',
        CO_CORREO = '{inquilino.CO_CORREO}'
    WHERE ID_INQUILINO = {ID_INQUILINO}     
    """
    try:    
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo='Edicion de datos'
        mensaje='No se ha podido editar este registro'
        messagebox.showwarning(titulo,mensaje)

def eliminar(ID_INQUILINO):
    conexion = ConexionDB()
    sql = f'DELETE FROM INQUILINOS WHERE ID_INQUILINO = {ID_INQUILINO}'

    try:    
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo='Eliminar datos'
        mensaje='No se ha podido eliminar este registro'
        messagebox.showwarning(titulo,mensaje)
