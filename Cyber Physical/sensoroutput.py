import mraa,time
import subprocess
import platform
from TH02 import TH02 # import temp and humidity command
from I2cLCDRGBBacklight import I2cLCDDisplay
from Servo import *

soilSensor = mraa.Aio(0)
uvSensor = mraa.Aio(1)
lightSensor = mraa.Aio(2)
led = mraa.Gpio(13)
led.dir(mraa.DIR_OUT)
thSensor = TH02()

# print(str(soilSensor.read()))
# print(str(uvSensor.read()))
# print(str(lightSensor.read()))  # assumption is output is in lumins

while True:
    light = str(lightSensor.read())
    uv = str(uvSensor.read())
    moist = str(soilSensor.read())
    tmp = str(round(thSensor.getTemperature(), 1))
    hum = str(round(thSensor.getHumidity(), 1))

    print("UVSensor: " + uv + ", Office Light: " + light + ", Soil:" + moist + ", Temp:" + tmp + ", Humidity:" + hum )

    cmd_srv = 'logger --udp --port 51514 --server splunkhome.myddns.me IoTid="QLD-A" ' + platform.node()
    cmd_var = ' UVSensor=' + uv + ', Office Light=' + light + ', Soil=' + moist + ', Temp=' + tmp + ', Humid=' + hum
    cmd_str = cmd_srv + cmd_var
    subprocess.call(cmd_str, shell=True)

    for x in range(30):
        led.write(1)
        time.sleep(1)
        led.write(0)
        time.sleep(1)

# aaarrrggg preset capitalised variables are shit!@!!!!!!!@!
def LCDInstruction(instruction):
    LCD.writeReg(0x80,instruction)
    time.sleep(0.05)
    return

def I2cLCDInit():
    LCD = mraa.I2c(0)
    LCD.address(0x3e)
    LCD.writeReg(0x80,0x38)                 #8Bit, 2lines, 5x7
    time.sleep(0.05)
    LCD.writeReg(0x80,0x08+0x07)    #display on, cursor on, blink on
    time.sleep(0.05)
    LCD.writeReg(0x80,0x01)                 #clear display, cursor 1st line, 1st character
    return(LCD)

def I2cLCDLEDInit():
    LCDLED = mraa.I2c(0)
    LCDLED.address(0x62)
    LCDLED.writeReg(0,0)
    LCDLED.writeReg(1,0)
    LCDLED.writeReg(0x08,0xaa)
    return(LCDLED)


def LCDPrint(text):
    for letter in text:
        LCD.writeReg(0x40,ord(letter))
    return

def LEDColor(R,G,B):
    LCDLED.writeReg(4,R)
    LCDLED.writeReg(3,G)
    LCDLED.writeReg(2,B)
    return


LCD = I2cLCDInit()  # start screen/display
LCDLED = I2cLCDLEDInit()  # start the rgb display backlight
LEDColor(32,32,32)  # background colour whtie = 255,255,255
LCDPrint("We are Women Hear us Roar!")
LCDDisplay = I2cLCDDisplay()
myServo = Servo("First Servo")
myServo.attach(6)
LCDInstruction(0x80+0x28)  # next line, first character point
LCDPrint("Smart Farm Prototyping")
time.sleep(1)
LEDColor(32,32,32)
time.sleep(1)

while True:                                     #Main loop
    lightSensor = mraa.Aio(2)               #Light Sensor analogue input 2
    LEDColor(128,255,128)
    LCDDisplay.LCDInstruction(0x01)
    LCDDisplay.LCDPrint("Light Sensor:")
    LCDDisplay.LCDInstruction(0x80 + 0x28)
    # try to reduce the Light Number to a value between 1 and 90
    light = int(lightSensor.read()/10)
    # old value - LCDDisplay.LCDPrint(str(lightSensor.read()))
    LCDDisplay.LCDPrint(str(light))
    myServo.write(light)
    time.sleep(1)
    print("Loopping")

print("Loop successful")

# testing the servo motions

# Create a new servo object with a reference name
myServo2 = Servo("Second Servo")

# Attaches the servo to pin 6 in Arduino Expansion board - Base Boad Con: D6
myServo2.attach(6)

# Print servo settings
print ""
print "*** Servo Initial Settings ***"
print myServo2
print ""

try:
    # Sweeps the servo motor forever
    while True:
        # From 0 to 180 degrees
        for angle in range(0,180):
            myServo2.write(angle)
            time.sleep(0.005)

        # From 180 to 0 degrees
        for angle in range(180,-1,-1):
            myServo2.write(angle)
            time.sleep(0.005)

except KeyboardInterrupt:
        print "Sweep ended."