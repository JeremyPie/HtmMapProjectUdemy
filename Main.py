import folium
import pandas as pd


df = pd.read_csv("Volcanoes.txt")

html = """<h4>Volcanoe Information:</h4>
Name: <a href="https://www.google.com/search?q=%22{}+Mount%22" target="_blank"><b>{}</b></a><br>
Height: {}m"""

def color_generator(elevation):
    if elev < 1000: return 'lightgreen'
    elif elev < 2000: return 'green'
    elif elev < 3000: return 'orange'
    elif elev < 4000: return 'red'
    else: return 'black'

map = folium.Map(location=[30.75624245178316, 34.88149453543761], zoom_start=9, tiles = "Stamen Terrain")
fg1 = folium.FeatureGroup(name="My Map")

for name, elev, lat, lon in zip(df['NAME'], df['ELEV'], df['LAT'], df['LON']):
    iframe = folium.IFrame(html=html.format(name,name,elev), width=200, height=100)
    fg1.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(iframe), radius=6,
    color=color_generator(elev), fill=True, fill_color=color_generator(elev), opacity=0.7, fill_opacity=0.7))
    map.add_child(fg1)

map.save("Map1.html")
