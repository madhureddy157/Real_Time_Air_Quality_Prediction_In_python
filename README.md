# Real-Time Air Quality Prediction using Python & ML

 Monitor and predict air quality in real-time using **sensors** and **machine learning models** (Random Forest & Decision Tree) on a **Raspberry Pi Zero 2W**. Data is visualized on **ThingSpeak** and displayed locally on an **LCD screen**.

---

##  Features

-  Real-time temperature, humidity, and gas level monitoring  
-  Air quality prediction using **Random Forest** & **Decision Tree**  
-  Algorithm selection via physical switches  
-  Data upload to **ThingSpeak**  
-  LCD display for live sensor data  
-  Low-cost, portable embedded system  

---

##  Hardware Components

|  Component           |  Description                                          |
|------------------------|---------------------------------------------------------|
| Raspberry Pi Zero 2W   | Main processor                                          |
| DHT11 Sensor           | Reads temperature & humidity                            |
| MQ-7 Sensor            | Detects carbon monoxide (CO)                            |
| MQ-135 Sensor          | Detects NH₃, NOₓ, smoke, alcohol, etc.                  |
| Nano Board             | Converts analog signals from MQ sensors to digital      |
| ESP8266 Module         | Wi-Fi connection to send data to ThingSpeak             |
| 16x2 LCD Display       | Displays real-time data and predictions                 |
| Switches (2x)          | Select ML model: Random Forest or Decision Tree         |
| Regulated Power Supply | Stable power source for system                          |

---

##  Machine Learning Models

-  **Random Forest Classifier**  
-  **Decision Tree Classifier**

Trained using labeled datasets of sensor readings and deployed on Raspberry Pi for real-time prediction.

---

##  System Architecture

```
MQ-7 & MQ-135 --> Nano Board (Serial) --> Raspberry Pi
                   DHT11 --------------->|
                          |
        [Raspberry Pi Zero 2W]
              |        |        |
         [LCD]    [ESP8266]  [ML Model]
                        |
                  ThingSpeak Cloud
```

---

##  How to Run

1.  Connect all hardware components to Raspberry Pi.  
2.  Power up the system.  
3.  Use switches to choose ML algorithm.  
4.  Run:

```bash
python3 main.py
```

5.  View data on LCD and 📡 check real-time values on [ThingSpeak](https://thingspeak.com).

---

##  ThingSpeak Integration

- Create a free channel at [thingspeak.com](https://thingspeak.com)  
- Add your Write API Key in the script  
- Data will be uploaded to your channel for real-time monitoring  

---


##  Team Members

- 👨‍💻 Madhusudhan G  
- 👩‍💻 Pavan Kumar A  
- 👨‍💻 BusiReddy Yaswanth
- 👨‍💻 Hemanth Kumar 


