class Student:
    # def __init__(self, name, id):
    #     self.name = name
    #     self.id = id
    # def __init__(self, name, id, grade): 
    #     self.name = name
    #     self.id = id
    #     self.CGPA=grade
    def __init__(self, *info):
        if len(info)==3:
            self.name = info[0]
            self.id = info[1]
            self.CGPA = info[2]
        elif len(info)==2:
            self.name = info[0]
            self.id = info[1]
        elif len(info)==1:
            self.name = info[0]
        print('A student object is created')
            

student1= Student("Yuhan",23)
student2= Student("Nina",22,3.97)
student3= Student("Tisha")
student4= Student()