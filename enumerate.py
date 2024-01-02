A=[1,2,3,4]
B=("Apple","Ball","Cat")
for index, a in enumerate(A):
    print(index,a)


#enumerate is a built-in function, that allows you to loop over sequence
#and get the index and value of each element in the sequence at the same time. 
for i,b in enumerate(B, start=1):
    print(i,b)