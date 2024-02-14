class Test:

    #To access this method we need to make the object of the class
    def sub(self,a,b):
        self.a=a
        self.b=b
        return self.a-self.b

   #To access this we can do by directly using the class name. 
    @staticmethod
    def add(a,b):
        return a+b
    
t=Test()
print(t.sub(1,2))
print(Test.add(2,3))
