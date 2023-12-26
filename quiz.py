amount=0

quetsions=["Capital city of Nepal", "How many provience are there in Nepal","Prime Minister of Nepal"]
answers=["Kathmandu",7,"Prachanda"]

for i in quetsions:
   print("Select the number from 1 to 3:")
   selected_question= int(input())
   if(selected_question==1):
    print(quetsions[0])
    selected_answer=int(input("Please select the correct answer:\n1.Kathmandu\n2.Lalitpur\n3:bhaktapur\n"))
    if(selected_answer==1):
        amount=amount+100
        print("Congratualtions you won"+str(amount))
    else:
       print("Wrong answer")
       continue
    
   if(selected_question==2):
      print(quetsions[1])
      selected_answer=int(input("Please select the correct answer:\n1\n2\n7\n"))
      if(selected_answer==7):
        amount=amount+100
        print("Congratualtions you won"+str(amount))
      else:
         print("Wrong answer")
         continue
         
   if(selected_question==3):
       print(quetsions[2])
       selected_answer=int(input("Please select the correct answer:\n1.KP\n2.Prachanda\n3:bhadur\n"))
       if(selected_answer==2):
        amount=amount+100
        print("Congratualtions you won"+str(amount))
       else:
          print("Wrong answer")
          continue

    



