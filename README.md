# VickersPhotoDoc
This repository will help to process images from the Lake Vickers Photographic Evidence folder. The photos will be processed with python to match the metadata coordinates to GPS coordinates taken with Garmin GPS Map64. 

    Background:
I want to use Python to solve a time consuming project. I am a recent student of python programming and I really appreciated the uses of programming language. I had collected about 1200 pictures for a project in watershed field verification techniques. I talked with my professor about the project and Professor Miller said I had a good project for Python. I was lucky to find a similar python project described by Eric Pimpler at http://geospatialtraining.com/extracting-geographic-coordinates-from-photos-using-python/ 
Much of my source code comes from the Eric Pimpler doc. I have tried to use my own wording and language where I can. Still a lot 
of the text in my source code may be directly copied from the Pimpler. Mr. Pimpler describes the code (I may or may not have used different wording, but any likeness is credited to the Pimpler document: This custom tool in an ArcGIS Python toolbox loops through a list of location enabled photos taken with an iPhone and extracts the latitude, longitude coordinates stored with the metadata for each photo, reverse geocodes the coordinates to obtain the nearest address, uploads the photo to a Dropbox account, and writes a new
point to feature class. I am working with Eric Pimpler's code and plan to edit that to my needs.

    Objective:
To apply Python programming to solve a task that can be done much quicker with Python
To apply Python to place photos on a map using metadata from photographic evidence collected during my special topics project:
Watershed Modeling and Field Verification Techniques on Lake Vickers and Lake Sydney Lanier. 
            
    Methods:    
Step 1. Import the various Python modules that will be used in this application. 
        I will use the standard libraries: shutil, os, sys, json, arcpy. 
        Additionally, nonstandard modules PILLOW, requests, and Dropbox will be used.

Step 2. Uses the getParameterInfo() method is used to capture:# input parameters from the tool dialog,
        which captures the path to the photos, path to the file geodatabase to be created,
        file geodatabase name, and output feature class name. The getParameterInfo(self) defines 
        parameter definition: callable objects that can accept some argument and returns an object 
        such as a tuple. Four parameters are set. 
  
Step 3. Execute defines input parameters and sends them to makeGISpointsFRomPics() function
        after user clicks okay from the tool dialog. This is the source code of the tool, using an assignment operator
    
Step 4. The mapointfile(inPicFolder, path, fgdb, fc) is the code that will get the metadata
        from the photos and define the GPS coordinates to a map. 
    
Step 5. Creates a four loop that loops through the pictures extracts the geographic coordinates from 
         photo meta data and writes to a feature class so that the code can retrieve the exif data
    
Step 6. The get_exif_data(fn) function gets the exif data and uses PIL(we will use PILLOW a newer version) image, 
        converting the GPS to Tags and passed back to the get_exif_data() function, returning as a dictionary. Use "if" "for" and "else"         statements. 

Step 7. Use the latitude and longitude coordinates which are retrieved from the metadata photographic evidence get_lat_lon() function.
        Returns a list object to retrieve the individual latitude and longitude values.
        
Step 8. Defines the get_lat_lon() function, retrieving the latitude, longitude imports the various Python modules that will be used in           the application and references information from the exif metadata and converts it form degrees, minutes, seconds to decimal             degrees via a call to the _conver_to_degrees() function

Step 9. Uses reverse Geocoding from the makeGISpointFromPics() function to retrieve point and send the photo to Dropbox. I am not able 
        to use dropbox at this time but it will be useful when this project is applied to an online platform. Additionally, nearest               address is not very important for me, but it don't hurt either. The call to the getAddress() function passes in the latitude,           longitude values retrieved from the photo metadata. The getAddress() function uses the Python requests module to send the                 coordinate information to the Esri World Geocoding Service: 
        https://developers.arcgis.com/rest/geocode/api-reference/overview-world-geocoding-service.htm
        The distance value specifies the maximum distance (in meters) to use when searching for the nearest address. I would like my code         to match to my GPS point location. Data will be returned by the reverse geocoding operation in json format.
        
Step 10. The sendPhotoDropbox() function makes a connection to a Dropbox account using the Python Dropbox module and uploads the file. 
         At this time, I do not have the funds to upload the photos to my Dropbox account.
         
Step 11. Uses ArcPy to create a new Point object from the extracted latitude, longitude coordinates and inserts this object into the              feature class using an InsertCursor object. Several attributes including the address are inserted into the row. 

    Results:
This python program creates a custom tool in an ArcGIS toolbox, looping through a list of location enabled photos taken with an iPhone and extracts the latitude, longitude coordinates stored with the metadata for each photo, reverse geocodes the coordinates to obtain the nearest address, uploads the phot to a Dropbox account, and writes a new point to feature class. The results are: I do not have the ability to create extra Dropbox storage at this time. Therefore, this code is a work in progress and I hope to continue to make progress in python coding and this project. 

    Conclusion:
I have made the attempt to create python code to perform a task. I found resources from google, which provide a frame work into the coding necessary to begin the task. I think this is a worthy project and one I intend to complete. I can't wait to see the results when I get it to work. The code that I borrowed from is incomplete just enough to make me want to pay for the book. 

    Acknowledgement: 
I would like to acknowledge my professor Zac Miller and alumni John P. Dees for their expertise and evaluation of my project and Eric Pimpler for sharing his coding.  
    
    References:
Pimpler, Eric. "Using Python to Extract Geographic Coordinates from iPhone Photos." Geospatial Training Services. geospatialtraining.com. google search. Accessed: 12, 1, 2018. http://geospatialtraining.com/extracting-geographic-coordinates-from-photos-using-python/
Pimpler, Eric. "Introduction to Programming the Google Maps API(v3)." GeoSpatial Training Services. google search. Accessed: 12, 10, 2018. http://geospatialtraining.com/introduction-to-programming-the-google-maps-api-v3/
Google Developers. "Python installation." Developers Guid. Google Earth Engine API. google search. Accessed: 12, 10, 2018.      
  
  


