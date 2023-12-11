class grades:
    def __init__(self,m):
        self.mark = m
    def grading(self):
        marks = self.mark
        if marks >= 80:
            print("A")
        elif marks >= 70:
            print("B")
        elif marks >=60:
            print("C")
        elif marks >= 50:
            print("D")
        elif marks >= 40:
            print("E")
        elif marks < 40:
            print("Fail")

graded = grades(int(input("enter grades- ")))

graded.grading()


