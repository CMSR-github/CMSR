import plotly.express as px
import numpy as np

lats = np.arange(30,40,.1) 
lons = np.arange(30,40,.1) 

fig = px.line_geo(lat=lats, lon=lons)
fig.update_geos(fitbounds="locations")

fig.show()
