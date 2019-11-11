# Geolocation Exercise
Exercise to create a web service that can do some basic geolocation. A user needs to be told which US state contains a street address.

# Data Engineer Exercise Description - US State Geolocator

## Objective
Create a web service that can do some basic geolocation. A user needs to be told which US state contains a street address.

## Requirements
Load the US State shapefiles (available here) into a PostGIS-enabled instance of PosgreSQL. 
Create an API with (at minimum) the following functionality
An endpoint that accepts an address, converts it to a lat/long (using Google API), and finds which state contains that point
Upload your application to a public GitHub repository, and be sure to include a README instructing a user how to run and use the application.

## Suggestions
No UI is necessary for this project. A simple web server that can be accessed via a REST client (such as Postman) is sufficient. 

You’ll need to convert the .shp files from the Census Bureau into a format ingestible by PostgreSQL. There’s plenty of documentation available online that can help with this. 

# How to Setup and run the application
Note: This application is a work in progress and is not production ready. Updates will be made to include better error handling, addditonal enhancements and configuration file usage.

## Set up Environment
### 1. Set up database
   - Restore the table "cb_2018_us_state500k2" into your own PostGIS-enabled instance of PosgreSQL. A dump of the table has been provide in the folder database.
   
     or
     
   - Load the US State Shapefiles (also provided) into a PostGIS-enabled instance of PosgreSQL.
### 2. Edit and download python scripts
   - myprocessor.py - This process the input from the webservice. Edit and save this script at the top to provide the following:
     - google_api_key - A google API Key  which is enabled to use the Geocoding API
     - dbname - The name of the PosgreSQL DB that has the shape table
     - user - PosgresSQL User that has permissions on the shape table
     - password - PosgreSQL password
     - shape_table - The fully identified shape table that was established in step 1.
     
   - ws.py - This is webservice script
### 3. Start the webservice
   - The webservice runs on localhost. Start it by running the script ws.py
### 4. Call the service (POST)
   - The service for Geo Location is called "process" - http://localhost:8080/process
   - The service expects as input a json formatted in the following way: {"addr": "123 Any Street, Anytown, AnyState"}
   - The return is json: {\"State\":{\"0\":\"AnyState\"}}
   
## Example using cURL
Executing the following cURL command:

curl -d '{"addr": "3535 Piedmont Rd NE, Atlanta, GA 30305"}' -H "Content-Type: application/json" -X POST http://localhost:8080/process

We would get the following response:

{\"State\":{\"0\":\"Georgia\"}}



   

