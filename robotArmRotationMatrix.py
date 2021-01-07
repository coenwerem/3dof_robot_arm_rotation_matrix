import numpy as np

T1 = 0 ##Angle of rotation of the first joint
T2 = 0 ##Angle of rotation of the second joint

T1 = (T1/180)*np.pi ##Converting first joint angle from degrees to radians
T2 = (T2/180)*np.pi ##Converting second joint angle from degrees to radians

I = [[1, 0, 0],[0, 1, 0],[0, 0, 1]] ##Writing the identity matrix

I = np.matrix(I) ##Converting the array type matrix to an actual matrix object using numpy

## Defining the rotation matrices
## Between the base and first joint
R0_1 = [[np.cos(T1), -np.sin(T1), 0],[np.sin(T1), np.cos(T1), 0],[0, 0, 1]]

## Between the first and second joint
R1_2 = [[np.cos(T2), -np.sin(T2), 0], [np.sin(T2), np.cos(T2), 0], [0, 0, 1]]

## Obtaining the final expression  by taking the dot product of R0_1 and R1_2, which are themselves first 
# multiplied to the identity matrix
R0_1 = np.dot(R0_1, I)
R1_2 = np.dot(R1_2, I)

R0_2 = np.dot(R0_1, R1_2)

print(R0_2)
