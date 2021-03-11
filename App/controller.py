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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de Videos

def initCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategoryID(catalog)
    

def loadVideos(catalog):
    videosfile = cf.data_dir + 'Videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding= 'utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategoryID(catalog):
    categoryidfile = cf.data_dir + 'Videos/category-id.csv'

    input_file = csv.DictReader(open(categoryidfile, encoding='utf-8'),delimiter= '\t')
    for category in input_file:
        model.addCategoryID(catalog,category)
        
# Funciones de ordenamiento

def sortVideosR1(catalog, size, category, country):
    """
    Ordena los libros por average_rating
    """
    BestVideos = model.modeloR1(catalog, category, country)
    size2 = lt.size(BestVideos['videos'])
    return model.sortVideos(BestVideos, int(size2))
    
def sortVideosR2(catalog,size, country):
    BestVideos = model.modeloR2(catalog,country)
    size2 = lt.size(BestVideos['videos'])
    list_sorted = model.sortVideosR2(BestVideos, int(size2))
    mayor = model.cmpNumByID(list_sorted)
    return mayor

def sortVideosR3(catalog,size, category):
    BestVideos = model.modeloR3(catalog,category)
    size2 = lt.size(BestVideos['videos'])
    list_sorted = model.sortVideosR3(BestVideos, int(size2))
    mayor = model.cmpNumByName(list_sorted)
    return mayor

def sortVideosR4(catalog, size, tag, country):
    BestVideos = model.modeloR4(catalog, country, tag)
    size2 = lt.size(BestVideos['videos'])
    list_sorted = model.sortVideosR4(BestVideos, int(size2))
    return list_sorted
    
# Funciones de consulta sobre el catálogo

