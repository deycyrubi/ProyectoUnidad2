from Numero import Numero
from Numero import Numero

class Archivos:

    def leerArchivo(self, archivo):
        file = open(archivo,'r')
        lineas_archivo = []
        for a in file.readlines():
            linea = a.replace('\n', '')
            lista = linea.split(',')

            try:
               lineas_archivo.append([int(lista[0]), int(lista[1]),])
            except ValueError:
               lineas_archivo.append([0,0])
        file.close()
        del (file)
        return lineas_archivo

    def escribirArchivoTresEUnaS(self, encabezado, archivo, lista, resultado):
        file = open(archivo, 'w')
        file.write(encabezado + '\n')
        for a in range(0, len(lista)):
            file.write(str(lista[a][0])+ ',' + str(lista[1]) + ','
                       + str(lista[a][2]) + ',' + str(resultado[a] + '\n'))
            file.close()
            del(file)


    def escribirarchivo(self, encabezado, archivo, lista, resultados):
        file = open(archivo, 'w')
        file.write(encabezado + '\n')
        for a in range(0, len(lista)):
            file.write(str(lista[a][0])+ ',' + str(resultados[a]) + '\n')
        file.close()
        del(file)

def main():
    archivo = Archivos()
    lista = archivo.leerArchivo(len('Numero.txt'))
    resultados = []
    num = Numero()
    for a in range(0, len(lista)):
     resultados.append(num.getNumeroPotencia(lista[a][0], lista[a][1], lista[a][2]))
    archivo.escribirArchivoTresEUnaS('numero', 'Numero.csv', lista, resultados)

    return 0

if __name__== '__main__':
    main()
