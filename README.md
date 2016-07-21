# python-samples
Python code samples



# HOW TO EXECUTE THE CODE

Make sure that you have Python 2.* and Python IDLE installed in your machine before you can run *.py file.




# Sample 1: Inheritance

There is only inheritance.py file in sample-1 folder. You can find two classes in the file, one is parent and another one is child. In which child inherit the behaviour and properties from the parent.

The execute this sample, use Python IDLE to run inheritance.py file. You will be the class properties printed on Python console.



# Sample 2: Check profanity words

There are two files in sample-2 folders: (1) check_profanity.py (2) movie-quotes.txt. check_profanity.py read the text content of movie-quotes.txt and then use online tools http://www.wdylike.appspot.com/?q= to check profanity words. Validation output will be printed in Python IDE console.

If profanity words are found, it will print "Profanity Alert!".



# Sample 3: Use pure Python code to create entertainment center

There are four files in sample-3 folder: (1) entertainment-center.py (2) media.py (2) fresh-tomatoes.py (4) fresh-tomatoes.html.
- media.py provides class and function to manage media content
- fresh-tomatoes.py consists of html web template and ability to create fresh_tomatoes.html file
- entertainment-center.py gets media information from media.py and then use fresh-tomatoes.py to create fresh-tomatoes.html file. To check the output, open fresh-tomatoes.html in your browser and you will see list of video content. Click on any item, video clip will be played. To watch the video clip, make sure that your computer is connected to internet because its contents derive from youtube.


# Sample 4: Use Python code to create SQL Alchemy database schema

There are two files in sample-4 folders: (1) database_setup.py (2) restaurantmenu.db. Run database_setup.py using Python IDLE, it will create a new restaurantmenu.db SQLite database file. Make sure that you have SQL Alchemy installed before you run the sample.

The objective of this sample is to explain how to use SQL Alchemy to create database schema and set relationship between two tables.



# Sample 5: Create a sample restaurant food menu using Python Flask and SQL Alchemy

Make sure that you have Python Flask and SQL Alchemy installed before you can start the web server (Python's built-in web server). You can start the built-in web server by executing project.py file. Once the web application is running, paste "http://localhost:8889/restaurants/2" into your bnrowser's address bar to test run application. You should be able to see list of food menu from a restaurant.
