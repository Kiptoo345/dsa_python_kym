class person:
    def __init__(self, name, age, stdNo):
        self.name = name
        #self.age = age 
        self.age = self.validate_age(age)
        self.stdNo = stdNo
    
    def validate_age(self, age):
        if age > 0 and age < 100:
            self.age = age
        else:
            self.age = 0
        return self.age 
    
    def getAge(self):
        return self.age
    
p1 = person("Kym", 19, 10924)
print(p1.getAge())
    
    
            
        