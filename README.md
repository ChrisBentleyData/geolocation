# geolocation
Exercise to create a web service that can do some basic geolocation. A user needs to be told which US state contains a street address.

# Data Engineer Exercise - US State Geolocator

# Objective
Create a web service that can do some basic geolocation. A user needs to be told which US state contains a street address.

# Requirements
Load the US State shapefiles (available here) into a PostGIS-enabled instance of PosgreSQL. 
Create an API with (at minimum) the following functionality
An endpoint that accepts an address, converts it to a lat/long (using Google API), and finds which state contains that point
Upload your application to a public GitHub repository, and be sure to include a README instructing a user how to run and use the application.

# Suggestions
No UI is necessary for this project. A simple web server that can be accessed via a REST client (such as Postman) is sufficient. 

You’ll need to convert the .shp files from the Census Bureau into a format ingestible by PostgreSQL. There’s plenty of documentation available online that can help with this. 
