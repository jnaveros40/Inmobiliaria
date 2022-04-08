from logging import root
import tkinter as tk
 
root = tk.Tk()

scroll = tk.Scrollbar(root)
texto = tk.Text(root, height=10, width=30)

scroll.pack(side=tk.RIGHT, fill=tk.Y)
texto.pack(side=tk.LEFT, fill=tk.Y)

scroll.config(command=texto.yview)

texto.config(yscrollcommand=scroll.set)

mensaje="""Las teorías de cuerdas son una serie de hipótesis científicas y modelos fundamentales de física teórica que asumen que las partículas subatómicas, aparentemente puntuales, son en realidad «estados vibracionales» de un objeto extendido más básico llamado «cuerda» o «filamento».1​

De acuerdo con estas teorías, un electrón no sería un "punto" sin estructura interna y de dimensión cero, sino una cuerda minúscula en forma de lazo vibrando en un espacio-tiempo de más de cuatro dimensiones; de hecho, el planteamiento matemático de esta teoría no funciona a menos que el universo tenga once dimensiones. Mientras que un punto simplemente se movería por el espacio, una cuerda podría hacer algo más: vibrar de diferentes maneras. Si vibrase de cierto modo, veríamos un electrón; pero si lo hiciese de otro, veríamos un fotón, un quark o cualquier otra partícula del modelo estándar dependiendo de la forma concreta en que estuviese vibrando. Estas teorías, ampliada con otras como la de las supercuerdas o la Teoría M, pretende alejarse de la concepción del punto-partícula.

La siguiente formulación de una teoría de cuerdas se debe a Jöel Scherk y John Henry Schwarz, que en 1974 publicaron un artículo en el que mostraban que una teoría basada en objetos unidimensionales o "cuerdas" en lugar de partículas puntuales podía describir la fuerza gravitatoria, aunque estas ideas no recibieron en ese momento mucha atención hasta la Primera revolución de supercuerdas de 1984. 

"""

texto.insert(tk.END, mensaje)

root.mainloop()








