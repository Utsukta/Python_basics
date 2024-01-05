#We use getters & setters to add validation logic around getting and setting a value.
#To avoid direct access of a class field i.e. private variables cannot be accessed directly or 
#modified by external user.

class Hello:
    def __init__(self,name):
        self._name=name
    
    @property
    def value(self):
        return self._name
    
    @value.setter
    def value(self, new_name):
        self._name=new_name
    
obj1= Hello("utsukta")
obj1.value="khatri"
print(f"object value is {obj1.value}")
print(f"object 2 value is {obj1.value}")