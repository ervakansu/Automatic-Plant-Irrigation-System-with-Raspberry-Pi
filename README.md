# Automatic-Plant-Irrigation-System-with-Raspberry-Pi
A plant irrigation system was designed w/ Python PL and Raspberry Pi 3A+

In my project, my goal was to provide the water needs of various plants in different time periods in an automatic way. As we all know, not all kinds of plants need the same amount of water or the same time periods.
I used an RGB color sensor for the system to understand the plant varieties. Thus, I have provided a color code for all kinds of plants. According to the platform I set, I first checked the plant with the color sensor, when it was time to be watered. So even if you change the place of the pots, the system will water the right plant. Afterwards, I checked whether the plant needed watering with the soil moisture sensor, so that the plant was watered or the motor returned to the starting point without irrigation. My purpose in doing this is to put our platform in sometimes very sunny and sometimes dark environments. This will affect the moisture of the soil.
I designed my platform for watering 3 different kinds of plants. The color sensor can detect colors in bright and dark environments in different colors than they should be. You can avoid this situation with more specific color codes in Python.

MATERIAL LIST

1 RGB Color Sensor https://learn.adafruit.com/adafruit-color-sensors/python-circuitpython

1 Stepper Motor

3 Soil Moisture Sensor (optional)

Rasberry Pi 3A+

12V DC Peristaltic Dosing Water Pump

You can watch my Youtube video at the link below to get some detailed information about how the project works.

https://www.youtube.com/watch?v=oTiviFv06XM
