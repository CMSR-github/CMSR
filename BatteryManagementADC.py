import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
#import numpy as np
import json
import random
#import matplotlib.pyplot as plt

#create the SPI Bus
spi = busio.SPI(clock = board.SCK, MISO = board.MISO, MOSI = board.MOSI)

#create the chip select
cs = digitalio.DigitalInOut(board.D22)

#create mcp object
mcp = MCP.MCP3008(spi,cs)
#create analog input on pin 0
chan0 = AnalogIn(mcp,MCP.P0)


#driver for the battery state of charge sensor, uses MCP ADC to read current values 
# across shunt resistor in order to calculate BSoC via Coulomb Counting. Used in livegraph to display values
class BatteryManagement:

    # TODO:initial battery state of charge, check new batteries? post testing,
    # we would want to remove self.accessData(), could be taking too much time
    def __init__(self):
        self.prev_time = time.time()
        self.cur_time = time.time()
        
        #initial BSoC, attribute should be changing
        self.BSoC = 5*3600  
        #total BSoC, should not change
        self.BSoC_total = 5*3600

        self.prev_val = 0
        self.cur_val = 0
        
        self.accessData() 
        self.idx = 0
        self.data_len = len(self.data)
        self.done = False

        #TODO: Test this? Worried about scope issues
        self.spi = busio.SPI(clock = board.SCK, MISO = board.MISO, MOSI = board.MOSI)
        #create chip select
        self.cs = digitalio.DigitialInOut(board.D22)
        #create mcp object
        self.mcp = MCP.MCP3008(self.spi,self.cs)
        #create analog input on pin 0
        self.chan0 = AnalogIn(self.mcp,MCP.P0)

        
    

    #this should be the main method called to report the BSoC, relies on 
    #separate get_measurement method to read raw data and then does CC
    def get_BSoC(self):
        if self.done:
            return None
       
        # Update Time stamps
        self.prev_time = self.cur_time
        self.cur_time = time.time()
        dt = self.cur_time - self.prev_time
        
        # Gets current measurement and then uses Coulomb Counting to calculate BSoC
        self.cur_val = self.get_measurement()
        dCharge = (self.prev_val+self.cur_val)/2 * dt
        self.BSoC -= dCharge

        return (self.BSoC/(self.BSoC_total))*100  #returns BSoC as a percentage of original amount 
    
    #method to access test data and load it into the object
    def accessData(self):
        with open('RandomData.txt') as json_file:
            self.data = json.load(json_file)

    #remap the value from the old range of values (raw values) to new range (for adc)
    def remap(self,value,orig_min,orig_max,new_min,new_max):
        orig_range = orig_max - orig_min
        new_range = new_max - new_min

        #convert
        valueScaled = int(value-orig_min) / int(orig_range)
        new_val = int(new_min + (valueScaled*new_range))

        return new_val

    
    #read the raw current value via ADC
    def get_measurement(self):

        raw_val = self.chan0.value
        val = raw_val
        print(f"raw val: {raw_val}")

        # BELOW: Code for indexing into the generated test data
        # data = self.data
        # val = data[self.idx]
        # self.idx += 1
        # if self.idx == self.data_len:
        #     self.done = True
        return val
        


if __name__ == '__main__':
    BSoC = 0
    BMS = BatteryManagement()
    while BSoC != None:
        BSoC = BMS.get_BSoC()
        time.sleep(0.1)
        
        print(f'Current Percent:{BSoC}')
    
    
