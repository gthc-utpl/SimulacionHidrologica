# SimulacionHidrologica
### TFT - Simulación Hidrológica 
Los siguientes Scripts forman parte del Trabajo de Integración Curricular correspondiente a la implementación computacional de un modelo hidrológico de paso continuo mediante el lenguaje de programación Python atraves de la herramienta de software geográfico Qgis. 

### Resumen
Los modelos hidrológicos actualmente existentes son muy complicados a la hora de trabajar, esto debido a la cantidad de datos que una persona debe ingresar, dificultando la evaluación de terreno y los efectos que la precipitación y demás condiciones hidrológicas producen el área en cuestión. De esta manera se procedió al desarrollo de un Script desarrollado en el lenguaje de programación Python y empleado dentro de la herramienta Qgis, este script permite realizar una extracción de datos climatológicos en base a una fecha inicial y final que una persona decida y simular un modelo hidrológico de paso continuo, el cual requiere únicamente de datos de estaciones climatológicas y de un archivo con información del terreno geográfico. Los resultados obtenidos nos muestran la obtención de cuencas hidrográficas delimitadas, las coordenadas de las estaciones climatológicas, los datos de precipitación, evapotranspiración y finalmente un interpolado en base a los datos hidrológicos posteriormente mencionados, todos los resultados se almacenan en un directorio con su carpeta correspondiente.
### Archivos de Entrada 
El modelo hidrológico solicita un directorio que contenga archivos excel con datos de precipitación y evapotranspiración de estaciones climatologicas, el segundo archivo que solicita es el modelo de elevación digital (DEM), este archivo es esencial para realizar la delimitación de la cuenca hidrográfica y por ultimo solicita un archivo excel que contenga las coordenadas geográficas de las estaciones climatológicas.
### Coordendas Geográficas
Una vez ejecutado el Script, se muestran los puntos de coordenadas en la interfaz de Qgis, en este caso se muestra un punto que contiene toda la información.
### Cuencas Hidrográficas 
En base al modelo de elevación digital (DEN) se demilita la cuenca hidrográfica, en el entorno de Qgis se muestra la cuenca mayor junto a las subcuencas, para ello el archivo DEM pasa por un tratamiento a travez de herramientas provistas por Qgis, las cuales permiten delimitar la cuenca.
### Interpolado
En base a al archivo que contiene los datos de precipitación y evapotranspiración, se unen junto a las coordenadas geograficas y tomando como referencia la cuenca hidrográfica para la extensión territoral se realiza un interpolado en base a los datos ponderados de precipitacón y evapotranspiración, como resultado se obtiene una capa de cada uno para el rango de fecha seleccionado con el usuario.
### Calculos matemáticos
Posteriormente se realizan los calculos matemáticos correspondientes al modelo hidrológico, un total de 40 variables que son realizadas mediante la herramienta calculadora de Raster, estos calculos permite obtener la variable debit, esta ultima hace referencia a los caudales y el impacto de las inundaciones dentro de la cuenca hidrográfica delimitada.
### Archivo netCDF

