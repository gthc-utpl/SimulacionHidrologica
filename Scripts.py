# import necessary libraries
import pandas as pd
import os
import glob
import datetime
import datetime as dt
import processing   
import qgis.core
import qgis.analysis
import sys
import os
import shutil
import netCDF4
import re
import numpy as np
from qgis.core import QgsProcessing
from qgis.core import QgsVectorLayer, QgsVectorFileWriter, QgsRasterLayer
from qgis.core import QgsProject
from qgis.core import QgsProcessingFeedback
from qgis.core import QgsCoordinateReferenceSystem
from PyQt5.QtCore import QVariant
from qgis.utils import iface
from osgeo import gdal
from PyQt5 import QtWidgets

#Eliminala las carpetas en caso de volver a ejecutar el algoritmo 

if os.path.exists("C:/Qgis/Results"):
    shutil.rmtree("C:/Qgis/Results")

if os.path.exists("C:/Qgis/Shapes"):
    shutil.rmtree("C:/Qgis/Shapes")

if os.path.exists("C:/Qgis/Calculado"):
    shutil.rmtree("C:/Qgis/Calculado")
    
if os.path.exists("C:/Qgis/Calculado ETA"):
    shutil.rmtree("C:/Qgis/Calculado ETA")

if os.path.exists("C:/Qgis/Interpolado"):
    shutil.rmtree("C:/Qgis/Interpolado")

if os.path.exists("C:/Qgis/Datos"):
    shutil.rmtree("C:/Qgis/Datos")

if os.path.exists("C:/Qgis/Interpolado ETA"):
    shutil.rmtree("C:/Qgis/Interpolado ETA")

if os.path.exists("C:/Qgis/Precipitacion"):
    shutil.rmtree("C:/Qgis/Precipitacion")

if os.path.exists("C:/Qgis/Evapotranspiracion"):
    shutil.rmtree("C:/Qgis/Evapotranspiracion")
    
if os.path.exists("C:/Qgis/Calculos/Pn"):
    shutil.rmtree("C:/Qgis/Calculos/Pn")
    
if os.path.exists("C:/Qgis/Calculos/En"):
    shutil.rmtree("C:/Qgis/Calculos/En")

if os.path.exists("C:/Qgis/Calculos/Ps"):
    shutil.rmtree("C:/Qgis/Calculos/Ps")
    
if os.path.exists("C:/Qgis/Calculos/Es"):
    shutil.rmtree("C:/Qgis/Calculos/Es")

if os.path.exists("C:/Qgis/Calculos/sX1(B)"):
    shutil.rmtree("C:/Qgis/Calculos/sX1(B)")

if os.path.exists("C:/Qgis/Calculos/Prec"):
    shutil.rmtree("C:/Qgis/Calculos/Prec")

if os.path.exists("C:/Qgis/Calculos/sX1(C)"):
    shutil.rmtree("C:/Qgis/Calculos/sX1(C)")

if os.path.exists("C:/Qgis/Calculos/Pr"):
    shutil.rmtree("C:/Qgis/Calculos/Pr")

if os.path.exists("C:/Qgis/Calculos/V23"):
    shutil.rmtree("C:/Qgis/Calculos/V23")
    
if os.path.exists("C:/Qgis/Calculos/V22"):
    shutil.rmtree("C:/Qgis/Calculos/V22")

if os.path.exists("C:/Qgis/Calculos/V21"):
    shutil.rmtree("C:/Qgis/Calculos/V21")

if os.path.exists("C:/Qgis/Calculos/V12"):
    shutil.rmtree("C:/Qgis/Calculos/V12")

if os.path.exists("C:/Qgis/Calculos/V11"):
    shutil.rmtree("C:/Qgis/Calculos/V11")

if os.path.exists("C:/Qgis/Calculos/V13"):
    shutil.rmtree("C:/Qgis/Calculos/V13")

if os.path.exists("C:/Qgis/Calculos/V14"):
    shutil.rmtree("C:/Qgis/Calculos/V14")

if os.path.exists("C:/Qgis/Calculos/V15"):
    shutil.rmtree("C:/Qgis/Calculos/V15")

if os.path.exists("C:/Qgis/Calculos/V16"):
    shutil.rmtree("C:/Qgis/Calculos/V16")

if os.path.exists("C:/Qgis/Calculos/V17"):
    shutil.rmtree("C:/Qgis/Calculos/V17")

if os.path.exists("C:/Qgis/Calculos/V18"):
    shutil.rmtree("C:/Qgis/Calculos/V18")

if os.path.exists("C:/Qgis/Calculos/V19"):
    shutil.rmtree("C:/Qgis/Calculos/V19")

if os.path.exists("C:/Qgis/Calculos/V110"):
    shutil.rmtree("C:/Qgis/Calculos/V110")

if os.path.exists("C:/Qgis/Calculos/V24"):
    shutil.rmtree("C:/Qgis/Calculos/V24")

if os.path.exists("C:/Qgis/Calculos/V25"):
    shutil.rmtree("C:/Qgis/Calculos/V25")

if os.path.exists("C:/Qgis/Calculos/V26"):
    shutil.rmtree("C:/Qgis/Calculos/V26")

if os.path.exists("C:/Qgis/Calculos/V27"):
    shutil.rmtree("C:/Qgis/Calculos/V27")

if os.path.exists("C:/Qgis/Calculos/V28"):
    shutil.rmtree("C:/Qgis/Calculos/V28")

if os.path.exists("C:/Qgis/Calculos/V29"):
    shutil.rmtree("C:/Qgis/Calculos/V29")

if os.path.exists("C:/Qgis/Calculos/V210"):
    shutil.rmtree("C:/Qgis/Calculos/V210")

if os.path.exists("C:/Qgis/Calculos/V211"):
    shutil.rmtree("C:/Qgis/Calculos/V211")

if os.path.exists("C:/Qgis/Calculos/V212"):
    shutil.rmtree("C:/Qgis/Calculos/V212")

if os.path.exists("C:/Qgis/Calculos/V213"):
    shutil.rmtree("C:/Qgis/Calculos/V213")

if os.path.exists("C:/Qgis/Calculos/V214"):
    shutil.rmtree("C:/Qgis/Calculos/V214")

