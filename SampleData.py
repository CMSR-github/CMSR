# CMSR Sample Data Generation

# Grayson Was here!

# Import libraries
import json
import random

# Randomize a long array of 'data' between 0 and 1023
# Somewhat 'continuous'
# Generating Random numbers
# How are we going to make that somewhat continuous?

#We could try to make a very long loop with just random or we could try out numpy
test = [random.Random() for i in range(0,10)]

#from searching online
#from numpy import random
#creates a 2D array from 0 to 100 with 3 rows and 5 random ints in each
#x = random.randint(100, size=(3, 5))
#how do you think we should 
#https://www.w3schools.com/python/numpy_random.aspkeep it cont inuous?


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