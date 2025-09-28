class Person:
    def __init__(self, firstname,lastname, health,status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion=random.randrange(1,3)
        if emotion==1:
            print("{} is happy".format(self.firstname))
        elif emotion==2:
            print("{} is sad".format(self.firstname))

    def status_change(self):
        if self.health ==100:
            print("{} is totaly healthy".format(self.firstname))
        elif self.health >=76:
            print("{} is a little tired today".format(self.firstname))
        elif self.health >=51:
            print("{} is FEELS UNWELL".format(self.firstname))
        elif self.health >=40:
            print("{} goes to doctor".format(self.firstname))
        else:
            print("{} is unconscious".format(self.firstname))

Maria=Person("Maria", "Guti", 95, status=True)
Ray=Person("Ray", "Jones", 88, status=False)
Lee=Person("Lee", "Smith", 90, status=True)

print("{} is my friend {}".format(Maria.firstname, Maria.status))
print("{} is my friend {}".format(Ray.firstname, Ray.status))

Maria.introduce()
Ray.introduce()
Lee.introduce()

Maria.status_change()
Ray.status_change()
Lee.status_change()
