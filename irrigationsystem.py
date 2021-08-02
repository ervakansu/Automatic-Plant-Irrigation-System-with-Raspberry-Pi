import time
import board
import busio
import adafruit_tcs34725
import numpy as np
import datetime
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#Stop coming out Warnings
GPIO.setwarnings(False)

c1yok="No Water Detected!"
c1var="Water Detected!"
c1_durumu = ""
#nem_durumu = bool

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)
sensor.integration_time = 100
#renk_listem=[]

def DetectControlPanelColor():
    colors = sensor.color_rgb_bytes
    r = np.floor(colors[0]/20)
    g = np.floor(colors[1]/20)
    b = np.floor(colors[2]/20)
    if ( r > 0 and g == 0 and b == 0):
        return [1, 0, 0, 0, 0]
    if (r == 0 and g > 0 and b == 0):
        return [0, 1, 0, 0, 0]
    if (r == 0 and g >= 0 and b > 0):
        return [0, 0, 1, 0, 0]
    if (r > 0 and g > 0 and b == 0):
        return [0, 0, 0, 1, 0]
    if r == 0 and b == 0 and g == 0:
        return [0, 0, 0, 0, 1]
    
    return [0, 0, 0, 0, 0]

def DetectionToColorName(colors):
    if (colors[0]): return "Red"
    elif (colors[1]): return "Green"
    elif (colors[2]): return "Blue"
    elif (colors[3]): return "Yellow"
    elif (colors[4]): return "Black"
    else: return "No Color Detected"
    
    
#while True:
#colordet = DetectControlPanelColor()
#for i in range(10):
  #  renk_listem.append(DetectionToColorName(colordet))
    #print(DetectionToColorName(colordet))
    #print(renk_listem)
    

###################################
                   
                
enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

GPIO.output(enable_pin, 1)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,GPIO.LOW)

def backwards(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)
def forward(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 0,1)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)
       
def setStep(w1, w2, w3, w4):
    
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
    
    
# 18:00  - 
    # 60 adım tam tur ..
    # 20 adım ileri
    # Renk kontrol 
        # Renk doğru değilse ; 20 adım geri
    # Renk doğruysa; Nem kontrol
        # Nem varsa 40 adım ileri
        # Nem yoksa sulama yap. 40 adım ileri    

channel1 = 21 #mor
channel2=25 #turuncu
channel3=20 #nem sensorleri kahve

GPIO.setup(channel1, GPIO.IN)
GPIO.setup(channel2, GPIO.IN)
GPIO.setup(channel3, GPIO.IN)
 

selectedChannel=0

#nem_durumu = bool()
def mycallback_one(channel1):
     # assign function to GPIO PIN, Run function on change
    
    if GPIO.input(channel1):
        c1_durumu = c1yok        
    else:
        c1_durumu = c1var        
    return c1_durumu  


GPIO.add_event_detect(channel1, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel1, callback=mycallback_one)



def mycallback_two(channel2):
     # assign function to GPIO PIN, Run function on change
    
    if GPIO.input(channel2):
        c1_durumu = c1yok        
    else:
        c1_durumu = c1var        
    return c1_durumu  


GPIO.add_event_detect(channel2, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel2, callback=mycallback_two)
#while True:
    #callback(channel1)
    #print(callback(channel1))      


def mycallback_three(channel3):
     # assign function to GPIO PIN, Run function on change
    
    if GPIO.input(channel3):
        c1_durumu = c1yok        
    else:
        c1_durumu = c1var        
    return c1_durumu  


GPIO.add_event_detect(channel3, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel3, callback=mycallback_two)
#while True:
    #callback(channel1)
    #print(callback(channel1))      
 
   
