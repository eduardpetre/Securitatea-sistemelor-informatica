from Crypto.Cipher import AES

key = b'O cheie oarecare'
# data = b'testtesttesttesttesttesttesttesttesttesttesttest'
data = b'test'

cipher = AES.new(key, AES.MODE_CCM)
# cipher.encrypt(data)
print(cipher.encrypt(data))