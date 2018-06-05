import os
from shutil import copyfile

main_folder = os.path.realpath(__file__).replace('\\', '/').split('/')[0: -1]

unal_aire_org = os.path.join(
    '/'.join(main_folder),
    'original_data',
    'unal_aire/'
)
unal_temperatura_org = os.path.join(
    '/'.join(main_folder),
    'original_data',
    'unal_temperatura/'
)
unal_viento_org = os.path.join(
    '/'.join(main_folder),
    'original_data',
    'unal_viento/'
)

unal_aire_tar = os.path.join(
    '/'.join(main_folder),
    'valid_data',
    'unal_aire/')
unal_temperatura_tar = os.path.join(
    '/'.join(main_folder),
    'valid_data',
    'unal_temperatura/'
)
unal_viento_tar = os.path.join(
    '/'.join(main_folder),
    'valid_data',
    'unal_viento/'
)

origin_directories = [unal_aire_org, unal_temperatura_org, unal_viento_org]
target_directories = [unal_aire_tar, unal_temperatura_tar, unal_viento_tar]

for directory in origin_directories:
    for filename in os.listdir(directory):
        try:
            if filename.startswith('estacion_data_calidadaire_'):
                new_name = filename[38:44] + '.csv'
                print(filename + ' to ' + new_name)
                copyfile(
                    directory + filename,
                    unal_aire_tar + new_name
                )
            elif filename.startswith('estacion_data_temperatura_'):
                new_name = filename[40:46] + '.csv'
                print(filename + ' to ' + new_name)
                copyfile(
                    directory + filename,
                    unal_temperatura_tar + new_name
                )
            elif filename.startswith('estacion_data_vientos_'):
                new_name = filename[36:42] + '.csv'
                print(filename + ' to ' + new_name)
                copyfile(
                    directory + filename,
                    unal_viento_tar + new_name
                )
        except Exception as e:
            print(e)
            pass