def sulama_yap():
    print("Sulama Başladı")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12,GPIO.OUT)
    GPIO.output(12,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(12,GPIO.LOW)
    #GPIO.cleanup()    
    print("Sulama tamamlandı.")
    
#while True:
    
    
x = datetime.datetime.now()
print(x.strftime("%H:%M"))  
    
    # saat 18 olduysa step motoru calistir
if x.strftime("%H:%M") == "02:20":
    print("Saati geldi..")
    delay = 10
    coil_A_1_pin = 4
    coil_A_2_pin = 17
    coil_B_1_pin = 23
    coil_B_2_pin = 24
    GPIO.setup(enable_pin, GPIO.OUT)
    GPIO.setup(coil_A_1_pin, GPIO.OUT)
    GPIO.setup(coil_A_2_pin, GPIO.OUT)
    GPIO.setup(coil_B_1_pin, GPIO.OUT)
    GPIO.setup(coil_B_2_pin, GPIO.OUT)

    #step motor ileriye dogru 20 adim atsin
    GPIO.setmode (GPIO.BCM)
    GPIO.setup(enable_pin, GPIO.OUT)
    GPIO.output(enable_pin, 1)
    steps = 40
    forward(int(delay) / 1000.0, int(steps))
    time.sleep(10)
    #renk kontrolu yap
    colordet = DetectControlPanelColor()
    print(DetectionToColorName(colordet))
    #renk kontrolu dogru ise
    if DetectionToColorName(colordet)=="Red":
        time.sleep(10)
        GPIO.output(enable_pin, 0)
        steps = 0
        print("red-stop")
        #nem kontrol etmeye basla
        #kontrol ettigi ilk kanal ise yesile ait olan
        if(mycallback_one(channel1)=="Water Detected!"):
            time.sleep(10)
            print("Nem algılandı.")
            #degilse 40 adım ileri gidip basa don
                
            GPIO.setmode (GPIO.BCM)
            GPIO.setup(enable_pin, GPIO.OUT)
            GPIO.output(enable_pin, 1)
            steps = 50
            backwards(int(delay) / 1000.0, int(steps))
            GPIO.output(enable_pin, 0)
            steps=0
             
        else:
            print("Nem yok - ")
            #bool degeri 0 ise sulama yap
            sulama_yap()
            #sulama yaptiktan sonra basa don
            #setStep(w1, w2, w3, w4)
            GPIO.setup(enable_pin, GPIO.OUT)
            GPIO.setmode (GPIO.BCM)
                
            GPIO.output(enable_pin, 1)
            steps =50
            backwards(int(delay) / 1000.0, int(steps))
            GPIO.output(enable_pin, 0)
            steps=0
                
    else:
        print("Aranılan renk bulunamadı")
        GPIO.output(enable_pin, 1)
        steps =50
        backwards(int(delay) / 1000.0, int(steps))
        GPIO.output(enable_pin, 0)
        steps=0
                    
 ##########################   

if x.strftime("%H:%M") == "02:38":
    print("Saati geldi..")
    
    
    coil_A_1_pin = 4
    coil_A_2_pin = 17
    coil_B_1_pin = 23
    coil_B_2_pin = 24
    GPIO.setup(enable_pin, GPIO.OUT)
    GPIO.setup(coil_A_1_pin, GPIO.OUT)
    GPIO.setup(coil_A_2_pin, GPIO.OUT)
    GPIO.setup(coil_B_1_pin, GPIO.OUT)
    GPIO.setup(coil_B_2_pin, GPIO.OUT)

    delay = 10
    #step motor ileriye dogru 20 adim atsin
    GPIO.setmode (GPIO.BCM)
    GPIO.setup(enable_pin, GPIO.OUT)
    GPIO.output(enable_pin, 1)
    steps = 90
    forward(int(delay) / 1000.0, int(steps))
    time.sleep(10)
    #renk kontrolu yap
    colordet = DetectControlPanelColor()
    print(DetectionToColorName(colordet))
    #renk kontrolu dogru ise
    if DetectionToColorName(colordet)=="Green":
        time.sleep(10)
        GPIO.output(enable_pin, 0)
        steps = 0
        print("green-stop")
        #nem kontrol etmeye basla
        #kontrol ettigi ilk kanal ise yesile ait olan
        if(mycallback_two(channel2)=="Water Detected!"):
            channel2=25;
            #GPIO.remove_event_detect(channel1)
            #GPIO.add_event_detect(channel2, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
            #GPIO.add_event_callback(channel2, callback)
            time.sleep(10)
            print("Nem algılandı.")
            #degilse 40 adım ileri gidip basa don
                
            GPIO.setmode (GPIO.BCM)
            GPIO.setup(enable_pin, GPIO.OUT)
            GPIO.output(enable_pin, 1)
            steps = 90
            backwards(int(delay) / 1000.0, int(steps))
            GPIO.output(enable_pin, 0)
            steps=0
             
        else:
            print("Nem yok - ")
            #bool degeri 0 ise sulama yap
            sulama_yap()
            #sulama yaptiktan sonra basa don
            #setStep(w1, w2, w3, w4)
            GPIO.setup(enable_pin, GPIO.OUT)
            GPIO.setmode (GPIO.BCM)
                
            GPIO.output(enable_pin, 1)
            steps =90
            backwards(int(delay) / 1000.0, int(steps))
            GPIO.output(enable_pin, 0)
            steps=0
                
    else:
        print("Aranılan renk bulunamadı")
        GPIO.output(enable_pin, 1)
        steps =90
        forward(int(delay) / 1000.0, int(steps))
        GPIO.output(enable_pin, 0)
        steps=0
        
        
##########

x = datetime.datetime.now()
print(x.strftime("%H:%M"))  
    
    # saat 18 olduysa step motoru calistir
if x.strftime("%H:%M") == "02:20":
    print("Saati geldi..")
    delay = 10
    coil_A_1_pin = 4
    coil_A_2_pin = 17
    coil_B_1_pin = 23
    coil_B_2_pin = 24
    GPIO.setup(enable_pin, GPIO.OUT)
    GPIO.setup(coil_A_1_pin, GPIO.OUT)
    GPIO.setup(coil_A_2_pin, GPIO.OUT)
    GPIO.setup(coil_B_1_pin, GPIO.OUT)
    GPIO.setup(coil_B_2_pin, GPIO.OUT)

    #step motor ileriye dogru 20 adim atsin
    GPIO.setmode (GPIO.BCM)
    GPIO.setup(enable_pin, GPIO.OUT)
    GPIO.output(enable_pin, 1)
    steps = 140
    forward(int(delay) / 1000.0, int(steps))
    time.sleep(10)
    #renk kontrolu yap
    colordet = DetectControlPanelColor()
    print(DetectionToColorName(colordet))
    #renk kontrolu dogru ise
    if DetectionToColorName(colordet)=="Blue":
        time.sleep(10)
        GPIO.output(enable_pin, 0)
        steps = 0
        print("blue-stop")
        #nem kontrol etmeye basla
        #kontrol ettigi ilk kanal ise yesile ait olan
        if(mycallback_one(channel3)=="Water Detected!"):
            channel3=20;
            time.sleep(10)
            print("Nem algılandı.")
            #degilse 40 adım ileri gidip basa don
                
            GPIO.setmode (GPIO.BCM)
            GPIO.setup(enable_pin, GPIO.OUT)
            GPIO.output(enable_pin, 1)
            steps = 140
            backwards(int(delay) / 1000.0, int(steps))
            GPIO.output(enable_pin, 0)
            steps=0
             
        else:
            print("Nem yok - ")
            #bool degeri 0 ise sulama yap
            sulama_yap()
            #sulama yaptiktan sonra basa don
            #setStep(w1, w2, w3, w4)
            GPIO.setup(enable_pin, GPIO.OUT)
            GPIO.setmode (GPIO.BCM)
                
            GPIO.output(enable_pin, 1)
            steps =140
            backwards(int(delay) / 1000.0, int(steps))
            GPIO.output(enable_pin, 0)
            steps=0
                
    else:
        print("Aranılan renk bulunamadı")
        GPIO.output(enable_pin, 1)
        steps =140
        backwards(int(delay) / 1000.0, int(steps))
        GPIO.output(enable_pin, 0)
        steps=0            

else:
    print("Saat gelmedi..")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(enable_pin, GPIO.OUT)
    GPIO.output(enable_pin, 0)
    steps = 0
    print("calismaz")
    #steps = input("Geri kac adim? ")
    #backwards(int(delay) / 1000.0, int(steps))
        
 ##########################   



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




