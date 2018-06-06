import os
from shutil import copyfile

from strings import Urls
from strings import AirFields
from strings import TempFields
from strings import WindFields


for directory in Urls.origin_directories:
    for filename in os.listdir(directory):
        try:
            if filename.startswith(AirFields.prefix):
                new_name = filename[38:44] + '.csv'
                print(filename + ' to ' + new_name)
                copyfile(
                    directory + filename,
                    Urls.unal_air + new_name
                )
            elif filename.startswith(TempFields.prefix):
                new_name = filename[40:46] + '.csv'
                print(filename + ' to ' + new_name)
                copyfile(
                    directory + filename,
                    Urls.unal_temp + new_name
                )
            elif filename.startswith(WindFields.prefix):
                new_name = filename[36:42] + '.csv'
                print(filename + ' to ' + new_name)
                copyfile(
                    directory + filename,
                    Urls.unal_wind + new_name
                )
        except Exception as e:
            print(e)
            pass


