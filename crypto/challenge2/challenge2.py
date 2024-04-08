import numpy as np

"""
Route Cipher:

For more information about route ciphers: https://en.wikipedia.org/wiki/Transposition_cipher#Route_cipher
Assume that the route always begins in the top right of the matrix representation.
"""

encrypted_key = ""
step_size = None

with open('challenge2.txt', 'r') as f:
    encrypted_key, step_size = f.read().split('\n')

print(encrypted_key)
print(step_size)


