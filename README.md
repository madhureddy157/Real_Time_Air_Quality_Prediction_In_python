🌫️ Real-Time Air Quality Prediction in Python:
This project focuses on real-time air quality monitoring and prediction using sensors and machine learning algorithms (Random Forest and Decision Tree). It uses a Raspberry Pi Zero 2W as the core processor, interfaced with environmental sensors, and transmits data to ThingSpeak for cloud visualization.

📌 Features:
Real-time air quality monitoring

ML-based prediction using Random Forest & Decision Tree

Sensor data display on LCD

Cloud logging via ThingSpeak

Physical switch to select algorithm

Portable and low-cost system

🧠 Machine Learning Algorithms:
Random Forest Classifier

Decision Tree Classifier

These models are trained on collected sensor data and deployed on the Raspberry Pi to predict the air quality index (AQI) or pollutant levels.

🧰 Hardware Components Used:
Component	                                Function
Raspberry Pi Zero 2W	               Main processing unit
DHT11 Sensor	                       Measures temperature and humidity
MQ-7 Sensor	                         Detects Carbon Monoxide (CO)
MQ-135 Sensor	                       Detects NH3, NOx, alcohol, benzene, smoke, etc.
Nano Board	                         Converts analog sensor values to digital via serial
ESP8266 Wi-Fi Module	               Sends data to ThingSpeak
LCD Display (16x2)	                 Displays current readings and predictions
2x Switches	                         Select between Decision Tree or Random Forest algorithm


🖥️ System Architecture:
DHT11 → Digital data → Raspberry Pi

MQ-7 & MQ-135 → Analog data → Nano Board → Serial to Raspberry Pi

Raspberry Pi:

Collects data

Predicts air quality using selected ML model

Displays results on LCD

Sends data to ThingSpeak via ESP8266

