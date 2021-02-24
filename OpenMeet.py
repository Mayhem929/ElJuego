import webbrowser
from datetime import datetime

##########################################################################
##########################################################################
# Enlaces Google Meet. Pueden variar de usuario a otro, recomiendo revisarlas

auth_user = '1'

mp_teoria = 'https://meet.google.com/mme-zppa-ptf?pli=1&authuser=' + auth_user
mp_pract = 'https://meet.google.com/tiu-gzpp-gfq?pli=1&authuser=' + auth_user
fs = 'https://meet.google.com/brs-jtop-ivv?pli=1&authuser=' + auth_user
geo = 'https://meet.google.com/fku-gqfb-ybw?pli=1&authuser=' + auth_user
calc = 'https://meet.google.com/sgo-fqpd-hko?pli=1&authuser=' + auth_user
edip = 'https://youtu.be/bxqLsrlakK8'
mn = 'https://meet.google.com/oej-ooub-tuq?pli=1&authuser=' + auth_user

##########################################################################
# Funcion para abrir la pestaña

def open_url(url):
    webbrowser.open_new_tab(url)

##########################################################################
# Encontramos la hora y dia actual

date = datetime
now = date.now()
day = now.weekday()
day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

hora = now.hour
minuto = now.minute

##########################################################################
# Lunes

hora_ref = 17
min_ref = 45

if day_name[day] == 'Monday':

    if hora < hora_ref:
        webbrowser.open_new_tab(mp_teoria)
    else:
        webbrowser.open_new_tab(mp_pract)

##########################################################################
# Martes

if day_name[day] == 'Tuesday':

    open_url(fs)

##########################################################################
# Miércoles

hora_ref = 16

if day_name[day] == 'Wednesday':
    for asig in [calc, mn, mn, edip, geo]:
        if (hora == hora_ref - 1 and minuto >= min_ref) or \
                (hora == hora_ref and minuto < min_ref):
            open_url(asig)
            hora_ref += 1

##########################################################################
# Jueves

hora_ref = 15

if day_name[day] == 'Thursday':
    for asig in [calc, calc, mn, edip, edip, geo]:
        if (hora == hora_ref - 1 and minuto >= min_ref) or \
                (hora == hora_ref and minuto < min_ref):
            open_url(asig)
            hora_ref += 1

##########################################################################
# Viernes

hora_ref = 16

if day_name[day] == 'Friday':
    for asig in [calc, mn, edip, geo, geo]:
        if (hora == hora_ref - 1 and minuto >= min_ref) or \
                (hora == hora_ref and minuto < min_ref):
            open_url(asig)
            hora_ref += 1

##########################################################################
