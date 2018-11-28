from fastkml import kml
from shapely.geometry import Point, Polygon
import pandas as pd

KML_FILE = 'wards.kml'
TERMINAL_FILE = 'terminals.csv'
OUTPUT_FILE = 'terminals_and_wards.csv'

def initialize_wards(filename):
    """
    Open the .kml, parses it, and returns the list of wards.

    .kml:    https://www.google.com/maps/d/u/0/viewer?mid=1ZH7qeq9DUOy7C4KYBXvtn1EbiFrSkBSk&ll=43.65017152286006%2C-79.37985265290109&z=16
    fastkml: https://fastkml.readthedocs.io/en/latest/reference_guide.html
    """ 

    # Open and encode
    file = open(filename, 'r', encoding="utf-8")
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

    https://automating-gis-processes.github.io/2017/lessons/L3/point-in-polygon.html
    """

    bike_terminal = Point(lng, lat)  # Weird convention?

    # This is gross, but do it anyway
    for ward in wards:
        if bike_terminal.within(ward.geometry):
            return ward.name.split()[-1]  # Assumes it'll only fit into _one_ ward



ward_list = initialize_wards(KML_FILE)
df = pd.read_csv(TERMINAL_FILE)
df['Ward'] = df.apply(lambda row: which_ward(ward_list, row['Latitude'], row['Longitude']), axis=1)
df.to_csv(OUTPUT_FILE)
