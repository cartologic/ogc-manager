# -*- coding: utf-8 -*-
import re
from collections import namedtuple

from django.conf import settings
from slugify import Slugify

from . import DOWNLOADS_PATH, TEMP_PATH

FORMAT_EXT = {
    "GPKG": '.gpkg',
    "KML": '.kml',
    "GeoJSON": '.json',
    "GML": '.gml',
    "GPX": '.gpx',
    "GPSTrackMaker": ".gmt",
    "ESRI Shapefile": ".shp"
}
PG_REGEX = re.compile(r"^\s?PG:\s?.*$")
WORLD_PERMISSION = 0o777
USER_GROUP_PERMISSION = 0o775
DEFAULT_WORKSPACE = settings.DEFAULT_WORKSPACE
SLUGIFIER = Slugify(separator='_')
STYLES_TABLE = "layer_styles"
ICON_REL_PATH = "workspaces/{}/styles".format(DEFAULT_WORKSPACE)
LayerPostgisOptions = namedtuple(
    'LayerPostgisOptions', ['skipfailures', 'overwrite', 'append', 'update'])
POSTGIS_OPTIONS = LayerPostgisOptions(True, True, False, False)
TEMP_DIR_PATH = TEMP_PATH
DOWNLOADS_DIR_PATH = DOWNLOADS_PATH
