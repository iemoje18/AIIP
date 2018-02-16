#This is the file submission for pRACTICE CHALLENGE 1


#list dataset
list_I_x=[10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]
list_I_y=[8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]
list_II_x=[10,8,13,9,11,14,6,4,12,7,5]
list_II_y=[9.14,8.14,8.74,8.77,9.26,8.1,6.13,3.1,9.13,7.26,4.74]
list_III_x=[10,8,13,9,11,14,6,4,12,7,5]
list_III_y=[7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]
list_IV_x=[8,8,8,8,8,8,8,19,8,8,8]
list_IV_y=[6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.5,5.56,7.91,6.89]

#imports
from collections import Counter
from statistics import mode
import matplotlib.pyplot as plt

def descrip_stat(list_name):
    #calculate mean
    total=0
    mean_value=0
    length=len(list_name)
    for i in list_name:
        total+=i
    mean_value=total/length
    print ("Mean:")
    print (mean_value)
    #return mean_value
    
    #calculate mode
    mode_value=Counter(list_name).most_common(1)
    print ("Mode: ")
    print (mode_value)
    #return mode_value
    
    #calculate median
    sorted_list=sorted(list_name)
    length_list=len(list_name)
    median_value=length_list//2
    if length_list%2==0:
        median_even=(sorted_list[median_value-1]+sorted_list[median_value])/2
        #return median_even
        print ("Median: ")
        print (median_even)
    else:
        print ("Median: ")
        print (median_value)
        #return sorted_list(median_value)

descrip_stat(list_I_x)
descrip_stat(list_I_y)
descrip_stat(list_II_x)
descrip_stat(list_II_y)
descrip_stat(list_III_x)
descrip_stat(list_III_y)
descrip_stat(list_IV_x)
descrip_stat(list_IV_y)

#TASK 2
#Create different scatter plots

plt.scatter(list_I_x,list_I_y)
plt.show()
plt.scatter(list_II_x,list_II_y)
plt.show()
plt.scatter(list_III_x,list_III_y)
plt.show()
plt.scatter(list_IV_x,list_IV_y)
plt.show()


"""
The summary statistics are not conclusive and cant be used to solely for data analysis

"""






