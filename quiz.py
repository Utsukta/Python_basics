# amount=0

# questions=["Capital city of Nepal", "How many provience are there in Nepal","Prime Minister of Nepal"]
# answers=["Kathmandu",7,"Prachanda"]

# selected1= False
# selected2= False
# selected3= False

# for i in questions:
#    print("Select the number from 1 to 3:")
#    selected_question= int(input())
#    if(selected_question==1 and selected1==False):
#     selected1=True
#     print(questions[0])
#     selected_answer=int(input("Please select the correct answer:\n1.Kathmandu\n2.Lalitpur\n3:bhaktapur\n"))
#     if(selected_answer==1):
#         amount=amount+100
#         print("Congratualtions you won"+str(amount))
#     else:
#        print("Wrong answer")
   
    
#    if(selected_question==2 and selected2==False):
#       print(questions[1])
#       selected2=True
#       selected_answer=int(input("Please select the correct answer:\n1\n2\n7\n"))
#       if(selected_answer==7):
#         amount=amount+100
#         print("Congratualtions you won"+str(amount))
#       else:
#          print("Wrong answer")
      
#    if(selected_question==3 and selected3==False):
#        print(questions[2])
#        selected3=True
#        selected_answer=int(input("Please select the correct answer:\n1.KP\n2.Prachanda\n3:bhadur\n"))
#        if(selected_answer==2):
#         amount=amount+100
#         print("Congratualtions you won"+str(amount))
#        else:
#           print("Wrong answer")
         

amount = 0

questions = ["Capital city of Nepal", "How many provinces are there in Nepal", "Prime Minister of Nepal"]
options = [
    ["Kathmandu", "Lalitpur", "Bhaktapur"],
    ["5", "7", "10"],
    ["KP Sharma Oli", "Prachanda", "Sher Bahadur Deuba"]
]

answers = [1, 2, 2]

# selected_questions = set()

for i in range(3):
    while True:
        print(questions[i])
        #     print(option)
        for j, option in enumerate(options[i], start=1):
            print(f"{j}. {option}")


        selected_answer = int(input())
        
        if 1 <= selected_answer <= len(options[i]):
            break
        else:
            print("Invalid selection. Please choose another question.")

    # selected_questions.add(i )

    if selected_answer == answers[i]:
        amount += 100
        print(f"Congratulations, you won {amount}")
    else:
        print("Wrong answer")

    # Display the current amount after each question
    print("Your current amount: " + str(amount))





