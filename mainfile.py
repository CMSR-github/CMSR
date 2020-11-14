from BatteryManagement import BatteryManagement
import time
import decimal


if __name__ == '__main__':
    BSoC = 0
    BMS = BatteryManagement()
    BSoC = BMS.get_BSoC()
    time.sleep(0.1)
    while BSoC != None:
        rounded = float(round(BSoC,2))
        print(f'Current Percent: {rounded}%')
        BSoC = BMS.get_BSoC()
        time.sleep(0.1)