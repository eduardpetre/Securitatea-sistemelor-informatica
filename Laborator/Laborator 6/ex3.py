from Crypto.Cipher import DES

key1 = '\x?0\x00\x00\x00\x00\x00\x00\x00'
key2 = '\x?0\x00\x00\x00\x00\x00\x00\x00'

cipher1 = DES.new(key1, DES.MODE_ECB)
cipher2 = DES.new(key2, DES.MODE_ECB)

plaintext = "Provocare MitM!!"
ciphertext = cipher2.encrypt(cipher1.encrypt(plaintext))

print(ciphertext)