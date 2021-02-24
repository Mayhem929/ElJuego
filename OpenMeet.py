import webbrowser
from datetime import datetime

##########################################################################
##########################################################################
# Enlaces Google Meet. Pueden variar de usuario a otro, recomiendo revisarlas

auth_user = '1'

mp_teoria = 'https://meet.google.com/mme-zppa-ptf?pli=1&authuser=' + auth_user
mp_pract  = 'https://meet.google.com/tiu-gzpp-gfq?pli=1&authuser=' + auth_user
fs        = 'https://meet.google.com/brs-jtop-ivv?pli=1&authuser=' + auth_user
geo       = 'https://meet.google.com/fku-gqfb-ybw?pli=1&authuser=' + auth_user
calc      = 'https://meet.google.com/nta-ggiq-bxz?pli=1&authuser=' + auth_user
edip1     = 'https://meet.google.com/bqh-etiv-tta?pli=1&authuser=' + auth_user
edip2     = 'https://meet.google.com/wmb-uufq-kdy?pli=1&authuser=' + auth_user
edip3     = 'https://meet.google.com/ovy-thqp-gtg?pli=1&authuser=' + auth_user
mn        = 'https://meet.google.com/oej-ooub-tuq?pli=1&authuser=' + auth_user
rr        = 'https://youtu.be/bxqLsrlakK8'


##########################################################################
# Funcion para abrir la pestaña

def open_url(url):
    webbrowser.open_new_tab(url)


##########################################################################
# Encontramos la hora y dia actual

date = datetime
now = date.now()
hora = now.hour
minuto = now.minute
day = now.weekday()
day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

rkrl = True

##########################################################################
# Lunes

hora_ref = 17

if day_name[day] == 'Monday':

    if hora_ref - 2 < hora < hora_ref:
        open_url(mp_teoria)
    elif hora_ref < hora < hora_ref + 2:
        open_url(mp_pract)
    else:
        open_url(rr)

##########################################################################
# Martes

hora_ref = 17

if day_name[day] == 'Tuesday':

    if hora_ref - 2 < hora < hora_ref + 2:
        open_url(fs)
    else:
        open_url(rr)

##########################################################################
# Miércoles

hora_ref = 16
min_ref = 45

if day_name[day] == 'Wednesday':
    for asig in [calc, mn, mn, edip1, geo]:
        if (hora == hora_ref - 1 and minuto >= min_ref) or \
                (hora == hora_ref and minuto < min_ref):
            open_url(asig)
            rkrl = False
        hora_ref += 1
    if rkrl: open_url(rr)

##########################################################################
# Jueves

hora_ref = 15

if day_name[day] == 'Thursday':
    for asig in [calc, calc, mn, edip2, edip2, geo]:
        if (hora == hora_ref - 1 and minuto >= min_ref) or \
                (hora == hora_ref and minuto < min_ref):
            open_url(asig)
            rkrl = False
        hora_ref += 1
    if rkrl: open_url(rr)

##########################################################################
# Viernes

hora_ref = 16

if day_name[day] == 'Friday':
    for asig in [calc, mn, edip3, geo, geo]:
        if (hora == hora_ref - 1 and minuto >= min_ref) or \
                (hora == hora_ref and minuto < min_ref):
            open_url(asig)
            rkrl = False
        hora_ref += 1
    if rkrl: open_url(rr)

##########################################################################
################## ᕦ( ͡° ͜ʖ ͡°)ᕤ EL FINDE ¯\_(ツ)_/¯ ######################
##########################################################################

if day_name[day] == 'Saturday':
    open_url('https://www.youtube.com/watch?v=MpqGPJz5aQY')

if day_name[day] == 'Sunday':
    open_url('https://www.youtube.com/watch?v=Vz1-R3UKVuw')
