# VickersPhotoDoc
This repository will help to process images from the Lake Vickers Photographic Evidence folder. The photos will be processed with python to match the metadata coordinates to GPS coordinates taken with Garmin GPS Map64. 

    Background:
I want to use Python to solve a time consuming project. I am a recent student of python programming and I really appreciated the    uses of programming lanquage. I had collected about 1200 pictures for a project in watershed field verification tecniques. I talked      with my professor about the project and professor Miller said I had a good project for Python. I was lucky to find a similar python project described by Eric Pimpler at http://geospatialtraining.com/extracting-geographic-coordinates-from-photos-using-python/ 
Much of my source code comes from the Eric Pimpler doc. I have tried to use my own wording and lanquage where I can. Still a lot 
of the text in my source code may be directly copied from the Pimpler. Mr. Pimpler describes the code (I may or may not have used different wording, but any likeness is credited to the Pimpler document: This custom tool in an ArcGIS Python toolbox loops through a list of location enabled photos taken with an iPhone and extracts the latitude, longitude coordinates stored with the metadat for each photo, reverse geocodes the cordinnates to obtain the nearest address, uploads the photo to a Dropbox account, and writes a new
point to feature class. I am working with Eric Pimpler's code and plan to edit that to my needs.

    Objective:
To apply Python programming to solve a task that can be done much quicker with Python
To apply Python to place photos on a map using metadata from photographic evidence collected during my special topics project:
Watershed Modeling and Field Verification Techniques on Lake Vickers and Lake Sydney Lanier. 
            
    Methods:    
Step 1. Import the various Python modules that will be used in this application. 
        I will use the standard libraries: shutil, os, sys, json, arcpy. 
        Additionally, non standard modules PILLOW, requests, and dropbox will be used.

Step 2. Uses the getParameterInfo() method is used to capture:# input parameters from the tool dialog,
        which captures the path to the photos, path to the file geodatabase to be created,
        file geodatabase name, and output feature class name. The getParameterInfo(self) defines 
        parameter definition: callable objects that can accept some argument and returns an object 
        such as a tuple. Four parameters are set. 
  
Step 3. Execute defines input parameters and sends them to makeGISpointsFRomPics() function
        after user clicks okay from the tool dialog. This is the source code of the tool, using an assignment operator
    
Step 4. The mapointfile(inPicFolder, path, fgdb, fc) is the code that will get the metadata
        from the photos and define the GPS coordinates to a map. 
    
Step 5. Creates a four loop that loops through the pictures exracts the geographic coordinates from 
         photo meta data and writes to a feature class so that the code can retrieve the exif data
    
Step 6. The get_exif_data(fn) function gets the exif data and uses PIL(we will use PILLOW a newer version) image, 
        converting the GPS to Tags

Step 7. Use the latitude and longitude coordinates which are retrieved from the metadata photographic evidence
    

Results:

Conclusion:

Acknowledgement: 
I would like to acknowledge my professor Zac Miller and alumni John P. Dees for their expertise and evaluation of my project and Eric Pimpler for sharing his coding.  
    
  
  


