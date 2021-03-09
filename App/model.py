﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as qui

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'videos': None,
               'categories': None,}

    catalog['videos'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['categories'] = lt.newList(datastructure='ARRAY_LIST')
                                 

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog,video):
    lt.addLast(catalog['videos'], video)


def addCategoryID(catalog, category):
    t = newCategoryID(category['name'], category['id'])
    lt.addLast(catalog['categories'], t)

# Funciones para creacion de datos

def newCategoryID(id, name):
    category = {'category_name':'', 'category_id': ''}
    category['category_name'] = name
    category['category_id'] = id
    return category

def newVideoCategory(category_id, video_id):
    videocategory = {'category_id': category_id, 'video_id': video_id}
    return videocategory


# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista


def comparecategorynames(name, category):
    return (name==category['name'])

def cmpVideosByViews(video1, video2):
    if float(video1['views']) > float(video2['views']):
        return True
    else:
        return False
  
def cmpVideosByID(video1, video2):
    if int(video1['id'])> int(video2['id']):
        return 1
    elif int(video1['id']) == int(video2['id']):
        return 0
    else:
        return -1


# Funciones de ordenamiento

def sortVideos(catalog,sort_type,size):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if sort_type == 'shell':
        sorted_list = ss.sort(sub_list, cmpVideosByViews)
    elif sort_type == 'selection':
        sorted_list = sel.sort(sub_list, cmpVideosByViews)
    elif sort_type == 'insertion':
        sorted_list = ins.sort(sub_list, cmpVideosByViews)
    elif sort_type == 'merge':
        sorted_list = mer.sort(sub_list, cmpVideosByViews)
    elif sort_type == 'quick':
        sorted_list = qui.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
