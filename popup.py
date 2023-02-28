"""
    Importa la función para la generación del mensaje de alerta sobre la presencia del virus en el equipo.

Example:

    >>> import popup
    >>> popup.generate_message()
"""

from tkinter import Tk, Label

def generate_message():
    """
        Función que genera el mensaje en pantalla para anunciar la presencia del virus del TEAMHAWKS
    """
    root = Tk() # iniciamos el objeto tipo Tk() para crear la ventana a mostrar
    root.overrideredirect(True) # desactiva la barra superior de la ventana para que esta no pueda ser cerrada.

    # sección de posicionamiento de la ventana en centro de la pantalla
    
    screen_width = root.winfo_screenwidth() # obtiene el valor del ancho del monitor del usuario
    screen_height = root.winfo_screenheight() # obtiene el valor de la altura del monitor del usuario
    x_cordinate = int((screen_width/2) - (800/2)) # calcula la posición en el centro de la ventana de la coordenada x
    y_cordinate = int((screen_height/2) - (50/2)) # calcula la posición en el centro de la ventana de la coordenada y
    root.geometry(f'800x50+{x_cordinate}+{y_cordinate}') # estable las características geométricas de la ventana
    # ubica la ventana en el centro de la pantalla con una anchura de 800 pixeles y una altura de 50 pixeles.

    # creamos el mensaje a presentar cuenta con fuente arial tamaño 12 y color rojo.

    message = Label(root,text='USTED HA SIDO INFECTADO POR UN KEYLOGGER DESARROLADO POR TEAMHAWKS',
                    font='ARIALBLACK 12',fg='Red')
    message.pack(expand=True) # agregamos el mensaje en la ventana ubicándolo justo en el centro. 

    root.call('wm', 'attributes', '.', '-topmost', '1') # posiciona la ventana generada encima de todas las demás ventanas.

    # sustitos del método mainloop() de modo que el código no quede atascado en el mensaje presentado.
    root.update_idletasks() 
    root.update()