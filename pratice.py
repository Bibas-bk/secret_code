"""class fire:
    name="bibas"
    faculty="engineering"
    department="IT"
    def __init__(self):
        print("this is default")     
        pass


    def __init__(self,name,faculty,department):
        self.name=name
        self.faculty=faculty
        self.department=department
    

    def display(self):
        print(f"{self.name}is a student of{self.faculty}of{self.department}")

obj=fire("Bibas","engineering","IT")
obj.display()

def greet(mfx):
    def fx(*args,**kwargs):
        print("good morning")
        mfx(*args,**kwargs)
        print("thanks for using this function")
    return fx
@greet
def hello():
    print("go to programming")

hello()
class Myclass:
    def __init__(self,value):
        self.value=value 
    def show(self):
        print(f"value is:{self.value}")
    @property
    def ten_value(self):
        return self.value*10
    
    @ten_value.setter
    def ten_value(self,new_value):
        self.value=new_value/10
        return self.value
obj=Myclass(5)               
obj.show()
print(obj.ten_value)
print(obj.ten_value)"""
class random:
    

