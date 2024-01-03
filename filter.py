#Similar to Map, takes a function and apply it to the sequence and generate new sequence
#Just it filters the sequence with some desired condition

list1=[1,3,4,5,5]

filterfunc1=list(filter(lambda x:x<4, list1))
print(filterfunc1)


def func(a):
    return a%2==0

filterfunc2=list(filter(func,list1))
print(filterfunc2)


list2=["Hello","there","Ustukta","Khatri"]
filterfunc3=list(filter(lambda x:len(x)>5, list2))
print(filterfunc3)