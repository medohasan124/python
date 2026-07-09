

class Studint:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Studint.count += 1

    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"
    
    @classmethod
    def status(cls):
        if cls.count == 0:
            return "no studint yet ."
        elif cls.count <= 5:
            return "so small"
        else:
            return "big class"
    
    
Studint1 = Studint("mohamed" , 44)
Studint2 = Studint("ahmed" , 20)
Studint3 = Studint("mahoud" , 30)
Studint4 = Studint("saeed" , 55)
Studint5 = Studint("ali" , 93)
Studint5 = Studint("alia" , 87)



print(Studint.count)

print(Studint.status())