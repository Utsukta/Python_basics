class Hello:
    name="Hari"
    def Test1(self):
        return self.name
    
    @classmethod
    def Test2(cls,newname):
        cls.name=newname

h=Hello()
print(f"Class variable name is {h.name}")
print(f"Test1 name is {h.Test1()}")

h.Test2("Roshan")
print(Hello.name)


class Example:
    def __init__(self,name,age):
        self.n=name
        self.a=age
        

    @classmethod
    def ClassMethod(cls,value):
        return cls(value.split("-")[0], value.split("-")[1])


print("Class Method as Alternative constructor")
e1=Example("Utsukta",23)
print(e1.n , e1.a)

value="Hari-22"
e2=Example.ClassMethod(value)
print(e2.a, e2.n)
