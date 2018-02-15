from collections import defaultdict
import random as rand
import pickle
import time
import string
import logging

#create dictionary dataset
objects= defaultdict(list)
#create file, time stamp
timestr=time.strftime("%Y%m%d-%H%M%S")
f = open('file1.txt', 'a+b')
#add time stamp to data
text='Data Collected on '+timestr
f.write(text)
#create entries containing 16 floats each
for i in range(16):
    for j in range(1,17):
        sensorDataNumber=rand.random()
        objects[j].append(sensorDataNumber)

#dump objects into file, close file
pickle.dump(objects,f)
f.close()

#create dummy data
sensorDataStr='err'
objects[16].append(sensorDataStr)

#Function to test for string, logging
letters=string.letters
key_list=[]
def search(sensorList, strings):
    for key in sensorList.keys():
        for value in strings:
            if value in strings:
                return key
                
        logging.warning('String found, index at '+timestr)
                
        return None

search(objects,letters)
