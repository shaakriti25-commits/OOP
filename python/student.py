class Student:
    def __init__(self, name,m1, m2, m3, m4, m5):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def average(self):
        avg= (self.m1+self.m2+self.m3+self.m4+self.m5)/5
        print("Name:", self.name)
        print("Average Marks:", avg)
        return avg
    def result(self):
        avg= self.average()
        if avg>=40:
            print("Pass")
        else:
            print("Fail")
s1=Student("Aakriti", 80,90,70,60,50)
s1.result()
            