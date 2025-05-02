# Real-Time-Air-Quality-Prediction-In-python
Real time air quality prediction using sensors and Machine Learning Algorithms [Random Forest and Decision Tree]


The sensors DHT11, MQ-7 and MQ-135 are used to get humidity, temperature, C02 
and air quality values. DHT 11 is interfaced to raspberry pi zero 2w directly as it gives digital values 
which could be read by Raspberry Pi. MQ7 and MQ135 are interfaced to a nano board which converts 
analog values to digital values and then to serial values which could be read by raspberry pi. 
Raspberry Pi zero 2W processes the data and then displays that data on to the Thing Speak using Wi- 
Fi module ESP8266. The same is displayed on LCD. There are also 2 switches to select which 
algorithm we prefer between Random Forest and Decision Tree algorithms. 
