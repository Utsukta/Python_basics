#Special type of function that allow you to create an iterable sequnce of values.
#It returns the generator object, which can be used to generate the value one by one
#Used to work on complex and large data sets.
#They allow us to generate values on-the-fly rather than having to create and store the entire sequence
#Create a generator by using yeild
#Benefits are- since they generate values on the fly, less memory is require

def generator():
    for i in range(0,500):
        yield i


gen=generator()
print(next(gen))

#Also can be done ad
for j in gen:
    print(j)