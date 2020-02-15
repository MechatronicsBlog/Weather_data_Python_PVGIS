from datetime import datetime
from PvGis import PvGis
import plotly.offline as py
import plotly.graph_objs as go

# Create PVGIS object
pvGis = PvGis()

# PvGis parameters
LATITUDE = 37.097
LONGITUDE = -2.365
START_DATE = datetime(2016, 6, 1, 00, 00, 00)
END_DATE = datetime(2016, 6, 7, 23, 59, 59)
DATABASE = 'PVGIS-SARAH'

# Set PVGIS parameters
pvGis.latitude = LATITUDE
pvGis.longitude = LONGITUDE
pvGis.start_date = START_DATE
pvGis.end_date = END_DATE
pvGis.rad_database = DATABASE
   
# Perform request
pvGis.request_hourly_time_series()

# Save weather data in a CSV file
pvGis.save_csv('weather_data.csv')

# Get Pandas DataFrame
df = pvGis.pandas_data_frame()

# Plot weather data
data_ghi = go.Scatter(x=df['DateTime'], y=df['GHI'], name='GHI (W/m^2)')
data_dni = go.Scatter(x=df['DateTime'], y=df['DNI'], name='DNI (W/m^2)')
data_dhi = go.Scatter(x=df['DateTime'], y=df['DHI'], name='DHI (W/m^2)')
data_tam = go.Scatter(x=df['DateTime'], y=df['TAmb'], name='Tamb (ºC)')
data_wsp = go.Scatter(x=df['DateTime'], y=df['Ws'], name='Wind (m/s)')
layout = go.Layout(title='Weather conditions', xaxis=dict(title='Date & time'), yaxis=dict(title='Value'))
fig = go.Figure(data=[data_ghi, data_dni, data_dhi, data_tam, data_wsp], layout=layout)
py.plot(fig, filename='weather_data.html')
