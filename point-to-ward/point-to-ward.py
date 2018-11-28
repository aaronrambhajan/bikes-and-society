from fastkml import kml
from shapely.geometry import Point, Polygon
import pandas as pd

def kml_to_wards():
    """
    Opens the .kml, parses it, and returns the list of wards.
    """

    # Open and encode
    file = open('wards.kml', 'r', encoding="utf-8")
    doc = file.read()

    # Read into KML
    k = kml.KML()
    k.from_string(doc)

    # Traverse the KML to ward lists
    features = list(k.features())
    place = list(features[0].features())
    wards = list(place[0].features())

    return wards


def which_ward(wards, lat, lng):
    """
    Takes the `wards` list, and the `lat`/`lng` of the terminal, outputs
    the ward it belongs to.
    """
    
    bike_terminal = Point(lng, lat) # Weird convention?

    # This is gross, but do it anyway
    for ward in wards:
        if bike_terminal.within(ward.geometry):
            print(ward.name)


def read_terminals(filename):
    pass


wards = kml_to_wards()
which_ward(wards, 43.6532, -79.3832)

