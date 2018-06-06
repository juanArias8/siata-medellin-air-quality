import pandas as pd
import os

from strings import Urls

all_data_air = []
all_data_temp = []
all_data_wind = []

files_air = os.listdir(Urls.unal_air)
files_temp = os.listdir(Urls.unal_temp)
files_wind = os.listdir(Urls.unal_wind)

files_air.sort()
files_temp.sort()
files_wind.sort()


def create_super_frame(files, url_files, all_data):
    for filename in files:
        try:
            file = url_files + filename
            data = pd.read_csv(file)
        except Exception as e:
            print(e)
        else:
            all_data.append(data)
            print('data from ' + filename + ' append to air_data')


create_super_frame(files_air, Urls.unal_air, all_data_air)
create_super_frame(files_temp, Urls.unal_temp, all_data_temp)
create_super_frame(files_wind, Urls.unal_wind, all_data_wind)

air_data_frame = pd.concat(all_data_air)
temp_data_frame = pd.concat(all_data_temp)
wind_data_frame = pd.concat(all_data_wind)


def save_file(frame, url, name):
    frame.to_csv(
        url + name + '.csv',
        header=True,
        index=False
    )


save_file(air_data_frame, Urls.valid_data, 'all_data_air')
save_file(temp_data_frame, Urls.valid_data, 'all_data_temp')
save_file(wind_data_frame, Urls.valid_data, 'all_data_wind')


