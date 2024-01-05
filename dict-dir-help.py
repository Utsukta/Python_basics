class Test:
    def Intro(self,name):
        self.name=name
        print(f"Name is {name} ")
    
    def details(self):
        print("details are given")


t=Test()
t.Intro("Utsukta")

#dir
print(dir(Test))
t.details()

#dict
print(t.__dict__)

#help
print(help(Test))