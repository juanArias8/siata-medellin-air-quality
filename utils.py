import os


class Urls(object):
    main_folder = os.path.realpath(
        __file__
    ).replace('\\', '/').split('/')[0: -1]

    valid_data = os.path.join(
        '/'.join(main_folder),
        'valid_data/'
    )

    unal_air = os.path.join(
        '/'.join(main_folder),
        'valid_data',
        'unal_air/'
    )

    unal_temp = os.path.join(
        '/'.join(main_folder),
        'valid_data',
        'unal_temp/'
    )

    unal_wind = os.path.join(
        '/'.join(main_folder),
        'valid_data',
        'unal_wind/'
    )

    unal_air_org = os.path.join(
        '/'.join(main_folder),
        'original_data',
        'unal_air/'
    )

    unal_temp_org = os.path.join(
        '/'.join(main_folder),
        'original_data',
        'unal_temp/'
    )

    unal_wind_org = os.path.join(
        '/'.join(main_folder),
        'original_data',
        'unal_wind/'
    )

    graphs_air = os.path.join(
        '/'.join(main_folder),
        'images',
        'graphs_air/'
    )

    graphs_temp = os.path.join(
        '/'.join(main_folder),
        'images',
        'graphs_temp/'
    )

    graphs_wind = os.path.join(
        '/'.join(main_folder),
        'images',
        'graphs_wind/'
    )

    origin_directories = [
        unal_air_org,
        unal_temp_org,
        unal_wind_org
    ]

    target_directories = [
        unal_air,
        unal_temp,
        unal_wind
    ]


class AirFields(object):
    prefix = 'estacion_data_calidadaire_'
    date = 'Fecha_Hora'
    pm25 = 'pm25'


class TempFields(object):
    prefix = 'estacion_data_temperatura_'
    date = 'fecha_hora'
    temp = 'Temperatura'


class WindFields(object):
    prefix = 'estacion_data_vientos_'
    date = 'fecha_hora'
    speed = 'Velocidad_Prom'