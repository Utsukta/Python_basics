#to open and read the file
f=open("test.txt",'r')
# print(f)
fread= f.read()
print(fread)

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
print()


#writeline takes objects such as list,tuples etc
f=open("test.txt", 'w')
lines=["line1","line2","line3"]
f.writelines(lines)