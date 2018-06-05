import matplotlib.pyplot as plt
import pandas as pd

from utils import Urls
from utils import AirFields
from utils import TempFields
from utils import WindFields

data_air = pd.read_csv(Urls.valid_data + 'all_data_air.csv')
data_temp = pd.read_csv(Urls.valid_data + 'all_data_temp.csv')
data_wind = pd.read_csv(Urls.valid_data + 'all_data_wind.csv')

air_data_frame = pd.DataFrame(data_air)
temp_data_frame = pd.DataFrame(data_temp)
wind_data_frame = pd.DataFrame(data_wind)


def create_graph(frame, field_1, field_2, url, name):
    plot = frame[[field_1, field_2]].plot(
        kind='bar',
        title=name,
        figsize=(15, 10),
        legend=True,
        fontsize=12
    )
    plot.set_xlabel(field_1, fontsize=12)
    plot.set_ylabel(field_2, fontsize=12)
    figure = plot.get_figure()
    figure.savefig(url + name + '.png')


create_graph(
    air_data_frame, AirFields.date,
    AirFields.pm25, Urls.graphs_air,
    'date vs pm25'
)
create_graph(
    temp_data_frame, TempFields.date,
    TempFields.temp, Urls.graphs_temp,
    'date vs temperature'
)
create_graph(
    wind_data_frame, WindFields.date,
    WindFields.speed, Urls.graphs_wind,
    'date vs winds'
)


air_monthly = air_data_frame.loc[
    air_data_frame[AirFields.date].str.endswith('15 12:00:00'),
    [AirFields.date, AirFields.pm25]
]

temp_monthly = temp_data_frame.loc[
    temp_data_frame[TempFields.date].str.endswith('15 12:00:00'),
    [TempFields.date, TempFields.temp]
]

wind_monthly = wind_data_frame.loc[
    wind_data_frame[WindFields.date].str.endswith('15 12:00:00'),
    [WindFields.date, WindFields.speed]
]

create_graph(
    air_monthly, AirFields.date, AirFields.pm25,
    Urls.graphs_air, 'All 15 days vs pm25'
)
create_graph(
    temp_monthly, TempFields.date, TempFields.temp,
    Urls.graphs_temp, 'All 15 days vs Temperature'
)
create_graph(
    wind_monthly, WindFields.date, WindFields.speed,
    Urls.graphs_wind, 'All 15 days vs wind speed'
)