if os.path.exists("C:/Qgis/Calculos/V215"):
    shutil.rmtree("C:/Qgis/Calculos/V215")

if os.path.exists("C:/Qgis/Calculos/V216"):
    shutil.rmtree("C:/Qgis/Calculos/V216")

if os.path.exists("C:/Qgis/Calculos/V217"):
    shutil.rmtree("C:/Qgis/Calculos/V217")

if os.path.exists("C:/Qgis/Calculos/V218"):
    shutil.rmtree("C:/Qgis/Calculos/V218")

if os.path.exists("C:/Qgis/Calculos/V219"):
    shutil.rmtree("C:/Qgis/Calculos/V219")

if os.path.exists("C:/Qgis/Calculos/V220"):
    shutil.rmtree("C:/Qgis/Calculos/V220")

if os.path.exists("C:/Qgis/Calculos/rX3(B)"):
    shutil.rmtree("C:/Qgis/Calculos/rX3(B)")

if os.path.exists("C:/Qgis/Calculos/Qr"):
    shutil.rmtree("C:/Qgis/Calculos/Qr")

if os.path.exists("C:/Qgis/Calculos/rX3(C)"):
    shutil.rmtree("C:/Qgis/Calculos/rX3(C)")

if os.path.exists("C:/Qgis/Calculos/Qd"):
    shutil.rmtree("C:/Qgis/Calculos/Qd")

if os.path.exists("C:/Qgis/Calculos/Q"):
    shutil.rmtree("C:/Qgis/Calculos/Q")

if os.path.exists("C:/Qgis/Calculos/Debit"):
    shutil.rmtree("C:/Qgis/Calculos/Debit")
    
if os.path.exists("C:/Qgis/netCDFiles"):
    shutil.rmtree("C:/Qgis/netCDFiles")

if os.path.exists("C:/Qgis/Calculos/Combinado"):
    shutil.rmtree("C:/Qgis/Calculos/Combinado")
    
