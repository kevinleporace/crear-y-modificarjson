'''es true o false segun se crea el archivo'''
import os
def valida():
    return os.path.isfile('archivo3.json')
#nombre del archivo
def archivo():
    return 'archivo3.json'