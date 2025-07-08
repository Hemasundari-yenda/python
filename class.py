class pc:
    def __init__(self,name,place,company):
        self.name=name
        self.place=place
        self.company=company
        print("i am in init constructor in python i am called as init method")
    def main(self):
        print('my name is',self.name)
        print('i am from',self.place)
        print('i am working in',self.company)
        print('i am in  main method')
pc1=pc('hema','sklm','google')
pc1.main()
    
#this is a instance method
class student:
    school='telsuko'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        print((self.m1+self.m2+self.m3)/3)
        print('the thing is completed')
    def avg(self):
        print((self.m1+self.m2+self.m3)/3)
    
s1=student(50,35,27)
s2=student(23,45,67)
s1.avg()
s2.avg()
print(s1.m1)
print(s1.m2)
print(s1.m3)
print(s2.m1)
print(s2.m2)
print(s2.m3)

#this is a class method

class student1:
    school='telsuko'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        print((self.m1+self.m2+self.m3)/3)
        print('the thing is completed')
    def avg(self):
        print((self.m1+self.m2+self.m3)/3)
    '''  @classmethod #it is a decarator  # decarators are need for writing a program in class method
    def config(cls):#in the parathesis  we need pass cls becase it is a class method it should be same not anything else
       '''
    #for updating the school name
    @classmethod
    def config(cls,new_name):
        cls.new_name=new_name
        print(f"the changed name is:{cls.new_name}")

    
    
s1=student1(50,35,27)
s2=student1(23,45,67)
s1.avg()
s2.avg()
student1.config('ists')
#for counting the students we usebelow example
class student:
    total_students=0

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        student.total_students +=1
    def display(self):
        print(f'the name is {self.name}')
        print('the rool no is',self.rollno)
  
        
s1=student('ram',18)
s2=student('sita',19)
s1.display()
s2.display()
print('the total students',student.total_students)




