class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age= age
        self.grade= grade

    def get_grade(self):
        return self.grade
class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_max_students = max_students
        self.students = []
    def add_students(self,student):
        if len(self.students) < self.max_max_students:
            self.students.append(student)
            return True
        return False
    def get_average(self):
        pass
std1 = student("John",25,98)
std2 = student("Milugo",22,100)
std3 = student("Joan",18,97)
std4 = student("kilian",26,78)
course = Course("Math Comp",3)
course.add_students(std1)
course.add_students(std2)
course.add_students(std3)
print(course.students[0].grade)




