"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*100)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Tipo de algoritmo de ordenamiento iterativo")
    print("3- Encontrar video tendencia por país (I)")
    print("4- Encontrarvideo tendencia por categoría (I)")
    print('5- Buscar los videos con más likes')
    print("0- Salir")

def initCatalog(tipo_de_lista):
    return controller.initCatalog(tipo_de_lista)

def loadData(catalog):
    controller.loadData(catalog)
    
def printResults(ord_videos,sample=10):
    size  = lt.size(ord_videos)
    if size > sample:
        print('Los primero ', sample, ' videos ordenados son:')
        i = 0
        while i <= sample:
            video = lt.getElement(ord_videos, i)
            print('Titulo: '+ video['title']+ ' Views: '+ video['views'])
            i+=1
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        lista = input(str('Escriba que tipo de representacion de la lista desea: '))
        print("Cargando información de los archivos ....")
        catalog = initCatalog(lista)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categories'])))

    elif int(inputs[0]) == 2:
        tipo_algoritmo = input('Por favor escriba cual tipo de algoritmo desea entre "selection", "insertion", "shell", "merge" o "quick"')
        size = input("Indique tamaño de la muestra: ")
        list_sorted = controller.sortVideos(catalog,tipo_algoritmo,int(size))
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(list_sorted[0]))
                        
        printResults(list_sorted[1])


    else:
        sys.exit(0)
sys.exit(0)
