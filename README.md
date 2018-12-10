# VickersPhotoDoc
This repository will help to process images from the Lake Vickers Photographic Evidence folder. The photos will be processed with the python to match the metadata coordinates to GPS coordinates taken with Garmin GPS Map64. 

This custom tool in an ArcGIS Python toolbox loops through a list of location
    enabled photos taken with an iPhone and extracts the latitude, longitude coordinates
    stored with the metadat for each photo, reverse geocodes the cordinnates to obtain
    the nearest address, uploads the photo to a Dropbox account, and writes a new
    point to feature class. I am working with Eric Pimpler's code and plan to edit that to my needs.
    
Step 1. of the code: Import the various Python modules that will be used in this application. 
  I will use the standard libraries: shutil, os, sys, json, arcpy. 
  Additionally, non standard modules PILLOW, requests, and dropbox will be used.

Step 2. Uses the getParameterInfo() method is used to capture:# input parameters from the tool dialog,
  which captures the path to the photos, path to the file geodatabase to be created,
  file geodatabase name, and output feature class name.
  
  The getParameterInfo(self) defines parameter definition: callable objects that can accept some argument
  and returen an object such as a tuple. Four parameters are set. 


