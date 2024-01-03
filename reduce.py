#Applies function to sequence and returns a single value
#required to be imported first

from functools import reduce

list1=[1,2,3,4,5,6,7,8,9]

#This line will throw an error simce it takes first two elements only. It cannot operate on more than 2 elements.
# Reduceoutput1= reduce(lambda x,y,z:x+y-z,list1)
Reduceoutput1= reduce(lambda x,y:((x+y)-1)*2,list1)
print(type(Reduceoutput1))
print(Reduceoutput1)