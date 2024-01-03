#Map is a built-in fucntion that allows you to apply a function on a sequence of elements
#and provides the new sequence


num=[1,2,3,4,5,6]
numsqr=list(map(lambda x :x*x,num))
print(numsqr)

tuplenum=(1,2,3,4,5,6,7)
tuplenumsqr=tuple(map(lambda x:x*x, tuplenum))
print(tuplenumsqr)

setnum={2,3,4,5,6,7,8,9,2}
setnumsqr=set(map(lambda x:x*x, setnum))
print(setnumsqr)

setnum.add(10)
print(setnum)