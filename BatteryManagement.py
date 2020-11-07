# Battery Management
# Keeps track of previous battery charge, previous measurement, previous timestamp
# Uses previous measurement and new measurement (also their respective timestamps) to calculate battery charge (using coulomb counting)
# (*advanced*) Might need to use concurrency for faster data reading and filtering?
# Grabs more data, excludes extreme values, averaging, etc.
# Probably more accurate, might be unnecessary.

import time


class BatteryManagement:

	def __init__(self):
    
    self.prev_time = 0
    self.cur_time = 0
    self.BSoC = 100
    self.prev_val = 0
    self.cur_val = 0
  
  def update(self):
    self.prev_time = self.cur_time
    self.cur_time = time.time()
    self.dt = self.cur_time - self.prev_time
    self.dCharge = (self.prev_val+self.cur_val)/2 * self.dt
    self.BSoC -= self.dCharge

  
	def get_BSoC(self):
    update(self)
    
    
