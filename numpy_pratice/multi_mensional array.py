import numpy as np

array = np.array([
    [["A","B","C"],["A","B","C"],["D","E","F"]],
    [["I","J","K"],["L","M","N"],["O","P","Q"]],
    [["R","S","T"],["U","V","W"],["X","Y","Z"]]
    ])

word = array[0,0,0] + array[1,1,0] + array[1,0,0]
box = array[0,0,1] + array[1,2,0] + array[2,2,0]
print(word) #ali
print(box) #ali
