import sys
import numpy as np

key = "WHY DID THE ROTATION CIPHER GO TO THERAPY? BECAUSE IT COULD NOT STOP SPINNING ITS SECRETS AROUND IN CIRCLES!"


def spiral(key):
    string = ""

    matrix_width = len(key[0])
    matrix_height = len(key)
    allowed_depth = 0

    if matrix_width < matrix_height:
        allowed_depth = matrix_width // 2
    else:
        allowed_depth = matrix_height // 2


    # Here "i" denotes the depth we're into the matrix
    # Here we read the normal matrix in a spiral form starting from top right corner
    for i in range(allowed_depth):

        # Going down on right side
        for j in range(i, matrix_height-i-1):
            string += key[j][matrix_width-i-1]

        # Going left on the bottom side
        for j in range(matrix_width-i-1, i, -1):
            string += key[matrix_height-i-1][j]

        # Going up on the left side
        for j in range(matrix_height-i-1, i, -1):
            string += key[j][i]
            
        # Going right on the top side
        for j in range(i, matrix_width-i-1):
            string += key[i][j]


    return string

if __name__ == '__main__':
    args = sys.argv

    if len(args) != 4:
        print("Usage: python route_cipher_encrypt.py <KEY> <rows> <columns>")
        exit(1)
    
    key = key
    key = key.replace(" ", "")
    rows = int(args[2])
    columns = int(args[3])

    if (rows * columns != len(key)):
        print("Error: Size of key is not equal to product of length and height")

    key = key.replace(" ", "")

    arr = np.array([*key])
    print(arr)
    arr = np.reshape(arr, (columns, rows)).T
    print(arr)
	
    print(spiral(arr))