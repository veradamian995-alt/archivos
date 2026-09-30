try: 
    arch = open("tabla-n.txt","r")
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
            print(linea)

    arch.close()
except IOError:
    print("Ha ocurrido un error al intentar abrir el archivo")    