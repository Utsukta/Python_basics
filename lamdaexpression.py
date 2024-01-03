
#anonymous function without a name
#used in situations where a small function is required for a short period of time
x=lambda y:y*y
print(x(2))

triple= lambda a,b,c: a*b*c
print(triple(2,3,4))
# print(triple())


#function passed as a parameter
def func(fx,value1,value2,value3):
    return 2*fx(value1,value2,value3)

print(func(triple,2,3,4))


#checking if instance is the tuple or not
num1=num2=(1,2,3,4)
print(isinstance(num1,tuple))