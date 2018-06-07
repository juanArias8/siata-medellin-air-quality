import pandas as pd
import os

from strings import Urls
from strings import AirFields
from strings import TempFields
from strings import WindFields


def validate_data(directory, field1, field2):
    for filename in os.listdir(directory):
        try:
            file = directory + filename
            data = pd.read_csv(file)
            print('Filename ' + filename + ' opened')
        except Exception as e:
            print(e)
        else:
            valid_data = data.loc[
                data[field1].str.endswith('12:00:00'),
                [field1, field2]
            ]
            valid_data.loc[valid_data[field2] < 0, field2] = 0
            valid_data.loc[valid_data[field2] > 100, field2] = 0
            good_records = valid_data.loc[
                valid_data[field2] != 0, field2
            ]
            mean = int(good_records.mean())
            print('Mean of ' + filename + ' => ' + str(mean))
            valid_data.loc[
                valid_data[field2] == 0, field2
            ] = mean
            data_frame = pd.DataFrame(valid_data)
            data_frame.to_csv(
                directory + filename,
                header=True,
                index=False
            )


validate_data(Urls.unal_air, AirFields.date, AirFields.pm25)
validate_data(Urls.unal_temp, TempFields.date, TempFields.temp)
validate_data(Urls.unal_wind, WindFields.date, WindFields.speed)
