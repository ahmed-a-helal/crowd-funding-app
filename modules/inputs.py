from modules.validation import *
from getpass import getpass
from modules.encryption import EncryptPass

def inputTemp(checkfn,message:str):
    while True:
        UsrInput=input(message)
        if checkfn(UsrInput):
            return UsrInput
        print("Your input is not valid")

def inputTemops(checkfn,operation,message:str):
    while True:
        UsrInput=operation(input(message))
        if checkfn(UsrInput):
            return UsrInput
        print("Your input is not valid")

def editTemops(checkfn,operation,oldvalue,message:str):
    while True:
        UsrInput=operation(input(message))
        if not UsrInput:
            return oldvalue
        elif checkfn(UsrInput):
            return UsrInput
        print("Your input is not valid")
        
def editTemp(checkfn,oldvalue,message:str):
    while True:
        UsrInput=input(message)
        if not UsrInput:
            return oldvalue
        elif checkfn(UsrInput):
            return UsrInput
        print("Your input is not valid")

def inputname(message:str):
    return inputTemp(message=message,checkfn=checkalpha)

def inputphone(message:str):
    return inputTemp(message=message,checkfn=checkphone)

def inputmail(message:str):
    return inputTemp(message=message,checkfn=checkmail)

def inputfund(message:str):
    return inputTemops(message=message,operation=lambda x: x.upper(),checkfn=CheckMoney)

def inputdate(message:str):
    return inputTemp(message=message,checkfn=checkdate)

def inputitle(message:str):
    message=message.title()
    return inputTemops(message=message,operation=lambda x: x.title(),checkfn=CheckTitle)

def inputdescription(message:str):
    return inputTemp(message=message,checkfn=checkdescription)



def editfund(message:str,oldvalue:str):
    return editTemops(message=message,oldvalue=oldvalue,operation=lambda x: x.upper(),checkfn=CheckMoney)

def editdate(message:str,oldvalue:str):
    return editTemp(message=message,oldvalue=oldvalue,checkfn=checkdate)

def edititle(message:str,oldvalue:str):
    message=message.title()
    return editTemops(message=message,oldvalue=oldvalue,operation=lambda x: x.title(),checkfn=CheckTitle)

def editdescription(message:str,oldvalue:str):
    return editTemp(message=message,oldvalue=oldvalue,checkfn=checkdescription)

def PassCreate(salt:str,
                   message1:str="Enter your Password: ",
                   message2:str="Enter The Same Password Again: "):
    while True:
        password1=getpass(message1)
        if len(password1) < 7:
            print("Your Password is too short, the password atleast must be 7 charchters long")
        elif not CheckPass(password1):
            print("You must use combination of uppercase and lowercase charachters and numbers only with no symbols")
        else:
            password2=getpass(message2)
            if password1 == password2:
                password=EncryptPass(password=password1,salt=salt)
                print("The Password Has been created successfully")
                return password
            else:
                print ("The password doesn't match please try again")



def LoginMail(mailist,message="Enter your mail: "):
    """
    this function compares the user's mail with mail list
    if the mail exist output -> mail:str
    if the mail doesn't exist return -> False 
    """
    for i in range(3):
        mail=inputmail(message=message).lower()
        if  ChckMailExist(mailist=mailist,mail=mail):
            return mail
    else:
        return False



def RegMail(mailist,message="Enter your mail: "):
    while True:
        mail=inputmail(message=message).lower()
        if not ChckMailExist(mailist=mailist,mail=mail):
            return mail
        else:
            print("This Mail is Unavailable, use another mail")

def LoginPass(hashedpass:str,salt:str,message:str):
    for _ in range(3):
        password=getpass(message)
        if len(password) < 7 and  not CheckPass(password) :
            print("Your Password is invalid, Try again")
        else:
            password=EncryptPass(password=password,salt=salt)
            if password == hashedpass:
                return True
    else:
        return False
def insertyes(message="If u want to perform this operation insert 'yes': "):
    selection= input(message)
    return yesorno(selection)
    
def getindex(message):
    return inputTemp(message=message,checkfn=isnumber)