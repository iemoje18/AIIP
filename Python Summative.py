from collections import defaultdict
import random as rand
import pickle
import time
import string
#create dictionary dataset
objects= defaultdict(list)
timestr=time.strftime("%Y%m%d-%H%M%S")
f = open(timestr+' '+'file.txt', 'a+b')
#create list with entries containing 16 floats each
for i in range(16):
    for j in range(1,17):
        sensorDataNumber=rand.random()
        objects[j].append(sensorDataNumber)


#dump objects into file
pickle.dump(objects,f)
f.close()

#Create dummy data inside current Objects dict
sensorDataStr='err'
objects[16].append(sensorDataStr)
print objects

letters=string.letters
key_list=[]

for key in objects.keys():
    for value in letters:
        if value in letters:
            key_list.append(key)

print "String found"
print key_list

"""
def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None

print search(objects, letters)



if string.letters in objects.values:
    print "There is a string"
    else:
        print "No string"


"""

#print 

#storedlist=pickle.load(f)
#print storedlist

#Test incoming data for string entries

#Dummy data



