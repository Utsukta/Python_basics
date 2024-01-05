class parent:
    def intro(self):
        print("name is parent")

class child(parent):
    def intro(self):
        print(f"name is child")
        super().intro()


c=child()
c.intro()


class area:
    def square(self, length):
        return length*length

class volume(area):
    def square(self,length):
        return length* super().square(2)
    
v=volume()
print(v.square(2))