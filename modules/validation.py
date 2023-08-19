from re import match
def checkregextemp(pattern:str,string:str):
    return bool(match(string=string,pattern=pattern))

def checkphone(phonenum:str):
    pattern='^01[0125]\d{8}$'
    return checkregextemp(pattern=pattern,string=phonenum)

def checkdate(date:str):
    pattern='^([0-9]{4}-(0[0-9]|1[0-2]){1}-(([0-2][0-9])|(3[0-1])))*$'
    return checkregextemp(pattern=pattern,string=date)

def checkmail(mail:str):
    pattern='^([\da-zA-z][-_.]{0,1})+@(?<![-_.]@)[\da-zA-Z]([-]{0,1}[\da-zA-Z])*(\.[a-z]{2,})+$'
    return checkregextemp(pattern=pattern,string=mail)

def checkalpha(string:str):
    return string.isalpha()
 
def CheckPass(password):
    pattern='^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-z0-9]+$'
    return checkregextemp(pattern=pattern,string=password)

def CheckTitle(string):
    return string.istitle()

def CheckMoney(amount):
    pattern='^[0-9]+\s?[A-Z]{3}$'
    return checkregextemp(pattern=pattern,string=amount)

def checkdescription(description):
    pattern='^([A-Za-z0-9]+\s+){4,}[A-Za-z0-9]+\s*$'
    return checkregextemp(pattern=pattern,string=description)

def ChckMailExist(mailist,mail):
    if mail in mailist:
        return True
    else:
        return False

def isnumber(num):
    return num.isnumeric()

def yesorno(selection):
    pattern='^[yY]([eE][Ss])?$'
    return checkregextemp(pattern=pattern,string=selection)

