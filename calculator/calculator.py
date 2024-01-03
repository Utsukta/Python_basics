from tkinter import *

expression=""


def button_clicked(num):
       global expression
       expression= expression + str(num)
       equation.set(expression)

    
def equalbtn_clicked():
        global expression
        try:
            result=eval(expression)
            equation.set(result)
            expression=""
            
        except ZeroDivisionError as e:
             equation.set("Math error")
             expression=""
        except SyntaxError as e:
             equation.set("Math syntax error")
             expression=""
             
        
def restbtn_clicked():
     global expression
     expression=""
     #this line is used to reflect the changes on the entry.
     #Without this line we cannot see any kind of changes in entry.
     equation.set(expression) 

def removebtn_clicked():
    #global keyword indicates that the function will modify the global variable
    #rather than creating the new local variable with the same name.
     global expression
     if((len(expression))>=1):
      #  This line removes the last character from the expression string using slicing. 
      #  The [:-1] notation means all characters from the beginning up to (but not including) 
      #  the last one. This effectively removes the last character.
      #negative means it counts from end of the sequence
               expression = expression[:-1]
               equation.set(expression)
               

class calculator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x700+0+0")
        self.root.minsize(500,700)
        self.root.maxsize(500,700)
        self.root.title("Calculator")
        self.root.config(bg="white")


        #We can place method within the class too and by passig self we can use this 
        #menthod inside the instances of class
    # def button_clicked(self,num):
    #    global expression
    #    expression= expression + str(num)
    #    equation.set(expression)
    
    def calculate(self):
        calculate_label=Label(text="Calculator", bg="white", foreground="black" ,font=("Times new roman",20))
        calculate_label.place(x=220, y=20)
    
        frame1=Frame(border=2, height=360,width=260, borderwidth=2, )
        frame1.place(x=100,y=140)

        entry_field= Entry( textvariable=equation, background="white", foreground="black", width=25)
        entry_field.place(x=110,y=155)

        reset_button=Button(height=2, width=2, text="AC",command=lambda:restbtn_clicked() )
        reset_button.place(x=110,y=210)

        remove_button=Button(height=2, width=2, text="xx", command=lambda:removebtn_clicked())
        remove_button.place(x=170,y=210)

        mod_button=Button(height=2, width=2, text="%", command=lambda:button_clicked("%"))
        mod_button.place(x=230,y=210)

        div_button=Button(height=2, width=2, text="/", command=lambda:button_clicked("/"))
        div_button.place(x=290,y=210)

        add_button=Button(height=2, width=2, text="+", command=lambda:button_clicked("+"))
        add_button.place(x=290,y=390)

        sub_button=Button(height=2, width=2, text="-", command=lambda:button_clicked("-"))
        sub_button.place(x=290,y=330)

        mul_button=Button(height=2, width=2, text="x", command=lambda:button_clicked("*"))
        mul_button.place(x=290,y=270)

        equal_button=Button(height=2, width=2, text="=", command=lambda:equalbtn_clicked())
        equal_button.place(x=290,y=450)

        button1=Button(height=2, width=2, text="1", command=lambda:button_clicked(1))
        button1.place(x=110,y=390)

        button2=Button(height=2, width=2, text="2",command=lambda:button_clicked(2))
        button2.place(x=170,y=390)

        button3=Button(height=2, width=2, text="3",command=lambda:button_clicked(3))
        button3.place(x=230,y=390)

        button4=Button(height=2, width=2, text="4",command=lambda:button_clicked(4))
        button4.place(x=110,y=330)

        button5=Button(height=2, width=2, text="5",command=lambda:button_clicked(5))
        button5.place(x=170,y=330)

        button6=Button(height=2, width=2, text="6",command=lambda:button_clicked(6))
        button6.place(x=230,y=330)

        button7=Button(height=2, width=2, text="7",command=lambda:button_clicked(7))
        button7.place(x=110,y=270)

        button8=Button(height=2, width=2, text="8",command=lambda:button_clicked(8))
        button8.place(x=170,y=270)

        button9=Button(height=2, width=2, text="9",command=lambda:button_clicked(9))
        button9.place(x=230,y=270)

        ebutton=Button(height=2, width=2, text="e",command=lambda:button_clicked(0.99))
        ebutton.place(x=110,y=450)

        button0=Button(height=2, width=2, text="0",command=lambda:button_clicked(0))
        button0.place(x=170,y=450)

        dotbutton=Button(height=2, width=2, text=".",command=lambda:button_clicked("."))
        dotbutton.place(x=230,y=450)

if __name__ == "__main__":
    root= Tk()
    calc=calculator(root)
    #Helps to manage the values of widgets like label/entry
    #We always use this after specifying the geometry
    equation=StringVar()
    calc.calculate()
    root.mainloop()
    
