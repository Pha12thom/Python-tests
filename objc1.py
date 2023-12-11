class person:
    def __init__(self,G,A,M,C,S):
        self.name =G
        self.age= A
        self.gender= M
        self.Course = C
        self.status = S
    def named(self):
        print("Hi my name is",self.name)
        print("I am mathematics and a computer science student at maseno university")
    def aged(self):
        my_age = self.age
        if my_age >= 20:
            print("I am eligible to get full stack `certificate in python")
        else:
            print("I cant get that certificate with YOUNG AGE")
    def gendered(self):
        if self.gender == "Male":
            print("I am a Male")
        else:
            print("I am Female")
    def coursed(self):

        print("I do",self.Course)
    def singles(self):
        if self.status == "single":
            print("You should get married")
            print("or start searching for a wife")
        else:
            print("Youre very lucky that your'e not single")
ob1 = person("Milugo",23,"Male","Mathematics and computer Science","single")
ob1.named()
ob1.aged()
ob1.gendered()
ob1.singles()
ob1.coursed()


