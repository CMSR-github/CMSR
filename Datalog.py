import time
# import Accelerometer
import BatteryManagement
import gps
import pandas as pd
from datetime import date
from threading import Timer


class Datalog():

    def __init__(self, interval: int):
        self.cur_time = time.time()
        self._timer = None
        self.interval = interval
        self.today = date.today()
        self.data = {'Time': [], 'Battery': [], 'AccX': [],
                     'AccY': [], 'GPS': []}
        self.is_running = False
        self.start()

    # Get accelerometer information
    # smbus library used in IMU only works on python 3.5
    # def get_acceleration(self):
        # get_acc = Accelerometer.Accelerometer()
        # accXnorm, accYnorm = get_acc.get_measurement()
        # return accXnorm, accYnorm

    # Get battery information
    def get_batterty(self):
        get_bat = BatteryManagement.BatteryManagement()
        battery = get_bat.get_measurement()
        return battery

    # Get gps information
    def get_gps(self):
        get_gps = gps.BerryGPS()
        res = get_gps.getData()
        lat, dirLat, lon, dirLon, speed, time, trCourse, date = res
        return res

    # What to do in each time step
    def _run(self):
        self.is_running = False
        self.start()
        self.cur_time = time.time()
        # data_x, data_y = self.get_acceleration()
        data_bat = self.get_batterty()
        data_gps = self.get_gps()
        self.data['Time'].append(self.cur_time)
        # self.data['AccX'].append(data_x)
        # self.data['AccY'].append(data_y)
        self.data['Battery'].append(data_bat)
        self.data['GPS'].append(data_gps)

    # Start data collection
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    # End data collection
    def stop(self):
        self._timer.cancel()
        self.is_running = False

    # Output saved data of the current run in csv
    def output_csv(self):
        df = pd.DataFrame(self.data)
        d4 = self.today.strftime("%b-%d-%Y")
        file_name = "CMSR_log_" + d4
        df.to_csv(file_name, encoding='utf-8', index=False)
        return True
