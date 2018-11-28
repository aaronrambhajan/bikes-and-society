from fastkml import kml
from shapely.geometry import Point, Polygon

file = open('wards.kml', 'r', encoding="utf-8")
doc = file.read()

k = kml.KML()
k.from_string(doc)
features = list(k.features())
place = list(features[0].features())
wards = list(place[0].features())

toronto = Point(43.6532, -79.3832)
print(toronto.within(wards[0].geometry))



