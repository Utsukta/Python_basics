import os

# print("main")
# exception.func()


#To make the directory
# os.mkdir("a")

#rename the directory
# os.rename("/Users/utsuktakhatri/Desktop/Python Basics/a","/Users/utsuktakhatri/Desktop/Python Basics/a1")

#check if path exists
if(not os.path.exists("a1")):
    os.mkdir("a1")
if( os.path.exists("a1")):
    print("exists")

# directory inside the directory
# os.mkdir("a1/day")
# os.mkdir("a1/day3/2")

# 10 directory inside the directory

for i in range(0,10):
 if(not os.path.exists(f"a1/Day{i}")):
    os.mkdir(f"a1/Day{i}")

# folders= os.listdir("a1")
# for folder in folders:
#     print(folder)
    
#current working directory
print(os.getcwd())

#Deleted the directory
# for i in range(0,10):
#  os.removedirs(f"/Users/utsuktakhatri/Desktop/Python Basics/a1/Day{i}")