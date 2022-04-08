from .conexion_db import ConexionDB
from tkinter import messagebox


def crear_tabla_apartamento ():
    conexion = ConexionDB ()

    sql='''
    CREATE TABLE APARTAMENTOS(
        Id_Apartamento INTEGER,
	    DIRECCION VARCHAR(50),
	    APARTAMENTO	VARCHAR(50),
	    MATRICULA VARCHAR(50),
	    FICHA_CATASTRAL VARCHAR(50),
        PRIMARY KEY(Id_Apartamento AUTOINCREMENT)
    )'''
    #try:
    conexion.cursor.execute(sql)
    conexion.cerrar()

    titulo= 'Crear Registro'
    mensaje = 'Se creo la tabla en la base de datos'
    messagebox.showinfo(titulo, mensaje)
    '''
    except:
        titulo = 'Crerar Registro'
        mensaje= 'La tabla de apartamentos ya exite'
        messagebox.showerror(titulo, mensaje)'''


def borrar_tabla_apartamento():
    conexion = ConexionDB()

    sql = 'DROP TABLE APARTAMENTOS' 

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo= 'Eliminar Registro'
        mensaje = 'Se elimino la tabla de apartamentos de la base de datos'
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = 'Eliminar Registro'
        mensaje= 'La tabla de apartamentos no exite'
        messagebox.showerror(titulo, mensaje)

class Apartamento:
    def __init__(self, DIRECCION, APARTAMENTO, MATRICULA, FICHA_CATASTRAL):
        self.id_apartamento = None
        self.DIRECCION = DIRECCION
        self.APARTAMENTO = APARTAMENTO
        self.MATRICULA = MATRICULA
        self.FICHA_CATASTRAL=FICHA_CATASTRAL

    def __str__(self):
        return f'Apartamento[{self.DIRECCION},{self.APARTAMENTO},{self.MATRICULA},{self.FICHA_CATASTRAL}]'              

def guardar(apartamento):
    conexion = ConexionDB()

    sql= f"""INSERT INTO APARTAMENTOS (DIRECCION, APARTAMENTO, MATRICULA, FICHA_CATASTRAL)
    VALUES( '{apartamento.DIRECCION}',
            '{apartamento.APARTAMENTO}',
            '{apartamento.MATRICULA}',
            '{apartamento.FICHA_CATASTRAL}')"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo='Conexion al registro'
        mensaje='La tabla apartamentos no esta creada en la base de datos'
        messagebox.showerror(titulo,mensaje)

def listar_apartamento():
    conexion = ConexionDB()

    lista_apartamentos=[]

    sql = 'SELECT * FROM APARTAMENTOS'

    try:    
        conexion.cursor.execute(sql)
        lista_apartamentos = conexion.cursor.fetchall()
        conexion.cerrar()

    except:
        titulo='Conexion al registro'
        mensaje='Crea la base de datos'
        messagebox.showwarning(titulo,mensaje)

    return lista_apartamentos    

def editar(apartamento, Id_Apartamento):
    conexion = ConexionDB()

    sql = f"""UPDATE APARTAMENTOS
    SET DIRECCION = '{apartamento.DIRECCION}',
        APARTAMENTO = '{apartamento.APARTAMENTO}',
        MATRICULA = '{apartamento.MATRICULA}',
        FICHA_CATASTRAL = '{apartamento.FICHA_CATASTRAL}' 
    WHERE Id_Apartamento = {Id_Apartamento}     
    """
    try:    
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo='Edicion de datos'
        mensaje='No se ha podido editar este registro'
        messagebox.showwarning(titulo,mensaje)

def eliminar(Id_Apartamento):
    conexion = ConexionDB()
    sql = f'DELETE FROM APARTAMENTOS WHERE Id_Apartamento = {Id_Apartamento}'

    try:    
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo='Eliminar datos'
        mensaje='No se ha podido eliminar este registro'
        messagebox.showwarning(titulo,mensaje)
