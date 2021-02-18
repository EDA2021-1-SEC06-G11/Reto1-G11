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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'videos': None,
               'categories': None,}

    catalog['videos'] = lt.newList()
    catalog['categories'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparecategorynames)

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


# Funciones de ordenamiento
