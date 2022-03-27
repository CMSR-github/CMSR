import time
#import numpy as np
import json
import random
#import matplotlib.pyplot as plt

class BatteryManagement:

    def __init__(self):
        self.prev_time = time.time()
        self.cur_time = time.time()
        self.BSoC = 5*3600
        self.prev_val = 0
        self.cur_val = 0
        
        self.accessData()
        self.idx = 0
        self.data_len = len(self.data)
        self.done = False
    
    def get_BSoC(self):
        if self.done:
            return None
       
        # Update Time stamps
        self.prev_time = self.cur_time
        self.cur_time = time.time()
        dt = self.cur_time - self.prev_time
        
        # Update Current Measurements
        self.cur_val = self.get_measurement()
        dCharge = (self.prev_val+self.cur_val)/2 * dt
        self.BSoC -= dCharge

        return (self.BSoC/(5*3600))*100
    
    def accessData(self):
        with open('/home/pi/CMSR/RandomData.txt') as json_file:
            self.data = json.load(json_file)
    
    def get_measurement(self):
        data = self.data
        val = data[self.idx]
        self.idx += 1
        if self.idx == self.data_len:
            self.done = True
        return val
        


if __name__ == '__main__':
    BSoC = 0
    BMS = BatteryManagement()
    while BSoC != None:
        BSoC = BMS.get_BSoC()
        time.sleep(0.1)
        
        print(f'Current Percent:{BSoC}')
    
    
