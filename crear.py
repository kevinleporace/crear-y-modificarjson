import os #if os.path.isfile(nombrearchivo):hacer lectura sino crear escritura
import json
import valida

archivo=valida.archivo()
def ingresar_datos():
    diccionario={}
    lista=[]
    empresa=input('Ingrese nombre de la empresa: ')
    url=input('Ingrese url de la empresa: ')
    descripcion=input('Ingrese descripcion de la empresa:')
    lista.append(url)
    lista.append(descripcion)
    diccionario[empresa]=lista
    return diccionario

def aplicacion():
    
   
    if os.path.isfile(archivo):
        #abrir en modo lectura
        
        with open(archivo,'r',encoding='utf-8')as f:
            data=json.load(f)
            print(data)
            print(archivo)
    else:
        diccionario=ingresar_datos()
        #abrir en modo escritura
        with open(archivo,'w',encoding='utf-8')as f:
            json.dump(diccionario,f,indent=4)

aplicacion()
