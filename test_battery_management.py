import time
import board
import busio
#import numpy as np
import json
import random
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
#import matplotlib.pyplot as plt

i2c = busio.I2C(board.SCL,board.SDA)
ads = ADS.ADS1115(i2c)
#ads.mode = Mode.CONTINUOUS
# this is directly affecting the reading values, replacing the opamp
ads.gain = 16
chan = AnalogIn(ads,ADS.P0)

class BatteryManagement:

    def __init__(self):
        self.prev_time = time.time()
        self.cur_time = time.time()
        self.BSoC = 210*3600
        self.prev_val = 0
        self.cur_val = 0
        
        self.accessData()
        self.idx = 0
        self.data_len = len(self.data)
        self.done = False
        self.amp_hour = 210 * 3600
    
    def get_BSoC(self):
        if self.done:
            return None
       
        # Update Time stamps
        self.prev_time = self.cur_time
        self.cur_time = time.time()
        dt = self.cur_time - self.prev_time
        
        # Update Current Measurements
        self.cur_val = self.get_measurement() * 40
        print(f'measurement * 40 = {self.cur_val}')
        dCharge = (self.prev_val+self.cur_val)/2 * dt
        self.BSoC -= dCharge
        self.prev_val = self.cur_val

        return (self.BSoC/self.amp_hour)*100
    
    def accessData(self):
        with open('RandomData.txt') as json_file:
            self.data = json.load(json_file)
    
    def get_measurement_original(self):
        data = self.data
        val = data[self.idx]
        self.idx += 1
        if self.idx == self.data_len:
            self.done = True
        return val

    def get_measurement(self):
        val = chan.voltage
        return val * 16
        


if __name__ == '__main__':
    BSoC = 0
    BMS = BatteryManagement()

    prevBSoC = 0
    
    while BSoC != None:
        BSoC = BMS.get_BSoC()
        time.sleep(0.1)
        
        print(f'Current Percent:{BSoC}, change = {prevBSoC - BSoC}')
        prevBSoC = BSoC
    
    
