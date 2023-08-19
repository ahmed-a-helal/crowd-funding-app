from hashlib import sha512

def EncryptPass(salt:str,password:str):
    password = str(salt)+password
    return sha512(password.encode()).hexdigest()