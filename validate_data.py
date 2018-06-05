import pandas as pd
import os

main_folder = os.path.realpath(__file__).replace('\\', '/').split('/')[0: -1]

unal_aire = os.path.join(
    '/'.join(main_folder),
    'valid_data',
    'unal_aire/')
unal_temperatura = os.path.join(
    '/'.join(main_folder),
    'valid_data',
    'unal_temperatura/'
)
unal_viento = os.path.join(
    '/'.join(main_folder),
    'valid_data',
    'unal_viento/'
)

for filename in os.listdir(unal_aire):
    try:
        file = unal_aire + filename
        data = pd.read_csv(file)
        print('Filename ' + filename + ' opened')
    except Exception as e:
        print(e)
        pass
    else:
        valid_data = data.loc[
            (data['Fecha_Hora'].str.endswith('12:00:00')) &
            (data['calidad_pm25'] == 1.0),
            ['Fecha_Hora', 'pm25']
        ]
        data_frame = pd.DataFrame(valid_data)
        data_frame.to_csv(
            unal_aire + filename,
            header=True,
            index=False
        )

for filename in os.listdir(unal_temperatura):
    try:
        file = unal_temperatura + filename
        data = pd.read_csv(file)
        print('Filename ' + filename + ' opened')
    except Exception as e:
        print(e)
        pass
    else:
        valid_data = data.loc[
            (data['fecha_hora'].str.endswith('12:00:00')) &
            (data['Calidad'] == 1),
            ['fecha_hora', 'Temperatura']
        ]
        data_frame = pd.DataFrame(valid_data)
        data_frame.to_csv(
            unal_temperatura + filename,
            header=True,
            index=False
        )

for filename in os.listdir(unal_viento):
    try:
        file = unal_viento + filename
        data = pd.read_csv(file)
        print('Filename ' + filename + ' opened')
    except Exception as e:
        print(e)
        pass
    else:
        valid_data = data.loc[
            (data['fecha_hora'].str.endswith('12:00:00')) &
            (data['Calidad'] == 1),
            ['fecha_hora', 'Velocidad_Prom', 'Direccion_Prom']
        ]
        data_frame = pd.DataFrame(valid_data)
        data_frame.to_csv(
            unal_viento + filename,
            header=True,
            index=False
        )
