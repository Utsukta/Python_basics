# def PrimeNum():
flag=False
num= eval(input("Enter the number"))
for i in range(2,num):
         if (num % i)==0:
            print(i)
            flag=True
            # print(f"{num} is not a prime number")
        #     break
        #  else:
        #     print(f"{num} is a prime number")
            break
         else:
               print("prime")
           
         
if flag:
      print("not a prime")
else:
      print("Prime Number")      
# PrimeNum()


# Program to check if a number is prime or not


# num= eval(input("Enter the number"))
# # To take input from the user
# #num = int(input("Enter a number: "))

# # define a flag variable
# flag = False

# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

#     # check if flag is True
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")