class Student:
    def __init__(self,name, mark1, mark2, mark3, mark4, mark5):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.mark4=mark4
        self.mark5=mark5

    def average(self):
        avg=(self.mark1+self.mark2+self.mark3+self.mark4+self.mark5)/5
        print("Name", self.name)
        print("Average Marks:", avg)
s1= Student("Aakriti", 80,90,70,60,50)
s1.average()


