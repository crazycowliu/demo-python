#AES-demo
import binascii
from Crypto.Cipher import AES 

#秘钥,此处需要将字符串转为字节 
key = b'abcdefgh' 

#加密内容需要长达16位字符，所以进行空格拼接
def pad(text): 
    while len(text) % 16 != 0: 
        text += b' ' 
    return text 

#进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
key = pad(key)
print("key=%s" % key)
aes = AES.new(key, AES.MODE_ECB) 

#加密内容,此处需要将字符串转为字节 
text = b'382211jjWW!@#$%^' 
#进行内容拼接16位字符后传入加密类中，结果为字节类型 
text = pad(text)
print("text=%s" % text)
encrypted_text = aes.encrypt(text) 
print("encrypted_text=%s" % encrypted_text) 
print("encrypted_text=%s" % binascii.b2a_hex(encrypted_text)) 

#用aes对象进行解密，将字节类型转为str类型，错误编码忽略不计
byte_arr = aes.decrypt(encrypted_text)
hex_str = binascii.b2a_hex(byte_arr)
print(hex_str)