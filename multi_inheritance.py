

class human:
    alive = True

class father(human):
    father_name = "hassan"

class mother(human):
    mother_name = "alia"

class son(father,mother):
    name = "Ali"

person = son()

print(person.father_name)
print(person.mother_name)
print(person.name)