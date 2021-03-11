"""
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
from datetime import datetime
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

def modeloR1(catalog, category, country):
    BestVideos = newCatalog()
    for pos in range(0,int(lt.size(catalog['videos']))):
        element = lt.getElement(catalog['videos'], pos)
        if (element['country'] == country) and (int(element['category_id'])== (cmpVideosCategoryID(catalog, category))):
            lt.addLast(BestVideos['videos'], element)
    return BestVideos

def modeloR2(catalog,country):
    BestVideos = newCatalog()
    for pos in range(0, int(lt.size(catalog['videos']))):
        element = lt.getElement(catalog['videos'], pos)
        if element['country'] == country:
            lt.addLast(BestVideos['videos'], element)
    return BestVideos

def modeloR3(catalog,category):
    BestVideos = newCatalog()
    for pos in range(0, int(lt.size(catalog['videos']))):
        element = lt.getElement(catalog['videos'], pos)
        if int(element['category_id']) == (cmpVideosCategoryID(catalog, category)):
            lt.addLast(BestVideos['videos'], element)
    return BestVideos

def modeloR4(catalog,country,tag):
    BestVideos = newCatalog()
    for pos in range(0, int(lt.size(catalog['videos']))):
        element = lt.getElement(catalog['videos'], pos)
        if element['country'] == country and cmpVideosTags(catalog,element, tag)== True:
            
            lt.addLast(BestVideos['videos'], element)
                

    return BestVideos

# Funciones para agregar informacion al catalogo

def addVideo(catalog,video):
    lt.addLast(catalog['videos'], video)


def addCategoryID(catalog, category):
    t = newCategoryID(category['name'], category['id'])
    lt.addLast(catalog['categories'], t)

# Funciones para creacion de datos

def newCategoryID(name, id):
    category = {'name':'', 'id': ''}
    category['name'] = name
    category['id'] = id
    return category

def newVideoCategory(category_id, video_id):
    videocategory = {'category_id': category_id, 'video_id': video_id}
    return videocategory


# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByLikes(video1,video2):
    if float(video1['likes']) > float(video2['likes']):
        return True
    else:
        return False


def cmpVideosByViews(video1, video2):
    if float(video1['views']) > float(video2['views']):
        return True
    else:
        return False

def cmpVideosByName(video1, video2):
    if video1['title'] > video2['title']:
        return True
    else:
        return False
  

def cmpVideosCategoryID(catalog,category):
    size = lt.size(catalog['categories'])
    i = 0
    centinela = False
    while i <= size and centinela == False:
        cat = lt.getElement(catalog['categories'], i)
        if cat['name'].lower() == (' '+category):
            respuesta = int(cat['id'])
            centinela = True
        i += 1
    return respuesta
    
def cmpVideosTags(catalog,element, tag):
    respuesta = False
    taglist = element['tags'].split('|')
    i = 0
    while i < len(taglist) and respuesta == False:
        t = taglist[i].find(tag)
        if t != (-1):
            respuesta = True
        i += 1
    return respuesta

def cmpVideosByID(video1, video2):
    if (video1['video_id']) < (video2['video_id']):
        return True
    else:
        return False

def repForID(catalog, video, firstpos):
    reps = 0
    pos = firstpos
    while pos <= lt.size(catalog):
        cmpvideo = lt.getElement(catalog, pos)
        if cmpvideo['video_id'] == video:
            reps += 1
        else:
            break
        pos += 1
    return reps

def cmpNumByID(catalog):
    bestvideo = None
    bestreps = 0
    cmpvideo = None
    cmpreps = 0
    pos = 1
    while pos <= lt.size(catalog):
        cmpvideo = lt.getElement(catalog, pos)
        cmpreps = repForID(catalog, cmpvideo['video_id'], pos)
        if cmpreps > bestreps:
            bestvideo = lt.getElement(catalog, pos)
            bestreps = cmpreps
        pos += cmpreps
    return (bestvideo,bestreps)

def repForName(catalog, video, pos):
    reps = 0
    while pos <= lt.size(catalog):
        cmpvideo = lt.getElement(catalog,pos)
        if cmpvideo['title'] == video:
            reps += 1
        else:
            break
        pos += 1
    return reps


def cmpNumByName(catalog):
    bestvideo = None
    bestreps = 0
    cmpvideo= None
    cmpreps = 0
    pos = 1
    while pos <= lt.size(catalog):
        cmpvideo = lt.getElement(catalog, pos)
        cmpreps = repForName(catalog, cmpvideo['title'], pos)
        if cmpreps > bestreps:
            bestvideo = cmpvideo
            bestreps = cmpreps
        pos += 1
    return (bestvideo,bestreps)
        
# Funciones de ordenamiento

def sortVideos(catalog,size):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    sorted_list = mer.sort(sub_list, cmpVideosByViews)
    return sorted_list

def sortVideosR2(catalog,size):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    sorted_list = mer.sort(sub_list, cmpVideosByID)
    return sorted_list

def sortVideosR3(catalog, size):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    sorted_list = mer.sort(sub_list, cmpVideosByName)
    return sorted_list

def sortVideosR4(catalog, size):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    sorted_list = mer.sort(sub_list, cmpVideosByLikes)
    return sorted_list