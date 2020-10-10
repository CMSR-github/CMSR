# CMSR Sample Data Generation

# Grayson Was here!

# Import libraries
import json
import random

# Randomize a long array of 'data' between 0 and 1023
# Somewhat 'continuous'
# Generating Random numbers
# How are we going to make that somewhat continuous?

def Direction(cont):
    direction = random.randint(0,10)
    cont += 5
    if direction > 5:
        return True
    else:
        return False
    

def GenerateData(datalist,start,amount,maxstepsize):
    cont = 0
    positive = True
    for i in range(amount):
        if cont > 0:
            delta = random.randint(0,100)/100 * maxstepsize
            if positive: 
                start += delta
            else:
                start -= delta 
            datalist.append(start)
            cont -= 1
        else:
            positive = Direction(cont)
#haven't really worked it out fully but this is what I was thinking 

#from searching online
#from numpy import random
#creates a 2D array from 0 to 100 with 3 rows and 5 random ints in each
#x = random.randint(100, size=(3, 5))
#https://www.w3schools.com/python/numpy_random.aspkeep 


# save that array of 'data' to a file
# how to save an array of 'data' to a file that is easily accessible

# Writes data from "data" list to json file named RandomData.txt
with open('RandomData.txt', 'w') as outfile:
    json.dump(data, outfile)
    
'''
# for accessing data from json file

with open('RandomData.txt') as json_file:
  data = json.load(json_file)
  for p in data:
      # do something to data
      
'''