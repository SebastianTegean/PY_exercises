# ESERCIZIO 2 - Che tempo fa? 🌤
# Per poter utillizare il programma bisona installare le seguente librerie: 
#    pip install requests
#    pip install pyfiglet
#    pip install termcolor

import requests
import pyfiglet
import termcolor


api_kei = '#################' # Inserire la propria api key
localita = input("Introdure la localitá: ")

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=it&units=metric'.format(localita, api_kei)

res = requests.get(url)
data = res.json()
print(data)
umidita = data['main']['humidity']
pressione = data['main']['pressure']
# Per il vento devo covertire i m/s in km/h 
vento_ms = float(data['wind']['speed']) 
vento_km = vento_ms * 3.6
vento = round(vento_km, 2)

description = data['weather'][0]['description']
temp = data['main']['temp']
temp_min = data['main']['temp_min']
temp_max = data['main']['temp_max']
termcolor.cprint('_____________________________________________________________________________','green')
result = pyfiglet.figlet_format(f" Il meteo a {localita}")
termcolor.cprint(result, 'yellow')
print('Deescrizione climatica:', end=' ')
termcolor.cprint(description,'green', attrs=['bold'])
print('Temperatura base: ', end=' ')
termcolor.cprint(f'{temp} °C','yellow', attrs=['bold'])
print('Temperatura minima:  ', end=' ')
termcolor.cprint(f'{temp_min} °C','blue', attrs=['bold'])
print('Temperatura massima:', end=' ')
termcolor.cprint(f'{temp_max} °C','red', attrs=['bold'])
print('Velocitá del vento:   ', end=' ')
termcolor.cprint(f'{vento} km/h', 'yellow', attrs=['bold'])
print('Umidita: ', end=' ')
termcolor.cprint(f'{umidita}%','blue', attrs=['bold'])

termcolor.cprint('_____________________________________________________________________________\n','green')
termcolor.cprint('                       Grazie per aver usato questo programma                ','white','on_red', attrs=['bold'])
termcolor.cprint('_____________________________________________________________________________\n','green')
print(data)