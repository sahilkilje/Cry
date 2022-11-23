import bcrypt
pwd = input()
falsePwd = "falsepassword"
bytePwd = pwd.encode('utf-8')
byteFalsepwd = falsePwd.encode('utf-8')

# Generate salt
mySalt = bcrypt.gensalt()

# Hash password
hash = bcrypt.hashpw(bytePwd, mySalt)
print(hash)
print(bcrypt.checkpw(bytePwd, hash))
print(bcrypt.checkpw(byteFalsepwd, hash))
