import pandas as pd
import os

from strings import Urls
from strings import AirFields
from strings import TempFields
from strings import WindFields


for filename in os.listdir(Urls.unal_air):
    try:
        file = Urls.unal_air + filename
        data = pd.read_csv(file)
        print('Filename ' + filename + ' opened')
    except Exception as e:
        print(e)
    else:
        valid_data = data.loc[
            (data[AirFields.date].str.endswith('12:00:00')),
            [AirFields.date, AirFields.pm25]
        ]
        valid_data.loc[valid_data[AirFields.pm25] < 0, AirFields.pm25] = 0
        valid_data.loc[valid_data[AirFields.pm25] > 100, AirFields.pm25] = 0
        valid_d = valid_data.loc[
            valid_data[AirFields.pm25] != 0, AirFields.pm25
        ]
        mean_air = valid_d.mean()
        mean_air = int(mean_air)
        print('mean_air ' + str(mean_air))
        valid_data.loc[valid_data[
           AirFields.pm25] == 0, AirFields.pm25
        ] = int(mean_air)
        data_frame = pd.DataFrame(valid_data)
        data_frame.to_csv(
            Urls.unal_air + filename,
            header=True,
            index=False
        )

for filename in os.listdir(Urls.unal_temp):
    try:
        file = Urls.unal_temp + filename
        data = pd.read_csv(file)
        print('Filename ' + filename + ' opened')
    except Exception as e:
        print(e)
    else:
        valid_data = data.loc[
            (data[TempFields.date].str.endswith('12:00:00')),
            [TempFields.date, TempFields.temp]
        ]
        valid_data.loc[valid_data[TempFields.temp] < 0, TempFields.temp] = 0
        valid_data.loc[valid_data[TempFields.temp] > 100, TempFields.temp] = 0
        valid_d = valid_data.loc[
            valid_data[TempFields.temp] != 0, TempFields.temp
        ]
        mean_temp = valid_d.mean()
        mean_temp = int(mean_temp)
        print('Mean temp ' + str(mean_temp))
        valid_data.loc[
            valid_data[TempFields.temp] == 0, TempFields.temp
        ] = int(mean_temp)
        data_frame = pd.DataFrame(valid_data)
        data_frame.to_csv(
            Urls.unal_temp + filename,
            header=True,
            index=False
        )

for filename in os.listdir(Urls.unal_wind):
    try:
        file = Urls.unal_wind + filename
        data = pd.read_csv(file)
        print('Filename ' + filename + ' opened')
    except Exception as e:
        print(e)
    else:
        valid_data = data.loc[
            (data[WindFields.date].str.endswith('12:00:00')),
            [WindFields.date, WindFields.speed]
        ]
        valid_data.loc[valid_data[WindFields.speed] < 0, WindFields.speed] = 0
        valid_data.loc[valid_data[WindFields.speed] > 100, WindFields.speed] = 0
        valid_d = valid_data.loc[
            valid_data[WindFields.speed] != 0, WindFields.speed
        ]
        mean_wind = valid_d.mean()
        mean_wind = int(mean_wind)
        print('Mean wind ' + str(mean_wind))
        valid_data.loc[valid_data[
            WindFields.speed] == 0, WindFields.speed
        ] = mean_wind
        data_frame = pd.DataFrame(valid_data)
        data_frame.to_csv(
            Urls.unal_wind + filename,
            header=True,
            index=False
        )
