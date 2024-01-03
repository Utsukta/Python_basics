#== compares the value
#is compares the object identity in the memory(returns true if constant or immutable)
#strings and int are immutable
a=5
b=5

print(a==b)
print(a is b)

a="harry"
b=5

print(a==b)
print(a is b)

a={1,2,3,4,5}
b={1,2,3,4,5}

print(a==b)
print(a is b)

#tuples are immutable so they will be kept on the same location on the memory
a=(1,2,3,4,5)
b=(1,2,3,4,5)

print(a==b)
print(a is b)