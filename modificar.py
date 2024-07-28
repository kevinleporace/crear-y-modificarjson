#el archivo esta validado
import valida
import json
import crear
def modificar():
    arch=valida.archivo()
    titulo=input('ingrese titulo: ')
    with open(arch,'r',encoding='utf-8')as f:
        data=json.load(f)
        #me aseguro que lo escriba bien o que ingrese fin para terminar
        while titulo!='fin' and (titulo not in data):
            print('El titulo ingresado no existe o esta mal escrito')
            titulo=input('Ingrese titulo o fin para cancelar:')

    #hacer la modificacion si titulo no fue fin
    if titulo!='fin':
        diccionario=crear.ingresar_datos()
        with open(arch,'w',encoding='utf-8')as f:
            json.dump(diccionario,f,indent=4)

if valida:
    modificar()
else:
    print('el archivo no existe')
 # if titulo in data:
        #     print('debug:  ',data[titulo])
        # else:
        #     print('debug:  ese titulo no es correcto')