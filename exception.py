#exception handling
a= input("Enter the number:")

try:
  a= int(a)
  print(f"Square of a is:{a*a}")

except Exception as e:
   print(e)
   
# we can use try and finally only as well. 
   #if asked if we can use try without except then we say yes with the help of finally
finally:
   print("error")




#Why do we need finally?
def func():
    a= input("Enter the number:")

    try:
       a= int(a)
       print(f"Square of a is:{a*a}")
       return 0

    except Exception as e:
       print(e)
       return 1
   
    
    finally:
         print("error")
    
print(func())
  