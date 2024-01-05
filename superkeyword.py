class Baseclass:
    def introduction(self, name):
        self.name=name
        print(f"Name is {self.name}")


#inheritance
class Childclass(Baseclass):
    def department(self, depart):
        self.depart= depart
        super().introduction("Hari")
        print(f"She work on the {depart} department")

bc=Baseclass()
bc.introduction("Utsukta")
cc=Childclass()
cc.department("Computer")

    