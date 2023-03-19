# import necessary libraries
import pandas as pd
import os
import glob
import datetime

fecha_inicio = QInputDialog().getText(None,"Rango de Fecha","Fecha Inicio")

fecha_fin = QInputDialog().getText(None,"Rango de Fecha","Fecha Fin")

start = datetime.datetime.strptime(fecha_inicio[0], "%Y-%m-%d")
end = datetime.datetime.strptime(fecha_fin[0], "%Y-%m-%d")

date_generated = pd.date_range(start, end)

path = 'C:/Users/andre/Desktop/Datos para modelo'

csv_files = glob.glob(os.path.join(path, "*.xlsx"))

combinado_csv = pd.concat([pd.read_excel(f) for f in csv_files ])

for i, valor in enumerate(date_generated):
    filtered_df = combinado_csv.loc[(combinado_csv['Fecha'] == valor)]
    filtered_df.to_csv('C:\Qgis\Datos\Datos-{}.csv'.format(valor.strftime("%Y-%m-%d")))


