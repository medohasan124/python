studint= [
    ("mohamed","A",50),
    ("ahmed","B",20),
    ("ali","C",10),
    ("saeed","B",100),
]

#def x(number):
#    return number[2]

soted_studint = sorted(studint , key= lambda number : number[2])

for i in soted_studint:
    print(i)