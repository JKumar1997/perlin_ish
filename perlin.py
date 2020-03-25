import numpy as np

cells = [[0, 0, 4, 0, 3],
         [0, 2, 0, 8, 0],
         [0, 2, 0, 0, 0],
         [0, 7, 0, 4, 0],
         [0, 0, 0, 0, 3]]

print(np.asmatrix(cells))

noise = []
#   The length of [cells], which is 5, so run this 5 times.
for i in range(len(cells)):
    #   Create an empty list
    c = []
    #   Length of each list within cells
    for j in range(len(cells[i])):
        #   Access the numbers within the lists
        x = cells[i][j]
        #   Now through the length of the new list, c.
        for k in range(len(c)):
            #   If c[k] is less than x (current number), we make c[k] equal to x - 1
            if c[k] < x:
                c[k] = x - 1
        # Append the cells
        c.append(cells[i][j])
    #   Append c to noise so we can take it out of the loop.
    noise.append(c)
print(np.asmatrix(noise))

