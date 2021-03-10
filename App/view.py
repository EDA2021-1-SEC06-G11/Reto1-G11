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
    print('9- Cargar informacion en el catalogo')
    print("1- Encontrar buenos videos por categoría y país")
    print("2- Encontrar video tendencia por país")
    print("3- Encontrar video tendencia por categoría")
    print("4- Buscar los videos con más likes")
    print("0- Salir")

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)
    
def printResults(ord_videos,sample):
    size  = lt.size(ord_videos)
    if size > sample:
        print('Los primero ', sample, ' videos ordenados son:')
        i = 0
        while i < sample:
            video = lt.getElement(ord_videos, i)
            print('Titulo: '+ video['title']+' Channel title: '+video['channel_title']+' trending date: '+
             video['trending_date']+ ' Country'+ video['country']+ ' Views: '+ video['views']+' likes: '+
              video['likes']+' dislikes: '+ video['dislikes'])
            i+=1

def printResultsR1(list_sorted,sample):
    size  = lt.size(list_sorted)
    if int(size+1) > int(sample):
        print('Los primero ', sample, ' videos ordenados son:')
        i = 1
        while i <= int(sample):
            video = lt.getElement(list_sorted, i)
            print('Titulo: '+ video['title']+' Channel title: '+video['channel_title']+' trending date: '+
            video['trending_date']+ ' Publish time'+ video['publish_time']+ ' Views: '+ video['views']+' likes: '+
            video['likes']+' dislikes: '+ video['dislikes'])
            i += 1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0])==9:
        print('Cargando datos....')
        catalog = initCatalog()
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categories'])))
        printResults(catalog['videos'],1)
        print(catalog['categories']['elements'])
        
        
    elif int(inputs[0]) == 1:
        n = input('Indique numero de videos que quiere listar: ')
        category = input('Indique la categoria: ')
        country = input('Indique el pais: ')
        size = lt.size(catalog['videos'])
        list_sorted = controller.sortVideosR1(catalog, int(size), category, country)
        printResultsR1(list_sorted[1], n) 
  

    elif int(inputs[0]) == 2:
        country = input('Indique el pais: ')
        size = lt.size(catalog['videos'])
        list_sorted = controller.sortVideosR2(catalog, size, country)
        print(list_sorted)

    elif int(inputs[0]) == 3:
        category = input('indique la categoria: ')
        size = lt.size(catalog['videos'])
        list_sorted = controller.sortVideosR3(catalog, size, category)
        print(list_sorted)

    elif int(inputs[0]) == 4:
        n = input('Indique numero de videos para listar: ')
        country = input('Indique el pais: ')
        category = input('Indique la categoria: ')
        size = lt.size(catalog['videos'])
        list_sorted = controller.sortVideosR3(catalog, size, category, country)
        

    else:
        sys.exit(0)
sys.exit(0)
