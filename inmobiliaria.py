import tkinter as tk
from client.gui_app_apartamento import Frame_apartamentos, barra_menu_apartamento, borrar_tabla_apartamento, crear_tabla_apartamento
from client.gui_app_inquilino import Frame_inquilino, barra_menu_inquilino, crear_tabla_inquilino, borrar_tabla_inquilino
from client.gui_app_facturacion import Frame_facturacion, barra_menu_facturacion, crear_tabla_facturacion, borrar_tabla_facturacion


def main():
    def inicio_apartamento():
        #barra_menu_apartamento(root=root)
        app = Frame_apartamentos(root = root)

    def inicio_inquilino():
        #barra_menu_inquilino(root=root)
        app = Frame_inquilino(root = root)

    def inicio_facturacion():
        #barra_menu_facturacion(root=root)
        app = Frame_facturacion(root = root)    
    
    def salir():
        root.destroy()

    root = tk.Tk()
    root.title('Inmobiliaria Finca Raiz') #Titulo de la ventana
    #root.iconbitmap('') #Colocar una imagen
    root.resizable(1,1) #para poder modificar el tamanno
    root.config(width=610, height=190)

    #Barra_menu
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=500, height = 30)
    
    menu_apartamento = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label='Apartameto', menu=menu_apartamento)
    menu_apartamento.add_command(label='Consultar Apartamentos', command=inicio_apartamento)
    menu_apartamento.add_command(label='Crear tabla de apartamentos', command=crear_tabla_apartamento)
    menu_apartamento.add_command(label='Borrar tabla de apartamentos', command=borrar_tabla_apartamento)
    
    menu_inquilino = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label='Inquilinos', menu=menu_inquilino)
    menu_inquilino.add_command(label='Consultar Inquilino', command=inicio_inquilino)
    menu_inquilino.add_command(label='Crear tabla de Inquilinos', command=crear_tabla_inquilino)
    menu_inquilino.add_command(label='Borrar tabla de Inquilinos', command=borrar_tabla_inquilino)
    
    menu_facturacion = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label='Facturacion', menu=menu_facturacion)
    menu_facturacion.add_command(label='Consultar Facturacion', command=inicio_facturacion)
    menu_facturacion.add_command(label='Crear tabla de facturaciones', command=crear_tabla_facturacion)
    menu_facturacion.add_command(label='Borrar tabla de facturaciones', command=borrar_tabla_facturacion)

    barra_menu.add_command(label='Salir', command=root.destroy)

    '''
    boton_Apartamento = tk.Button(text="Apatamentos", command=inicio_apartamento)
    boton_Apartamento.place(x=55, y=5)
    boton_Apartamento.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='blue',
                                                cursor='hand2', activebackground='blue')

    boton_inquilino = tk.Button(text="Inquilinos", command=inicio_inquilino)
    boton_inquilino.place(x=55, y=50)
    boton_inquilino.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='blue',
                                                cursor='hand2', activebackground='blue')

    boton_facturacion = tk.Button(text="Facturacion", command=inicio_facturacion)
    boton_facturacion.place(x=55, y=95)
    boton_facturacion.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='blue',
                                                cursor='hand2', activebackground='blue')                                            
    
    boton_salir = tk.Button(text="Salir", command=salir)
    boton_salir.place(x=55, y=140)
    boton_salir.config(width=20, font=('Times New Roman',12,'bold'),
                                                fg = '#DAD5D6', bg='blue',
                                                cursor='hand2', activebackground='blue')                                          
    '''
    root.mainloop()

if __name__ == '__main__':
    main()
