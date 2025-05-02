
import RPi.GPIO as GPIO
import time, sys, os

import serial

import datetime
from sklearn.ensemble import RandomForestRegrssor
from sklearn.ensemble import DecisionTree
from time import sleep

import Adafruit_DHT



def main():
  lcd_init()
 
  lcd_string("  Welcome To",LCD_LINE_1)
  lcd_string("The project ",LCD_LINE_2)
  time.sleep(1) # 700 milli second delay

  GPIO.output(led, True) # LED
  time.sleep(0.7) # 700 milli second delay
  GPIO.output(led, False) # LED
  time.sleep(0.7) # 700 milli second delay  
  GPIO.output(led, True) # LED
  time.sleep(0.7) # 700 milli second delay
  GPIO.output(led, False) # LED
  k = 0
  
  hb = 0
  ser.flush()
  ser.flush()
  ser.flush()
  count = 0
  flag = 0
  while True:
          

        received_data = (str)(ser.readline())                   #read NMEA string received        
        print "Data received"
        
        humidity, temperature = Adafruit_DHT.read_retry(11, 18)
        buf = str("T:%0.1f C"%(temperature))
        buf1 = str("H:%0.1f "%(humidity))
        print buf
        print buf1
        

        if len(received_data) > 3:
            print(received_data)
            data = received_data.split(',')

            mq7 = int(data[0])
            mq135 = int(data[1])
            
            string1 = "AQ:"+data[0]+"PPM "+buf
            string2 = "M7:"+str(mq135)+"PPM "+buf1

            lcd_byte(0x01, LCD_CMD)
            lcd_string(string1,LCD_LINE_1) #commands.getoutput('hostname -I')
            lcd_string(string2,LCD_LINE_2) #commands.getoutput('hostname -I')
            time.sleep(1)
            
            data = str(humidity)+","+str(temperature)+","+str(mq135)+","+str(mq7)
            
            ser.write(received_data)
            ser.write("\r\n")
            count = count+1
            
            if(count > 25):
                flag = 1
            perc = 0
            if not GPIO.input(sw1):                             
                        
                if flag == 1:
                                  
                    lcd_byte(0x01, LCD_CMD)
                    lcd_string("Decision Tree Alg:",LCD_LINE_1) #commands.getoutput('hostname -I')
                    time.sleep(1)
                    lcd_string("Loading ",LCD_LINE_2) #commands.getoutput('hostname -I')
                    time.sleep(2)

                    if humidity < 50:                                    
                        lcd_byte(0x01, LCD_CMD)
                        lcd_string("Weather Condition:",LCD_LINE_1) #commands.getoutput('hostname -I')
                        lcd_string("     Normal   ",LCD_LINE_1) #commands.getoutput('hostname -I')
                        time.sleep(1)
                    else:
                        regressor = RandomForestRegrssor(n_estimators = 100, random_state = 0)
                        
                        perc = regressor.fit(humidity,temperature,mq135,mq7)
                                                   
                        
                        rain = "Rain: "+str(perc)+" %"
                        lcd_byte(0x01, LCD_CMD)
                        lcd_string("Weather Condition:",LCD_LINE_1) #commands.getoutput('hostname -I')
                        lcd_string(rain,LCD_LINE_1) #commands.getoutput('hostname -I')
                        time.sleep(1)
                else:                   
                    lcd_byte(0x01, LCD_CMD)
                    lcd_string("Need More Samples",LCD_LINE_1) #commands.getoutput('hostname -I')
                    time.sleep(1)
                    
            
            if not GPIO.input(sw2):
                                    
                        
                if flag == 1:
                       
                    lcd_byte(0x01, LCD_CMD)
                    lcd_string("Random forest Alg:",LCD_LINE_1) #commands.getoutput('hostname -I')
                    time.sleep(1)
                    lcd_string("Loading ",LCD_LINE_2) #commands.getoutput('hostname -I')
                    time.sleep(2)

                    if humidity < 50:                                    
                        lcd_byte(0x01, LCD_CMD)
                        lcd_string("Weather Condition:",LCD_LINE_1) #commands.getoutput('hostname -I')
                        lcd_string("     Normal   ",LCD_LINE_1) #commands.getoutput('hostname -I')
                        time.sleep(1)
                    else:
                        regressor = DesicionTree(n_estimators = 100, random_state = 0)
                        
                        perc = regressor.fit(humidity,temperature,mq135,mq7)
                        
                        rain = "Rain: "+str(perc)+" %"
                        lcd_byte(0x01, LCD_CMD)
                        lcd_string("Weather Condition:",LCD_LINE_1) #commands.getoutput('hostname -I')
                        lcd_string(rain,LCD_LINE_1) #commands.getoutput('hostname -I')
                        time.sleep(1)
                else:                   
                    lcd_byte(0x01, LCD_CMD)
                    lcd_string("Need More Samples",LCD_LINE_1) #commands.getoutput('hostname -I')
                    time.sleep(1)
                        

        time.sleep(0.3) # 700 milli second delay

if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Please Restart...",LCD_LINE_1)
    GPIO.cleanup()
      
      
        


