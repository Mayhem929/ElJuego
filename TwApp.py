cadena = "El oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera, llena de cactus, " \
         "en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza, torcidos " \
         "arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque " \
         "Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excurcionistas, acampadores y " \
         "entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones " \
         "de esta region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para " \
         "visitarla es de Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las " \
         "plantas del desierto con la humedad en el aire." \
         "El oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera, llena de cactus, " \
         "en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza, torcidos " \
         "arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque " \
         "Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excurcionistas, acampadores y " \
         "entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones " \
         "de esta region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para " \
         "visitarla es de Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las " \
         "plantas del desierto con la humedad en el aire."

sigo      = True
result    = '\n\n'
num_parte = 2

while sigo:

    ultimo_espacio = cadena.rfind(' ', 0, 275)

    subcadena = cadena[:ultimo_espacio]
    cadena = cadena[ultimo_espacio + 1:]

    result += subcadena + ' (+)' + '\n\n'
    num_parte += 1

    if len(cadena) < 280:
        sigo = False
        result += cadena

result = result[:-5]

print(result)
