def eje1():
    n = int(input("ingrese un numero entre 1 y 10: "))

    archivo = open("tabla-" + str(n) + ".txt", "w")

    for i in range(1, 11):
        r = n * i
        archivo.write(str(n) + " x " + str(i) + " = " + str(r) + "\n")

    archivo.close()
    print("tabla guardada correctamente")
#eje1()


def eje2():
    n = int(input("ingrese un numero entre 1 y 10: "))

    try:
        archivo = open("tabla-" + str(n) + ".txt", "r")

        for linea in archivo:
            print(linea, end="")

        archivo.close()

    except:
        print("el fichero no existe")
#eje2()


def eje3():
    n = int(input("ingrese el numero de la tabla: "))
    m = int(input("ingrese el numero de linea: "))

    try:
        archivo = open("tabla-" + str(n) + ".txt", "r")

        for i in range(m):
            linea = archivo.readline()

        print(linea, end="")

        archivo.close()

    except:
        print("el fichero no existe")
#eje3()


def eje4():
    from urllib.request import urlopen

    url = input("ingrese la url: ")

    archivo = urlopen(url)
    texto = archivo.read().decode("utf-8")

    palabras = texto.split()

    print("el numero de palabras es: ", len(palabras))

    archivo.close()
#eje4()


def eje5():
    import csv

    archivo = open("cotización.csv", "r", encoding="utf-8")

    lector = csv.DictReader(archivo, delimiter=";")

    datos = {}

    for columna in lector.fieldnames:
        datos[columna] = []

    for fila in lector:
        for columna in lector.fieldnames:
            datos[columna].append(fila[columna])

    archivo.close()

    archivo = open("cotizaciones.csv", "r", encoding="utf-8")

    escritor = csv.writer(archivo)

    escritor.writerow(["Columna", "Minimo", "Maximo", "Media"])

    for columna in datos:
        if columna != "Nombre":
            valores = []

            for valor in datos[columna]:
                valores.append(float(valor.replace(",", ".")))

            minimo = min(valores)
            maximo = max(valores)
            media = sum(valores) / len(valores)

            escritor.writerow([columna, minimo, maximo, media])

    archivo.close()

    print("archivo creado correctamente")
#eje5()