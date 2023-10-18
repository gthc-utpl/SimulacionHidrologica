### Simulación Hidrológica

Los siguientes scripts forman parte del Trabajo de Integración Curricular correspondiente a la implementación computacional de un modelo hidrológico de paso continuo mediante el lenguaje de programación Python a través de la herramienta de software geográfico QGIS.

### Resumen
Los modelos hidrológicos existentes son complicados de trabajar debido a la cantidad de datos que se deben ingresar, lo que dificulta la evaluación del terreno y los efectos de la precipitación y otras condiciones hidrológicas en el área en cuestión. Por lo tanto, se desarrolló un script en Python que se utiliza dentro de la herramienta QGIS para realizar una extracción de datos climatológicos y simular un modelo hidrológico de paso continuo. Este modelo sólo requiere datos de estaciones climatológicas y un archivo con información del terreno geográfico. Los resultados obtenidos incluyen la delimitación de cuencas hidrográficas, las coordenadas de las estaciones climatológicas, los datos de precipitación y evapotranspiración, y una interpolación basada en estos datos. Todos los resultados se almacenan en un directorio con su carpeta correspondiente.

### Archivos de entrada
El modelo hidrológico requiere un directorio que contenga archivos de Excel con datos de precipitación y evapotranspiración de estaciones climatológicas. También solicita un archivo de modelo de elevación digital (DEM), que es necesario para delimitar la cuenca hidrográfica. Por último, se solicita un archivo de Excel que contenga las coordenadas geográficas de las estaciones climatológicas.

### Coordenadas geográficas
Una vez que se ejecuta el script, se muestran los puntos de coordenadas en la interfaz de QGIS. En este caso, se muestra un punto que contiene toda la información.

### Cuencas hidrográficas
Se delimita la cuenca hidrográfica en base al modelo de elevación digital (DEM). En el entorno de QGIS, se muestra la cuenca principal junto con las subcuencas. Para lograr esto, el archivo DEM se procesa utilizando herramientas proporcionadas por QGIS, que permiten delimitar la cuenca.

### Interpolación
Se realiza una interpolación basada en los datos de precipitación y evapotranspiración, utilizando las coordenadas geográficas y la cuenca hidrográfica como referencia para la extensión territorial. Como resultado, se obtiene una capa para cada variable (precipitación y evapotranspiración) para el rango de fechas seleccionado por el usuario.

### Cálculos matemáticos
Se realizan cálculos matemáticos correspondientes al modelo hidrológico, que involucran un total de 40 variables. Estos cálculos se realizan utilizando la herramienta Calculadora de Raster y permiten obtener la variable "debit", que se refiere a los caudales y al impacto de las inundaciones dentro de la cuenca hidrográfica delimitada.

### Archivo netCDF
Finalmente, todas las capas "debit" creadas por el script se recopilan y se agregan a un archivo netCDF. Gracias al formato netCDF, todas las capas solicitadas por el usuario se pueden almacenar en un solo archivo, lo que permite visualizar el impacto de las precipitaciones de manera más efectiva. 
