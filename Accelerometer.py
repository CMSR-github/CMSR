import datetime
import IMU
import math
import sys


IMU.detectIMU()
if(IMU.BerryIMUversion == 99):
    print(" No BerryIMU found... exiting ")
    sys.exit()
IMU.initIMU()       #Initialise the accelerometer, gyroscope and compass

class Accelerometer:

    def __init__(self):
        self.prev_time = datetime.datetime.now()
        self.cur_time = datetime.datetime.now()
        self.accXnorm = 0
        self.accYnorm = 0
        

    def get_measurement(self):
        ACCx = IMU.readACCx()
        ACCy = IMU.readACCy()
        ACCz = IMU.readACCz()
        GYRx = IMU.readGYRx()
        GYRy = IMU.readGYRy()
        GYRz = IMU.readGYRz()
        MAGx = IMU.readMAGx()
        MAGy = IMU.readMAGy()
        MAGz = IMU.readMAGz()
        #in the future we may want to add compas callibration here 

        #time between GyroReads here?
        self.accXnorm = ACCx/math.sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)
        self.accYnorm = ACCy/math.sqrt(ACCx * ACCx + ACCy * ACCy + ACCz * ACCz)

    def display_data(self):
        print(f"accX: {self.accXnorm} accY: {self.accYnorm}")


