# CMSR Sample Data Generation

# Grayson Was here!

# Import libraries
import json
import random
import matplotlib.pyplot as plt
import math

# Randomize a long array of 'data' between 0 and 1023
# Somewhat 'continuous'
# Generating Random numbers
# How are we going to make that somewhat continuous?

# random direction
def Direction():
  	return bool(random.getrandbits(1))
    

def GenerateData(datalist,start,amount,maxstepsize):
    cont = 5
    #cont maintains a direction for 5 data points
    positive = True
    #we start in the positive direction
    for i in range(amount):
        if cont > 0:
            delta = random.randint(0,100)/100 * maxstepsize
            if positive: 
                start += delta
            else:
                start -= delta 
            datalist.append(math.trunc(start))
            cont -= 1
        else:
            positive = Direction()
            cont += 5
  
# datalist = []
# GenerateData(datalist,300,100,20)
# plt.plot(datalist)
# plt.show()


#from searching online
#from numpy import random
#creates a 2D array from 0 to 100 with 3 rows and 5 random ints in each
#x = random.randint(100, size=(3, 5))
#how do you think we should 
#https://www.w3schools.com/python/numpy_random.aspkeep it cont inuous?


# save that array of 'data' to a file
# how to save an array of 'data' to a file that is easily accessible

# Writes data from "data" list to json file named RandomData.txt
'''
def writeDataToFile(data):
  with open('RandomData.txt', 'w') as outfile:
      json.dump(data, outfile)

# for accessing data from json file
def accessData():
  with open('RandomData.txt') as json_file:
    data = json.load(json_file)
    for p in data:
        # do something to data
'''