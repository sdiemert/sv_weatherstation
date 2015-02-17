#Arduino Weather Station

This is the code for running the arduino weather station made at Science Venture. 

##Arduino

Code for the arduino is in sketch.ino file in arduino/. Open and download this in the Arduino IDE.

##Python Server

This is python code for the server. It runs in the local directory. There must be at least two files in the same directory as the server.py

* **index.html** which is the default file to be served.
* **style.css** contains css styles for index.html

To access data from the arduino include the correct tag within the HTML: 

* **{TEMP}** is replaced by the current temperature from the arduino.
* **{LIGHT}** is replaced by the current ambient light value from the arduino
* **{PRESSURE}** is replaced by the current pressure from the arduino.


