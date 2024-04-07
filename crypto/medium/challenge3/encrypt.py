import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

__key__ = hashlib.sha256(b'16-character key').digest()

def encrypt(raw):
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    raw = base64.b64encode(pad(raw).encode('utf-8'))
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key = __key__, mode= AES.MODE_CFB,iv= iv)

    ct = (cipher.encrypt(raw))
    open('aes_ciphertext.hex', 'w').write(cipher.encrypt(raw).hex())
    open('aes_iv.hex', 'w').write(iv.hex())
    open('aes_key.hex', 'w').write(__key__.hex())

    # return base64.b64encode(iv + cipher.encrypt(raw))
    unpad = lambda s: s[:-ord(s[-1:])]

    cipher = AES.new(__key__, AES.MODE_CFB, iv)
    return unpad(base64.b64decode(cipher.decrypt(ct)).decode('utf8'))


if __name__ == '__main__':
    plaintext = "Why did AES encryption go to the gym? To flex its byte muscles and lift the security bar!"
    print(encrypt(plaintext))