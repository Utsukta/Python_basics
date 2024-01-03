#to open and read the file
f=open("test.txt",'r')
# print(f)
fread= f.read()
# print(fread)

#to open and write on the file= erase the already available content with given content.
#also creates the file if not exists.
f=open("test.txt","w")
fwrite=f.write("Namaste")
print(fwrite)

#appends the content i.e add the content without erasing already available content
f=open("test.txt","a")
f.write(" Utsukta")

#with statement
with open('test.txt','a') as f:
    f.write(" is my name")



#writeline takes objects such as list,tuples etc
f=open("test.txt", 'w')
lines=["line1\n","line2\n","line3\n"]
tupeles=(1,2,3,4,5,6,"hello")
# f.writelines(lines)
for i in tupeles:
 print(i)
 f.writelines(str(i))


#readline
f=open("test.txt","r")

#this read only one line
# print(f.readline()) 

#to read all lines we will use while loop
while True:
    line=f.readline()
    
    if(not line ):
      break
    print(line)



