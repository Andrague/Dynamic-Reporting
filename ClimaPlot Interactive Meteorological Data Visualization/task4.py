import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import re
import plotly.subplots as sp
import plotly.graph_objects as go
def convert_coordinates(coord_str, direction):
    degrees, minutes, seconds = map(float, re.findall(r'\d+', coord_str))
    decimal_degrees = degrees + minutes / 60 + seconds / 3600
    return -decimal_degrees if direction in ['W', 'S'] else decimal_degrees

stations_data = pd.read_csv('data-meteo/zestawienie_stacji.txt', sep='\t')
print(stations_data)
for col in ['DŁUG_GEOG', 'SZER_GEOGR']:
    stations_data[f'{col}_value'] = stations_data[col].str.extract(r'(\d+°\d+\'\d+\'\')')[0]
    stations_data[f'{col}_direction'] = stations_data[col].str.extract(r'(\w)$')[0]
    stations_data[col] = stations_data.apply(lambda row: convert_coordinates(row[f'{col}_value'], row[f'{col}_direction']), axis=1)

fig_map = px.scatter_geo(stations_data,
                         lat='SZER_GEOGR',
                         lon='DŁUG_GEOG',
                         text='NAZWA_ST',
                         title='Mapa stacji',
                         labels={'NAZWA_ST': 'Nazwa stacji'},
                         hover_name='NAZWA_ST',
                         hover_data={'NAZWA_ST': False, 'SZER_GEOGR': ':.4f', 'DŁUG_GEOG': ':.4f'},
                         projection='natural earth')

fig_map.update_traces(marker=dict(size=10, color='red', symbol='circle'))

fig_map.show()
fig_map.write_image("graf.png")

data_station1 = pd.read_json('data-meteo/json/249180010.json')
data_station2 = pd.read_json('data-meteo/json/249180130.json')
data_station3 = pd.read_json('data-meteo/json/249180160.json')
# Создание subplots
fig = sp.make_subplots(rows=3, cols=1, subplot_titles=['Stacja 1', 'Stacja 2', 'Stacja 3'],
                       shared_xaxes=True, vertical_spacing=0.1)
# Добавление графиков на subplots
fig.add_trace(go.Scatter(x=data_station1['dt'], y=data_station1['t'], mode='lines', name='Stacja 1'), row=1, col=1)
fig.add_trace(go.Scatter(x=data_station2['dt'], y=data_station2['t'], mode='lines', name='Stacja 2'), row=2, col=1)
fig.add_trace(go.Scatter(x=data_station3['dt'], y=data_station3['t'], mode='lines', name='Stacja 3'), row=3, col=1)

# Настройка меток осей и заголовка
fig.update_xaxes(title_text='Data i godzina', row=3, col=1)
fig.update_yaxes(title_text='Temperatura (°C)', row=2, col=1)
fig.update_layout(title_text='Wykres temperatur dla trzech stacji', height=800)
fig.show()

fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True, sharey=True)

axes[0].hist(data_station1['t'], bins=20, color='blue', alpha=0.7, label='Stacja 1')
axes[0].set_title('Rozkład temperatury - Stacja 1')

axes[1].hist(data_station2['t'], bins=20, color='green', alpha=0.7, label='Stacja 2')
axes[1].set_title('Rozkład temperatury - Stacja 2')

axes[2].hist(data_station3['t'], bins=20, color='orange', alpha=0.7, label='Stacja 3')
axes[2].set_title('Rozkład temperatury - Stacja 3')

for ax in axes:
    ax.legend()
    ax.set_xlabel('Temperatura (°C)')
    ax.set_ylabel('Liczba pomiarów')
plt.tight_layout()
plt.show()

data_all_stations = []
for station_id in stations_data['KOD_SZS']:
    json_file_path = f'data-meteo/json/{station_id}.json'
    if os.path.exists(json_file_path):
        data_station = pd.read_json(json_file_path)
        data_station['station_id'] = station_id
        data_all_stations.append(data_station)

# Объединение данных для всех станций
df_all_stations = pd.concat(data_all_stations, ignore_index=True)
# Расчет среднегодовой температуры для каждой станции
df_avg_temp = df_all_stations.groupby('station_id')['t'].mean().reset_index()
# Сортировка станций по среднегодовой температуре
df_sorted_stations = pd.merge(stations_data, df_avg_temp, left_on='KOD_SZS', right_on='station_id').sort_values(by='t')
fig = px.scatter_geo(df_sorted_stations,
                     lat='SZER_GEOGR',
                     lon='DŁUG_GEOG',
                     text='NAZWA_ST',
                     title='Mapa stacji według średniej rocznej temperatury.',
                     labels={'NAZWA_ST': 'Nazwa stacji'},
                     hover_name='NAZWA_ST',
                     hover_data={'NAZWA_ST': False, 'SZER_GEOGR': ':.4f', 'DŁUG_GEOG': ':.4f', 't': ':.2f'},
                     projection='natural earth',
                     color='t',
                     color_continuous_scale='viridis',
                     size='t',
                     size_max=20)

fig.show()
