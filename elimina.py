import os
import valida

#si el archivo existe
if valida.valida():
    archivo=valida.archivo()
    os.remove(archivo)
    print(f"{archivo} ha sido eliminado.")
else:
    print(f"El archivo no existe o ya fue eliminado.")