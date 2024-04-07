import base64
from Crypto.Cipher import AES

# Read hex strings from file
key = ...
iv = ...
ciphertext = ...

# Unpad function used to remove padding from the decrypted text
unpad = lambda s: s[:-ord(s[-1:])]

# Create the cipher object using the AES object from the Crypto package
# and find the plaintext
cipher_obj = ...
