class School:
      school_name = "Spring High School"
      def __init__(self,name, grade):
            self.name= name
            self.grade= grade
s1=School("Aakriti", "12th")
s2=School("Ananya", "11th")
print(s1.school_name)
print(s2.school_name)
School.school_name="Southwestern School"
print(s1.school_name)
print(s2.school_name)
s1.school_name="Spring High School"
print(s1.school_name)
print(s2.school_name)

          