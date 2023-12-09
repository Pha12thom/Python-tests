class person:
    def __init__(self):
        self.name = "sam"
        self.gender= "male"
        self.age = 22
    def talk(self):
        print("Hi i am", self.name)
    def nature(self):
        print("I am ",self.gender)
    def vote(self):
        if self.age >= 18:
            print("i am elgible to vote")
        else:
            print("Not eligible for vote")
print("#method one of calling objects")
obj = person()
person.talk(obj)
person.nature(obj)
person.vote(obj)
print("_____________________________________")
print("#method 2")

obj.talk()
obj.nature()
obj.vote()
#adding values to obj1
