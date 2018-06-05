import numpy as np
import pandas as pd
import os

from matplotlib import pyplot as plt

main_folder = os.path.realpath(__file__).replace('\\', '/').split('/')[0: -1]

unal_folder = os.path.join('/'.join(main_folder), 'estacion_unal/')
itagui_folder = os.path.join('/'.join(main_folder), 'estacion_itagui/')

data = pd.read_csv(
    unal_folder + '201204.csv',
    sep=',',
    usecols=("Fecha_Hora", "pm25")
)

cond_1 = data['pm25'] < 100
cond_2 = data['pm25'] > 0
valid_data = data[cond_1 & cond_2]

valid_data['Fecha_Hora'] = pd.to_datetime(valid_data['Fecha_Hora'])
valid_data['hora'] = valid_data.loc[:, 'Fecha_Hora'].dt.hour

cond_3 = valid_data[valid_data['hora'] == 12]

print(valid_data.head())

# os.walk
# Creo lista de dataframe
# pandas concatenar dataframe
# pandas to csv

# fecha = valid_data['Fecha_Hora'].tolist()
# pm25 = valid_data['pm25'].tolist()
#
# plt.plot(fecha, pm25)
# plt.show()
#
# print(fecha)
# print(pm25)
