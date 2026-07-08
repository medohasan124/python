
class person:
    def __init__(self , name , phone):
        self.name = name
        self.phone = phone

    def father_contact_info(self):
        print(f"my name is {self.name} - my phone is {self.phone}")
    
class owner(person):
    def __init__(self, name, phone , property_count):
        super().__init__(name, phone)
        self.property_count = property_count

    def contact_info(self):
        super().contact_info() # to use the same method from father
        print(f"Owns {self.property_count} properties")

my_owner = owner("Ahmed Hassan", "0501234567", 3)
my_owner.contact_info()

