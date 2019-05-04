from datetime import datetime
from PvGis import PvGis
import plotly.offline as py
import plotly.graph_objs as go

# PvGis parameters
PRJ_LATITUDE = 37.097
PRJ_LONGITUDE = -2.365
PRJ_START_DATE = datetime(2016, 7, 1, 00, 00, 00)
PRJ_END_DATE = datetime(2016, 7, 7, 23, 59, 59)

# Set PvGis parameters
pvGis = PvGis()
pvGis.latitude = PRJ_LATITUDE
pvGis.longitude = PRJ_LONGITUDE
pvGis.start_date = PRJ_START_DATE
pvGis.end_date = PRJ_END_DATE
pvGis.verbose = True
   
# Perform request
pvGis.request_hourly_time_series()

# Save weather data in a CSV file
pvGis.save_csv('weather_data.csv')

# Get Pandas DataFrame
df = pvGis.pandas_data_frame()

# Plot data
data_ghi = go.Scatter(x=df['DateTime'], y=df['GHI'], name='GHI (W/m^2)')
data_dni = go.Scatter(x=df['DateTime'], y=df['DNI'], name='DNI (W/m^2)')
data_dhi = go.Scatter(x=df['DateTime'], y=df['DHI'], name='DHI (W/m^2)')
data_tam = go.Scatter(x=df['DateTime'], y=df['TAmb'], name='Tamb (ºC)')
data_wsp = go.Scatter(x=df['DateTime'], y=df['Ws'], name='Wind (m/s)')
layout = go.Layout(title='Weather conditions', xaxis=dict(title='Date & time'), yaxis=dict(title='Value'))
fig = go.Figure(data=[data_ghi, data_dni, data_dhi, data_tam, data_wsp], layout=layout)
py.iplot(fig, filename='weather-plot')
