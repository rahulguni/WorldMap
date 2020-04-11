import folium
import pandas

map = folium.Map(location = [38.77,-77.47], zoom_start = 10, tiles = "Stamen Terrain")

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def colorprod(eleva):
    if eleva < 1000:
        return "green"
    elif eleva >= 1000 and eleva < 3000:
        return "orange"
    else:
        return "red"

fgv = folium.FeatureGroup(name = "Volcanoes") #to organize the code
for lt, ln, el in zip(lat,lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt,ln], popup = str(el) + "m",
     fill_color = colorprod(el), fill = True, color = "grey", fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = open("world.json", 'r', encoding='utf-8-sig').read()
, style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("Map1.html")
