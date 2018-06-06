import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from strings import Urls
from strings import AirFields
from strings import TempFields
from strings import WindFields

data_air = pd.read_csv(Urls.valid_data + 'all_data_air.csv')
data_temp = pd.read_csv(Urls.valid_data + 'all_data_temp.csv')
data_wind = pd.read_csv(Urls.valid_data + 'all_data_wind.csv')

air_data_frame = pd.DataFrame(data_air)
temp_data_frame = pd.DataFrame(data_temp)
wind_data_frame = pd.DataFrame(data_wind)

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

list_air = air_monthly.values.tolist()
list_temp = temp_monthly.values.tolist()
list_wind = wind_monthly.values.tolist()

unified_list = []
for item_air in list_air:
    for item_temp in list_temp:
        for item_wind in list_wind:
            if item_air[0] == item_temp[0] == item_wind[0]:
                item = [item_air[0], item_air[1], item_temp[1], item_wind[1]]
                unified_list.append(item)
                break


unified_data_frame = pd.DataFrame(unified_list)
unified_data_frame.to_csv(
    Urls.valid_data + 'final_data.csv',
    index=False
)


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
create_graph(
    air_monthly, AirFields.date,
    AirFields.pm25, Urls.graphs_air,
    'All 15 days vs pm25'
)
create_graph(
    temp_monthly, TempFields.date,
    TempFields.temp, Urls.graphs_temp,
    'All 15 days vs Temperature'
)
create_graph(
    wind_monthly, WindFields.date,
    WindFields.speed, Urls.graphs_wind,
    'All 15 days vs wind speed'
)

date_list = unified_data_frame.iloc[:, 0].tolist()
pm25_list = unified_data_frame.iloc[:, 1].tolist()
temp_list = unified_data_frame.iloc[:, 2].tolist()
wind_list = unified_data_frame.iloc[:, 3].tolist()

for i in range(len(date_list)):
    date_list[i] = date_list[i][3:9]

axe_y = [pm25_list, temp_list, wind_list]

plt.figure()
plt.xlabel("Date")
plt.ylabel("pm25, temp, wind")
plt.title("All 15 days values data")
plt.xticks(rotation=90)

plt.plot(date_list, pm25_list, 'r', label='Pm25')
plt.plot(date_list, temp_list, 'g', label='Temperature')
plt.plot(date_list, wind_list, 'b', label='Wind')
plt.legend()
plt.savefig(Urls.graphs + 'final_data.png')
plt.show()

