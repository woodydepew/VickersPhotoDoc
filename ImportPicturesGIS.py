#Import the various Python modules that will be used in this application.

import shutil
import os
import sys
import json
import arcpy
from PIL import Image
#PILLOW:https://python-pillow.org/
from PIL.ExifTags import TAGS, GPSTAGS
import requests
import dropbox

#Defines parameter definitions: these callable objects can accept some argument and return an object (often a tuple)

def getParameterInfo(self):
    """The getParameterInfo() method is used to capture
    input parameters from the tool dialog,
    which captures the path to the photos,
    path to the file geodatabase to be created,
    file geodatabase name, and output feature class name.
    """
    param0 = arcpy.Parameter(displayName = "Path to Pictures",
                             name="folderToImport",
                             datatype="DEFolder",
                             parameterType="Required",
                             direction="Input"
                             )
    
    param1 = arcpy.Parameter(displayName = "Path to File Geodatabase",
                             name="pathToFGDB",
                             datatype="DEFolder",
                             parameterType="Required",
                             direction="Input"
                             )
    
    param2 = arcpy.Parameter(displayName = "VickersPhotoDoc",
                             name="VickersPhotoDoc",
                             datatype="GPString",
                             parameterType="Required",
                             direction="Input"
                             )
    
    param3 = arcpy.Parameter(displayName = "Output Feature Class Name",
                             name="output_fc",
                             datatype="GPString",
                             parameterType="Required",
                             direction="Input"
                             )

    params = [param0, param1, param2, param3]
    return params

#This is the source code of the tool. We are using an assignment operator

def execute(Self, parameters, messages):
    """ execute defines input parameters and sends them to makeGISpointsFRomPics()
    function after user clicks okay from the tool dialog
    """
    inPicFolder = parameters[0].valueAsText
    path = parameters[1].valueAsText
    fgdb = parameters[2].valueAsText
    fc = parameters[3].valueAsText

    makeGISpointsFromPics (inPicFolder, path, fgdb, fc)

#Code makes the GPS point from picture metadata
    
def mappointfile(inPicFolder, path, fgdb, fc):
    """This is the code that will get the metadata from the photos
    and define the GPS coordinates to a map
    """
    arcpy.AddMessage("Building GIS points for geotagged photos")

    #Building a geodatabase
    createFGDB(path, fgdb, fc)
    dsc = arcpy.Describe(path + "\\" + fgdb + ".gdb" + "\\" + fc)
    shpFld = dsc.ShapeFieldName
    pics = os.listdir(inPicFolder)
    pics = [p for p in pics if p.endswith(".JPG") or p.endwith(".jpg")]

#Returns a dictionary from the exif data of a PIL (PILLOW) image and converts the GPS to Tags
    
def get_exif_data(fn):
    """ A four loop will be used to loop through the pictures,
    extract the geographic coordinates from the photo metadata
    Function get_exif_data uses PIL (code will need changed to PILLOW)
    module to open the picture metadata with GPS tags.
    Info is passed back to the get_exif_data()function.
    """
  
    image = Image.open(fn)

    exif_data = {}
    infor = image._getexif()
    if infor:
        for tag, value in infor.items():
            decoded = TAGS. get (tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = gps_data

                    exifPdata[decoded] = gps_data
                else:
                    exif_data[decoded] = value

    return exif_data

# Returns the latitude and longitude, if available, from the provided exif_data (coordinates)

def get_lat_lon(exif_data):    
    """ Defines the get_lat_lon() function retrieves the latitude, longitude
    Imports the various Python modules that will be used in this application.
    References information from the exif metadata and converts it
    from degrees, minutes, seconds to decimal degrees via
    a call to the _convert_to_degrees() function
    """

    lat = None
    lon = None

    if "GPSInfo" in exif_data:
        gps_info = exif_data["GPSInfo"]

        gps_latitude = _get_if_exist (gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, "GPSLatitudeRef")
        gps_longitude =  _get_if_exist (gps_info, "GPSLongitude")
        gps_longitude_ref = _get_if_exist(gps_info, "GPSLongitudeRef")

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degrees(gps_latitude)
            if gps_latitude_ref != "N":
                lat = 0 - lat

                lon = _convert_to_degrees (gps_longitude)
                if gps_longitude_re != "E":
                    lon = 0 - lon
    return lat, lon



    
                    

                

    
    
          