# De no realizar este proceso existira un error
try:
    #Crear carpetas en el Disco Local para almacenar los datos 
    os.makedirs("C:/Qgis/Results")
    os.makedirs("C:/Qgis/Shapes")
    os.makedirs("C:/Qgis/Calculado")
    os.makedirs("C:/Qgis/Datos")
    os.makedirs("C:/Qgis/Calculado ETA")
    os.makedirs("C:/Qgis/Interpolado")
    os.makedirs("C:/Qgis/Interpolado ETA")
    os.makedirs("C:/Qgis/Precipitacion")
    os.makedirs("C:/Qgis/Evapotranspiracion")
    os.makedirs("C:/Qgis/Calculos/Pn")
    os.makedirs("C:/Qgis/Calculos/En")
    os.makedirs("C:/Qgis/Calculos/Ps")
    os.makedirs("C:/Qgis/Calculos/Es")
    os.makedirs("C:/Qgis/Calculos/sX1(B)")
    os.makedirs("C:/Qgis/Calculos/Prec")
    os.makedirs("C:/Qgis/Calculos/sX1(C)")
    os.makedirs("C:/Qgis/Calculos/Pr")
    os.makedirs("C:/Qgis/Calculos/V23")
    os.makedirs("C:/Qgis/Calculos/V22")
    os.makedirs("C:/Qgis/Calculos/V21")
    os.makedirs("C:/Qgis/Calculos/V12")
    os.makedirs("C:/Qgis/Calculos/V11")
    os.makedirs("C:/Qgis/Calculos/V13")
    os.makedirs("C:/Qgis/Calculos/V14")
    os.makedirs("C:/Qgis/Calculos/V15")
    os.makedirs("C:/Qgis/Calculos/V16")
    os.makedirs("C:/Qgis/Calculos/V17")
    os.makedirs("C:/Qgis/Calculos/V18")
    os.makedirs("C:/Qgis/Calculos/V19")
    os.makedirs("C:/Qgis/Calculos/V110")
    os.makedirs("C:/Qgis/Calculos/V24")
    os.makedirs("C:/Qgis/Calculos/V25")
    os.makedirs("C:/Qgis/Calculos/V26")
    os.makedirs("C:/Qgis/Calculos/V27")
    os.makedirs("C:/Qgis/Calculos/V28")
    os.makedirs("C:/Qgis/Calculos/V29")
    os.makedirs("C:/Qgis/Calculos/V210")
    os.makedirs("C:/Qgis/Calculos/V211")
    os.makedirs("C:/Qgis/Calculos/V212")
    os.makedirs("C:/Qgis/Calculos/V213")
    os.makedirs("C:/Qgis/Calculos/V214")
    os.makedirs("C:/Qgis/Calculos/V215")
    os.makedirs("C:/Qgis/Calculos/V216")
    os.makedirs("C:/Qgis/Calculos/V217")
    os.makedirs("C:/Qgis/Calculos/V218")
    os.makedirs("C:/Qgis/Calculos/V219")
    os.makedirs("C:/Qgis/Calculos/V220")
    os.makedirs("C:/Qgis/Calculos/rX3(B)")
    os.makedirs("C:/Qgis/Calculos/Qr")
    os.makedirs("C:/Qgis/Calculos/rX3(C)")
    os.makedirs("C:/Qgis/Calculos/Qd")
    os.makedirs("C:/Qgis/Calculos/Q")
    os.makedirs("C:/Qgis/Calculos/Debit")
    os.makedirs("C:/Qgis/netCDFiles")
    
    #Rango de Fecha Inicial
    fecha_inicio = QInputDialog().getText(None,"Rango de Fecha","Fecha Inicio")
    #Rango de Fecha Final 
    fecha_fin = QInputDialog().getText(None,"Rango de Fecha","Fecha Fin")
    #Codigo para convertir los datos en formato de fecha (Año - Mes- Dia)
    start = datetime.datetime.strptime(fecha_inicio[0], "%Y-%m-%d")
    end = datetime.datetime.strptime(fecha_fin[0], "%Y-%m-%d")

    date_generated = pd.date_range(start, end)

    #Se abre el explorador de archivos para seleccionar la carpeta que contiene los datos de estaciones 
    #Lugar donde se almacenan los los archivos Excel
    print('Seleccione la carpeta con los datos de estaciones')
    path = QFileDialog.getExistingDirectory()

    #Recoleta todos los archivos xlsx
    csv_files = glob.glob(os.path.join(path, "*.xlsx"))

    #Crea un solo archivo que combina todos los datos 
    combinado_csv = pd.concat([pd.read_excel(f) for f in csv_files ])

    #Crea todos los datos en formato CSV
    for i, valor in enumerate(date_generated):
        filtered_df = combinado_csv.loc[(combinado_csv['Fecha'] == valor)]
        filtered_df.to_csv('C:\Qgis\Datos\Datos-{}.csv'.format(valor.strftime("%Y-%m-%d")))

    print('Archivos Creados')
    
    #Ingreso por parte del usuario de los archivos DEM y de Coordenadas
    print('Seleccione el archivo DEM')
    filedem = QFileDialog.getOpenFileName()
    dem = filedem[0]
    rasterDEM = QgsRasterLayer(dem,"DEM")
    rasterDEM.isValid()
    print('Seleccione el archivo con las coordenadas de las estaciones')
    coordenates = QFileDialog.getOpenFileName()
    coordenatesfile = coordenates[0]
    rasterLyr = QgsVectorLayer(coordenatesfile, "Datos Estaciones")
    rasterLyr.isValid()
    
    # Fill Sinks (Wang & Liu)
    parameters = {
                'ELEV': rasterDEM,
                'MINSLOPE': 0.1,
                'FDIR': QgsProcessing.TEMPORARY_OUTPUT,
                'FILLED': "C:/Qgis/Results/FilledDem.sdat",
                'WSHED':QgsProcessing.TEMPORARY_OUTPUT,
            }

    processing.run('saga:fillsinkswangliu',parameters)

    # Delimitar Cuenca - Olla mayor 
    parameters = {
                '-4': False,
                '-a': False,
                '-b': False,
                '-m': True,
                '-s': True,
                'GRASS_RASTER_FORMAT_META': '',
                'GRASS_RASTER_FORMAT_OPT': '',
                'GRASS_REGION_CELLSIZE_PARAMETER': 0,
                'GRASS_REGION_PARAMETER': None,
                'blocking': None,
                'convergence': 5,
                'depression': None,
                'disturbed_land': None,
                'elevation': "C:/Qgis/Results/FilledDem.sdat",
                'flow': None,
                'max_slope_length': 0,
                'memory': 300,
                'threshold': 25000,
                'basin': "C:/Qgis/Results/Olla.sdat"
            }
            
    processing.run('grass7:r.watershed',parameters)

    # Delimitar Cuenca - Subcuencas 
    parameters = {
                '-4': False,
                '-a': False,
                '-b': False,
                '-m': False,
                '-s': False,
                'GRASS_RASTER_FORMAT_META': '',
                'GRASS_RASTER_FORMAT_OPT': '',
                'GRASS_REGION_CELLSIZE_PARAMETER': 0,
                'GRASS_REGION_PARAMETER': None,
                'blocking': None,
                'convergence': 5,
                'depression': None,
                'disturbed_land': None,
                'elevation': "C:/Qgis/Results/FilledDem.sdat",
                'flow': None,
                'max_slope_length': 0,
                'memory': 300,
                'threshold': 10000,
                'basin': "C:/Qgis/Results/Subcuencas.sdat"
            }
            
    processing.run('grass7:r.watershed',parameters)

    # Convertir a Vector - Olla
    parameters = {
                '-b': False,
                '-s': True,
                '-t': False,
                '-v': False,
                '-z': False,
                'GRASS_OUTPUT_TYPE_PARAMETER': 0,  # auto
                'GRASS_REGION_CELLSIZE_PARAMETER': 0,
                'GRASS_REGION_PARAMETER': None,
                'GRASS_VECTOR_DSCO': '',
                'GRASS_VECTOR_EXPORT_NOCAT': False,
                'GRASS_VECTOR_LCO': '',
                'column': 'value',
                'input': "C:/Qgis/Results/Olla.sdat",
                'type': 2,  # area
                'output': "C:/Qgis/Results/OllaVector.shp"
            }
            
    processing.run('grass7:r.to.vect',parameters)

    # Convertir a Vector - Subcuencas
    parameters = {
                '-b': False,
                '-s': True,
                '-t': False,
                '-v': False,
                '-z': False,
                'GRASS_OUTPUT_TYPE_PARAMETER': 0,  # auto
                'GRASS_REGION_CELLSIZE_PARAMETER': 0,
                'GRASS_REGION_PARAMETER': None,
                'GRASS_VECTOR_DSCO': '',
                'GRASS_VECTOR_EXPORT_NOCAT': False,
                'GRASS_VECTOR_LCO': '',
                'column': 'value',
                'input': "C:/Qgis/Results/Subcuencas.sdat",
                'type': 2,  # area
                'output': "C:/Qgis/Results/subCuencaVector.shp"
            }
            
    processing.run('grass7:r.to.vect',parameters)

    # Cortar Cuencas Olla
    parameters = {
                'INPUT': "C:/Qgis/Results/subCuencaVector.shp",
                'OVERLAY': "C:/Qgis/Results/OllaVector.shp",
                'OUTPUT': "C:/Qgis/Results/Cuencas.shp"
            }
            
    processing.run('native:clip',parameters)

    Cuencas = QgsVectorLayer("C:/Qgis/Results/Cuencas.shp", "Cuencas")
    QgsProject.instance().addMapLayer(Cuencas)

    print('Cuenca Delimitada')

    #Crear puntos a partir de tabla 
    parameters ={
                'INPUT': rasterLyr,
                'MFIELD': '',
                'TARGET_CRS': QgsCoordinateReferenceSystem('EPSG:24877'),
                'XFIELD': 'UTMX',
                'YFIELD': 'UTMY',
                'ZFIELD': '',
                'OUTPUT': "C:/Qgis/Results/Estaciones.shp"
                }
    processing.run('native:createpointslayerfromtable',parameters)

    Estaciones = QgsVectorLayer("C:/Qgis/Results/Estaciones.shp", "Estaciones")
    QgsProject.instance().addMapLayer(Estaciones)

    print('Coordenadas Creadas')

    # Unir los puntos de coordenadas con datos de precipitacion 
    path = "C:\Qgis\Datos"

    outPath = "C:\Qgis\Shapes"

    list_files = os.listdir(path)

    extension = ".csv"

    outprefix = '_Union'


    for f in list_files:
         if os.path.splitext(f)[1] == extension:
             abs_path = path+"/"+f
             ex_path = f.rstrip(".csv")
             layer = iface.addVectorLayer(abs_path, os.path.splitext(f)[0], 'ogr')
             parameters = {
                        'DISCARD_NONMATCHING': False,
                        'FIELD': 'Estacion',
                        'FIELDS_TO_COPY': [''],
                        'FIELD_2': 'Estacion',
                        'INPUT':"C:/Qgis/Results/Estaciones.shp",
                        'INPUT_2': layer,
                        'METHOD': 1,  # Tomar solo los atributos del primer objeto coincidente (uno a uno)
                        'PREFIX': '',
                        'OUTPUT': os.path.join(outPath, "{1}{0}.shp".format(outprefix, ex_path)) }
             processing.run('native:joinattributestable',parameters)
             QgsProject.instance().removeMapLayer(layer)

    #Calculo de la Precipitacion 
    pathShapes = "C:\Qgis\Shapes"
    list_shapes = os.listdir(pathShapes)

    outPathCalculado = "C:\Qgis\Calculado"

    outprefix = '_CalculadoP'
    extensionShape = ".shp"
    for i in list_shapes:
         if os.path.splitext(i)[1] == extensionShape:
             abs_path = pathShapes+"/"+i
             ex_path = i.rstrip("_Union.shp")
             layer = iface.addVectorLayer(abs_path, os.path.splitext(i)[0], 'ogr')
             parameters = {
                'FIELD_LENGTH': 1000,
                'FIELD_NAME': 'Precipitacion ',
                'FIELD_PRECISION': 3,
                'FIELD_TYPE': 1,#Entero
                'FORMULA': ' "P" ',
                'INPUT':layer,
                'OUTPUT':os.path.join(outPathCalculado, "{1}{0}.shp".format(outprefix, ex_path))
                }
             processing.run('native:fieldcalculator',parameters)
             QgsProject.instance().removeMapLayer(layer)
        

    #Calculo de la EvapoTranspiracion 
    pathShapesETA = "C:\Qgis\Shapes"
    list_shapesETA = os.listdir(pathShapesETA)

    outPathCalculadoETA = "C:\Qgis\Calculado ETA"

    outprefixETA = '_CalculadoETA'
    extensionShapeETA = ".shp"
    for i in list_shapesETA:
         if os.path.splitext(i)[1] == extensionShapeETA:
             abs_path = pathShapesETA+"/"+i
             ex_path = i.rstrip("_Union.shp")
             layer = iface.addVectorLayer(abs_path, os.path.splitext(i)[0], 'ogr')
             parameters = {
                'FIELD_LENGTH': 1000,
                'FIELD_NAME': 'Precipitacion ',
                'FIELD_PRECISION': 3,
                'FIELD_TYPE': 1,#Entero
                'FORMULA': ' "ET" ',
                'INPUT':layer,
                'OUTPUT':os.path.join(outPathCalculadoETA, "{1}{0}.shp".format(outprefixETA, ex_path))
                }
             processing.run('native:fieldcalculator',parameters)
             QgsProject.instance().removeMapLayer(layer)


    # Interpolado Precipitacion
    pathInterpolado  = "C:\Qgis\Calculado"
    list_idw = os.listdir(pathInterpolado)
    outPathIDW = "C:\Qgis\Interpolado"
    outprefix = '_InterpoladoP'
    extensionIDW = ".shp"
    rulesIDW = "::~::0::~::9::~::0"
    for i in list_idw:
         if os.path.splitext(i)[1] == extensionIDW:
             abs_path = pathInterpolado+"/"+i
             dir_path = pathInterpolado+"/"+i+rulesIDW
             ex_path = i.rstrip("_CalculadoP.shp")
             #layer = iface.addVectorLayer(abs_path, os.path.splitext(i)[0], 'ogr')
             parameters = {
                'DISTANCE_COEFFICIENT': 2,
                'EXTENT': '681273.100000000,727871.840000000,9517836.000000000,9599684.000000000 [EPSG:24877]',
                'INTERPOLATION_DATA': dir_path,
                'PIXEL_SIZE': 50,
                'OUTPUT': os.path.join(outPathIDW, "{1}{0}.shp".format(outprefix, ex_path))
                }
             processing.run('qgis:idwinterpolation',parameters)
             #QgsProject.instance().removeMapLayer(layer)


    # Interpolado Evapotranspiracion
    pathInterpoladoETA  = "C:\Qgis\Calculado ETA"
    list_idwETA = os.listdir(pathInterpoladoETA)
    outPathIDW_ETA = "C:\Qgis\Interpolado ETA"
    outprefix_ETA = '_InterpoladoETA'
    extensionIDW_ETA = ".shp"
    rulesIDW_ETA = "::~::0::~::9::~::0"
    for i in list_idwETA:
         if os.path.splitext(i)[1] == extensionIDW_ETA:
             abs_path = pathInterpoladoETA+"/"+i
             dir_path = pathInterpoladoETA+"/"+i+rulesIDW_ETA
             ex_path = i.rstrip("_CalculadoETA.shp")
             #layer = iface.addVectorLayer(abs_path, os.path.splitext(i)[0], 'ogr')
             parameters = {
                'DISTANCE_COEFFICIENT': 2,
                'EXTENT': '681273.100000000,727871.840000000,9517836.000000000,9599684.000000000 [EPSG:24877]',
                'INTERPOLATION_DATA': dir_path,
                'PIXEL_SIZE': 50,
                'OUTPUT': os.path.join(outPathIDW_ETA, "{1}{0}.shp".format(outprefix_ETA, ex_path))
                }
             processing.run('qgis:idwinterpolation',parameters)
             #QgsProject.instance().removeMapLayer(layer)

    #Cortado Raster en base a Cuenca - Precipitacion 
    pathCortadoInterpolado  = "C:\Qgis\Interpolado"
    list_cortadoIDW = os.listdir(pathCortadoInterpolado)
    outPathCortadoIDW = "C:\Qgis\Precipitacion"
    outprefix = '_Precipitación'
    extensionCortadoIDW = ".shp"

    for i in list_cortadoIDW:
        if os.path.splitext(i)[1] == extensionCortadoIDW:
            abs_path = pathCortadoInterpolado+"/"+i
            ex_path = i.rstrip("_InterpoladoP.shp")
            #layer = iface.addVectorLayer(abs_path, os.path.splitext(i)[0], 'ogr')
            parameters = {
                'ALPHA_BAND': False,
                'CROP_TO_CUTLINE': True,
                'DATA_TYPE': 0,  # Usar el tipo de datos de la capa de entrada
                'EXTRA': '',
                'INPUT': abs_path,
                'KEEP_RESOLUTION': True,
                'MASK': "C:/Qgis/Results/Cuencas.shp",
                'MULTITHREADING': False,
                'NODATA': None,
                'OPTIONS': '',
                'SET_RESOLUTION': False,
                'SOURCE_CRS': None,
                'TARGET_CRS': None,
                'X_RESOLUTION': None,
                'Y_RESOLUTION': None,
                'OUTPUT': os.path.join(outPathCortadoIDW, "{1}{0}.tif".format(outprefix, ex_path))
            }
            processing.runAndLoadResults('gdal:cliprasterbymasklayer',parameters)

    print('Interpolado de Precipitación')

    #Cortado Raster en base a Cuenca - Evapotranspiración
    pathCortadoInterpoladoETA  = "C:\Qgis\Interpolado ETA"
    list_cortadoIDW_ETA = os.listdir(pathCortadoInterpoladoETA)
    outPathCortadoIDW_ETA = "C:\Qgis\Evapotranspiracion"
    outprefix_ETA = '_Evapotranspiracion'
    extensionCortadoIDW_ETA = ".shp"

    for i in list_cortadoIDW_ETA:
        if os.path.splitext(i)[1] == extensionCortadoIDW_ETA:
            abs_path = pathCortadoInterpoladoETA+"/"+i
            ex_path = i.rstrip("_InterpoladoETA.shp")
            #layer = iface.addVectorLayer(abs_path, os.path.splitext(i)[0], 'ogr')
            parameters = {
                'ALPHA_BAND': False,
                'CROP_TO_CUTLINE': True,
                'DATA_TYPE': 0,  # Usar el tipo de datos de la capa de entrada
                'EXTRA': '',
                'INPUT': abs_path,
                'KEEP_RESOLUTION': True,
                'MASK': "C:/Qgis/Results/Cuencas.shp",
                'MULTITHREADING': False,
                'NODATA': None,
                'OPTIONS': '',
                'SET_RESOLUTION': False,
                'SOURCE_CRS': None,
                'TARGET_CRS': None,
                'X_RESOLUTION': None,
                'Y_RESOLUTION': None,
                'OUTPUT': os.path.join(outPathCortadoIDW_ETA, "{1}{0}.tif".format(outprefix_ETA, ex_path))
            }
            processing.runAndLoadResults('gdal:cliprasterbymasklayer',parameters)

    print('Interpolado de Evapotranspiración')
    
    # Calculos LLuvia - Escorrentia 
    print('Calculos matemáticos')

    #Acceso a los archivos para realizar los calculos
    pathQgis = 'C:/Qgis'
    parthDirection= 'C:/Qgis/Calculos'

    #Pedir datos 
    soX1 = QInputDialog().getText(None,"S0/X1","Tasa Incial de Relleno")
    roX3 = QInputDialog().getText(None,"R0/x3","Tasa Incial de Reemplazo")
    x1 = QInputDialog().getText(None,"X1","Capacidad de Produccion")
    x2 = QInputDialog().getText(None,"X2","Parametro de intercambio")
    x3 = QInputDialog().getText(None,"X3","Capacidad de Ruteo")
    x4 = QInputDialog().getText(None,"X4","Tiempo de retrazo")

    prec = glob.glob(os.path.join(pathQgis+"/Precipitacion", "*.tif"))
    eta = glob.glob(os.path.join(pathQgis+"/Evapotranspiracion", "*.tif"))


    outprefixPn = '_Pn'
    outprefixEn = '_En'
    for valor_a, valor_b in zip(prec,eta):
        ex_path = valor_a.rstrip("_Precipitación.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Precipitacion')
        finalpath = parthDirection +"/Pn"+temp_path
        finalpathEn = parthDirection +"/En"+temp_path
        #Pn
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '(A>=B)* (A-B)+ (A<B)*0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/Pn", "{1}{0}.tif".format(outprefixPn,finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)
        #En
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '(A<B)* (B-A)+ (B>A)*0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/En", "{1}{0}.tif".format(outprefixEn,finalpathEn))
                }
        processing.run('gdal:rastercalculator',parameters)

    print('Calculando..')
    pN = glob.glob(os.path.join(parthDirection+"/Pn", "*.tif"))
    eN = glob.glob(os.path.join(parthDirection+"/En", "*.tif"))

    outprefixPs = '_Ps'
    outprefixEs = '_Es'
    for valor_a, valor_b in zip(pN,eN):
        ex_path = valor_a.rstrip("_Pn.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/Pn')
        finalpath = parthDirection+"/Ps" + temp_path
        formula = "(A>0)* ("+x1[0]+"*(1-"+soX1[0]+"*"+soX1[0]+")*tan(A/"+x1[0]+")/1+B*tan(A/"+x1[0]+"))+ (A<0)*0"
        finalpathEs = parthDirection+"/Es" + temp_path
        formulaEs = "(B>0)* ("+soX1[0]+"*("+x1[0]+")*(2-"+soX1[0]+")*tan(B/"+x1[0]+")/1+(1-"+soX1[0]+")*tan(B/"+soX1[0]+"))+ (A<0)*0"
        #Ps
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA':formula,
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/Ps", "{1}{0}.tif".format(outprefixPs,finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)
        #Es
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA':formulaEs,
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/Es", "{1}{0}.tif".format(outprefixEs,finalpathEs))
                }
        processing.run('gdal:rastercalculator',parameters)

    print('Calculando..')
    pS = glob.glob(os.path.join(parthDirection+"/Ps", "*.tif"))
    eS = glob.glob(os.path.join(parthDirection+"/Es", "*.tif"))

    outprefixsX1 = '_sX(B)'

    for valor_a, valor_b in zip(pS,eS):
        ex_path = valor_a.rstrip("_Ps.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/Ps')
        finalpath = parthDirection+"/sX1(B)" + temp_path
        formula = "("+soX1[0]+"+(A-B)/"+x1[0]+")"
        #sX1
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA':formula,
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/sX1(B)", "{1}{0}.tif".format(outprefixsX1,finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)
        
    print('Calculando..')
    sX1B = glob.glob(os.path.join(parthDirection+"/sX1(B)", "*.tif"))

    outprefixprec = '_prec'

    for valor_a in sX1B:
        ex_path = valor_a.rstrip("_sX(B).tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/sX1(B)')
        finalpath = parthDirection+"/Prec" + temp_path
        formula = "((A*"+x1[0]+")*(1-(1+(4/9*A)*4))*(-0.25))"
        #prec
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_a,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA':formula,
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/Prec", "{1}{0}.tif".format(outprefixprec,finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)
        
    print('Calculando..')
    pres = glob.glob(os.path.join(parthDirection+"/Prec", "*.tif"))
    outprefix1C = '_sX(C)'
    for valor_a, valor_b in zip(pres,sX1B):
        ex_path = valor_a.rstrip("_prec.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/Prec')
        finalpath = parthDirection+"/sX1(C)" + temp_path
        formula = "B-A/"+x1[0]+""
        #sx1C
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA':formula,
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join( parthDirection+"/sX1(C)", "{1}{0}.tif".format(outprefix1C,finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)
        
    outprefixPr = '_pr'
    print('Calculando..')
    for valor_a, valor_b, valor_c in zip(pres,pN,pS):
        ex_path = valor_a.rstrip("_prec.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/Prec')
        finalpath = parthDirection+"/Pr" + temp_path
        #Pr
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': valor_c,
                'BAND_C': 1,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': 'A+(B-C)',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/Pr", "{1}{0}.tif".format(outprefixPr,finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)
        
    pr = glob.glob(os.path.join(parthDirection+"/Pr", "*.tif"))

    print('Calculando..')
    outprefixV12 = '_v12'

    for valor_a in pr:
        ex_path = valor_a.rstrip("_pr.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/Pr')
        finalpathV12 = parthDirection+"/V12" + temp_path
        #V12
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': 'A*0.9*0.56',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V12", "{1}{0}.tif".format(outprefixV12,finalpathV12))
                }
        processing.run('gdal:rastercalculator',parameters)

    v12 = glob.glob(os.path.join(parthDirection+"/V12", "*.tif"))
    outprefixV11 = '_v'
    print('Calculando..')
    for valor_a, valor_b in zip(pr,v12):
        ex_path = valor_a.rstrip("_pr.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/Pr')
        finalpathV11 = parthDirection+"/V11" + temp_path
        #V11
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': 'A*0.9*0.56',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V11", "{1}{0}.tif".format(outprefixV11,finalpathV11))
                }
        processing.run('gdal:rastercalculator',parameters)


    outprefixV23 = '_v23'
    print('Calculando..')
    for valor_a in pr:
        ex_path = valor_a.rstrip("_pr.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/Pr')
        finalpathV23 = parthDirection+"/V23" + temp_path
        #V23
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '(A*0.1*0.12)',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V23", "{1}{0}.tif".format(outprefixV23,finalpathV23))
                }
        processing.run('gdal:rastercalculator',parameters)

    v23 = glob.glob(os.path.join(parthDirection+"/V23", "*.tif"))
    outprefixV22 = '_v22'
    print('Calculando..')
    for valor_a, valor_b in zip(pr,v23):
        ex_path = valor_a.rstrip("_pr.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/Pr')
        finalpathV22 = parthDirection+"/V22" + temp_path
        #V22
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '(A*0.1*0.66)',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V22", "{1}{0}.tif".format(outprefixV22,finalpathV22))
                }
        processing.run('gdal:rastercalculator',parameters)
        
    v22 = glob.glob(os.path.join(parthDirection+"/V22", "*.tif"))
    outprefixV21 = '_v21'
    print('Calculando..')
    for valor_a, valor_b in zip(pr,v22):
        ex_path = valor_a.rstrip("_pr.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/Pr')
        finalpathV21 = parthDirection+"/V21" + temp_path
        #V21
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '(A*0.1*0.22)',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V21", "{1}{0}.tif".format(outprefixV21,finalpathV21))
                }
        processing.run('gdal:rastercalculator',parameters)
        
    outprefixV13 = '_v13'
    outprefixV14 = '_v14'
    outprefixV15 = '_v15'
    outprefixV16 = '_v16'
    outprefixV17 = '_v17'
    outprefixV18 = '_v18'
    outprefixV19 = '_v19'
    outprefixV110 = '_v110'
    outprefixV24 = '_v24'
    outprefixV25 = '_v25'
    outprefixV26 = '_v26'
    outprefixV27 = '_v27'
    outprefixV28 = '_v28'
    outprefixV29 = '_v29'
    outprefixV210 = '_v210'
    outprefixV211 = '_v211'
    outprefixV212 = '_v212'
    outprefixV213 = '_v213'
    outprefixV214 = '_v214'
    outprefixV215 = '_v215'
    outprefixV216 = '_v216'
    outprefixV217 = '_v217'
    outprefixV218 = '_v218'
    outprefixV219 = '_v219'
    outprefixV220 = '_v220'

    print('Calculando..')
    for valor_a in pr:
        ex_path = valor_a.rstrip("_pr.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/Pr')
        finalpathV13 = parthDirection+"/V13" + temp_path
        finalpathV14 = parthDirection+"/V14" + temp_path
        finalpathV15 = parthDirection+"/V15" + temp_path
        finalpathV16 = parthDirection+"/V16" + temp_path
        finalpathV17 = parthDirection+"/V17" + temp_path
        finalpathV18 = parthDirection+"/V18" + temp_path
        finalpathV19 = parthDirection+"/V19" + temp_path
        finalpathV110 = parthDirection+"/V110" + temp_path
        finalpathV24 = parthDirection+"/V24" + temp_path
        finalpathV25 = parthDirection+"/V25" + temp_path
        finalpathV26 = parthDirection+"/V26" + temp_path
        finalpathV27 = parthDirection+"/V27" + temp_path
        finalpathV28 = parthDirection+"/V28" + temp_path
        finalpathV29 = parthDirection+"/V29" + temp_path
        finalpathV210 = parthDirection+"/V210" + temp_path
        finalpathV211 = parthDirection+"/V211" + temp_path
        finalpathV212 = parthDirection+"/V212" + temp_path
        finalpathV213 = parthDirection+"/V213" + temp_path
        finalpathV214 = parthDirection+"/V214" + temp_path
        finalpathV215 = parthDirection+"/V215" + temp_path
        finalpathV216 = parthDirection+"/V216" + temp_path
        finalpathV217 = parthDirection+"/V217" + temp_path
        finalpathV218 = parthDirection+"/V218" + temp_path
        finalpathV219 = parthDirection+"/V219" + temp_path
        finalpathV220 = parthDirection+"/V220" + temp_path
        
        #V13
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '(A*0.9*0)',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V13", "{1}{0}.tif".format(outprefixV13,finalpathV13))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V14
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V14", "{1}{0}.tif".format(outprefixV14,finalpathV14))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V15
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V15", "{1}{0}.tif".format(outprefixV15,finalpathV15))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V16
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V16", "{1}{0}.tif".format(outprefixV16,finalpathV16))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V17
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V17", "{1}{0}.tif".format(outprefixV17,finalpathV17))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V18
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V18", "{1}{0}.tif".format(outprefixV18,finalpathV18))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V19
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V19", "{1}{0}.tif".format(outprefixV19,finalpathV19))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V110
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V110", "{1}{0}.tif".format(outprefixV110,finalpathV110))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V24
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V24", "{1}{0}.tif".format(outprefixV24,finalpathV24))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V25
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V25", "{1}{0}.tif".format(outprefixV25,finalpathV25))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V26
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V126", "{1}{0}.tif".format(outprefixV26,finalpathV26))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V27
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V27", "{1}{0}.tif".format(outprefixV27,finalpathV27))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V28
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V28", "{1}{0}.tif".format(outprefixV28,finalpathV28))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V29
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V29", "{1}{0}.tif".format(outprefixV29,finalpathV29))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V210
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V210", "{1}{0}.tif".format(outprefixV210,finalpathV210))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V211
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V211", "{1}{0}.tif".format(outprefixV211,finalpathV211))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V212
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V212", "{1}{0}.tif".format(outprefixV212,finalpathV212))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V213
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V213", "{1}{0}.tif".format(outprefixV213,finalpathV213))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V214
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V214", "{1}{0}.tif".format(outprefixV214,finalpathV214))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V215
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V215", "{1}{0}.tif".format(outprefixV215,finalpathV215))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V216
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V216", "{1}{0}.tif".format(outprefixV216,finalpathV216))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V217
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V217", "{1}{0}.tif".format(outprefixV217,finalpathV217))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V218
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V218", "{1}{0}.tif".format(outprefixV218,finalpathV218))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V219
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V219", "{1}{0}.tif".format(outprefixV219,finalpathV219))
                }
        processing.run('gdal:rastercalculator',parameters)
        #V220
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '0',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/V220", "{1}{0}.tif".format(outprefixV220,finalpathV220))
                }
        processing.run('gdal:rastercalculator',parameters)
        

    v11 = glob.glob(os.path.join(parthDirection+"/V11", "*.tif"))
    outPrefixRx3 = '_rx(B)'
    print('Calculando..')
    for valor_a in v11:
        ex_path = valor_a.rstrip("_v.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/V11')
        finalpath = parthDirection+"/rX3(B)" + temp_path
        formula = "max("+roX3[0]+"+(A+"+x2[0]+")/"+x3[0]+")"
        #r/x3(B)
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': formula,
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/rX3(B)", "{1}{0}.tif".format(outPrefixRx3,finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)
        
    rx3B = glob.glob(os.path.join(parthDirection+"/rX3(B)", "*.tif"))
    outPrefixQr = '_Qr'
    print('Calculando..')
    for valor_a in rx3B:
        ex_path = valor_a.rstrip("_rx(B).tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/rX3(B)')
        finalpath = parthDirection+"/Qr" + temp_path
        formula = "(A*"+x3[0]+"*(1-(1+A^4)^(-0.25)))"
        #Qr
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': formula,
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/Qr", "{1}{0}.tif".format(outPrefixQr,finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)
        
    qR = glob.glob(os.path.join(parthDirection+"/Qr", "*.tif"))
    outPrefixRxC = '_rx(C)'
    print('Calculando..')
    for valor_a, valor_b in zip(rx3B,qR):
        ex_path = valor_a.rstrip("_rx(B).tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/rX3(B)')
        finalpath = parthDirection+"/rX3(C)" + temp_path
        formula = "(A-B/"+x3[0]+")"
        #RX/3C
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': formula,
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/rX3(C)", "{1}{0}.tif".format(outPrefixRxC,finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)

    outPrefixQD = '_qd'
    print('Calculando..')
    for valor_a in prec:
        ex_path = valor_a.rstrip("_Precipitación.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Precipitacion')
        finalpath = parthDirection+"/Qd" + temp_path
        formula = "max(A+"+x2[0]+")"
        #Qd
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':None,
                'BAND_B': None,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': formula,
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/Qd", "{1}{0}.tif".format(outPrefixQD,finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)

    qD = glob.glob(os.path.join(parthDirection+"/Qd", "*.tif"))
    outPrefixQ = '_q'
    print('Calculando..')
    for valor_a, valor_b in zip(qR,qD):
        ex_path = valor_a.rstrip("_Qr.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Calculos/Qr')
        finalpath = parthDirection+"/Q" + temp_path
        #RX/3C
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': 'A+B*2',
                'NO_DATA': None,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/Q", "{1}{0}.tif".format(outPrefixQ,finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)

    print('Calculando..')
    outPrefixDeb = '_Debit'
    for valor_a, valor_b in zip(prec,eta):
        ex_path = valor_a.rstrip("_Precipitación.tif")
        temp_path = ex_path.lstrip('C:/Qgis/Precipitacion')
        finalpath = parthDirection+"/Debit" + temp_path
        #Debit
        parameters = {
                'INPUT_A':valor_a,
                'BAND_A':1,
                'INPUT_B':valor_b,
                'BAND_B': 1,
                'INPUT_C': None,
                'BAND_C': None,
                'INPUT_D': None,
                'BAND_D': None,
                'INPUT_E': None,
                'BAND_E': None,
                'INPUT_F': None,
                'BAND_F': None,
                'FORMULA': '(A+B)',
                'NO_DATA': 50,
                'RTYPE': None,
                'OPTIONS':'',
                'EXTRA': '',
                'OUTPUT': os.path.join(parthDirection+"/Debit", "{0}.tif".format(finalpath))
                }
        processing.run('gdal:rastercalculator',parameters)

    print('Calculos Finalizados')

    #Convertir los Datos a NetCDF
    print('Creando Archivo NetCDF')
    ds = gdal.Open('C:/Qgis/Calculos/Debit/Datos-2022-01-01.tif')
    a = ds.ReadAsArray()
    projection = ds.GetProjection()
    nlat,nlon = np.shape(a)
    b = ds.GetGeoTransform() #bbox, interval
    lon = np.arange(nlon)*b[1]+b[0]
    lat = np.arange(nlat)*b[5]+b[3]
    x_origin = b[0]
    y_origin = b[3]
    x_res = b[1]
    y_res = b[5]
    width = ds.RasterXSize
    height = ds.RasterYSize
    x_end = x_origin + (width * x_res)
    y_end = y_origin + (height * abs(y_res))
    basedate = dt.datetime(1980,1,1,0,0,0)
    nco = netCDF4.Dataset('C:/Qgis/netCDFiles/caudales4.nc','w',clobber=True)
    chunk_lon=10
    chunk_lat=10
    chunk_time=12
    # create dimensions, variables and attributes:
    nco.createDimension('lon',nlon)
    nco.createDimension('lat',nlat)
    nco.createDimension('time',None)
    
    timeo = nco.createVariable('time','f4',('time'))
    timeo.units = 'days since 1980-1-1 00:00:00'
    timeo.standard_name = 'time'
    timeo.calendar = 'gregorian'
    timeo.axis = 'T'
    
    lono = nco.createVariable('lon','f4',('lon'))
    lono.units = 'degrees_east'
    lono.standard_name = 'longitude'
    lono.long_name = 'longitude'
    lono.axis = 'X'
    
    lato = nco.createVariable('lat','f4',('lat'))
    lato.units = 'degrees_north'
    lato.standard_name = 'latitude'
    lato.long_name = 'latitude'
    lato.axis = 'Y'
    
    # create container variable for CRS: lon/lat WGS84 datum
    crso = nco.createVariable('crs','i4')
    crso.long_name = 'Sistema de Referencia de Coordenadas'
    crso.grid_mapping_name ='Mercator'
    crso.latitude_of_projection_origin = 0.0
    crso.scale_factor_at_projection_origin = 0.9996
    crso.false_easting = 500000.0
    crso.longitude_of_prime_meridian = -81.0
    crso.semi_major_axis = 6378137.0
    crso.inverse_flattening = 298.257223563
    crso.x_origin = x_origin
    crso.y_origin = y_origin
    crso.x_res = x_res
    crso.y_res = y_res
    crso.width = width
    crso.height = height
    crso.x_end = x_end
    crso.y_end = y_end
    
    # create short integer variable for precipitation data, with chunking
    pcpo = nco.createVariable('band', 'f4',  ('time', 'lat', 'lon'),
        zlib=True,chunksizes=[chunk_time,chunk_lat,chunk_lon],fill_value=-9999.)
    pcpo.units = 'Degree'
    pcpo.standard_name = 'Datos de caudales'
    pcpo.long_name = 'Caudales a causa del impacto de las precipitaciones'
    pcpo.time_step = 'dekad'
    pcpo.missing_value = -9999.
    pcpo.geospatial_lat_min = 0.0
    pcpo.geospatial_lat_max = 80.0
    pcpo.geospatial_lon_min = -180.0
    pcpo.geospatial_lon_max = 180.0
    pcpo.grid_mapping = 'crs'
    pcpo.set_auto_maskandscale(False)
    
    nco.Conventions='CF-1.6'
    nco.title = "Caudales"
    nco.history = "created by Andrés Vallejo"
    nco.version = "Version 2.0"
    nco.comments = "Impacto de precipitaciones en cuenca hidrografica"
    nco.website = "N/A"
    nco.date_created = "2022-3-14"
    nco.creator_name = "Benny Istanto"
    nco.creator_email = "andresvallejoz@gmail.com"
    nco.institution = "UTPL Universidad Técnica Particular de Loja"
    nco.note = "Datos a partir del Interpolado en base a calculos de Precipitación"
    
    #write lon,lat
    lono[:]=lon
    lato[:]=lat
    
    pat = re.compile('Datos-[0-9]{4}-[0-9]{2}-[0-9]{2}')
    itime=0
    
    #step through data, writing time and data to NetCDF
    for root, dirs, files in os.walk('C:/Qgis/Calculos/Debit/'):
        dirs.sort()
        files.sort()
        for f in files:
            if re.match(pat,f):
                # read the time values by parsing the filename
                year=int(f[6:10])
                mon=int(f[11:13])
                dekad=int(f[14:16])
                date=dt.datetime(year,mon,dekad,0,0,0)
                dtime=(date-basedate).total_seconds()/86400.
                timeo[itime]=dtime
                # caudales
                pcp_path = os.path.join(root,f)
                pcp=gdal.Open(pcp_path)
                a=pcp.ReadAsArray()  #data
                pcpo[itime,:,:]=a
                itime=itime+1

    
    pcp = None
    ds = None
    nco.close()
    print('Archivo NetCDF creado')
    print('Proceso terminado')
except: 
   print('Formato de fecha incorrecto') 



