import hmac
import hashlib
#Initial sent message
sent_msg = input("Enter message: ")
s_md_1 = hmac.new(b'secret-key',msg=sent_msg.encode(),digestmod=hashlib.md5)
init_msg_digest = s_md_1.hexdigest()
# Receieved Message
received = sent_msg
r_md_1 = hmac.new(b'secret-key',msg=received.encode(),digestmod=hashlib.md5)
recv_msg_digest = r_md_1.hexdigest()
#Comparing sent and received messages
print("----Before Tampering----")
print('Is the message received without any tampering:',hmac.compare_digest(init_msg_digest,recv_msg_digest))
#Tampered Message
tampered_msg = "Welcme to the encryption"
md_2 =hmac.new(b'secret-key',msg=tampered_msg.encode(),digestmod=hashlib.md5)
tampered_msg_digest = md_2.hexdigest()
#Comparing after tampering
print("----After Tampering----")
print('Is the message received without any tampering:',hmac.compare_digest(init_msg_digest,tampered_msg_digest))

