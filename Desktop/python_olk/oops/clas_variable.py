class Students :
    school ="dav 15 chd"
    def __init__(self,name:str)->None:
        self.name= name


s1=Students("maahir")
s2=Students("raj")

print(s1.name)
print(s2.name)       #### isntance  var
print(s1.school)        #### class var
print(s2.school)
print(Students.school)


# Students.school ="xyz"   ###### method to change class var

s1.school="xyz"
print(s1.school)
print(s2.school)
print(Students.school)
