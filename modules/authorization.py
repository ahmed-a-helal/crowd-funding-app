from modules.inputs import inputTemp,inputname,inputphone,inputmail,PassCreate,LoginPass,LoginMail,RegMail
from time import time

    
def register(mailist):
    userdict={}
    userdict["First Name"]=inputname(message="Enter your first name: ")
    userdict["Last Name"]=inputname(message="Enter your last name: ")
    userdict["Mail"]=RegMail(mailist=mailist,message="Enter Your Mail: ")
    userdict["Phone Number"]=inputphone(message="Enter your Phone Number: ")
    userdict["Password Time Stamp"]=time()
    userdict["Password"]=PassCreate(salt=userdict["Password Time Stamp"],message1="Enter your Password: ",message2="Enter The Same Password Again: ")
    userdict["Projects"]=[]
    return userdict


def login(readfn,mailist):
    while True:
        mail=LoginMail(mailist,message="Enter your mail: ")
        if mail :
            userdata=readfn(filename=mail)
        else:
            print("Login failed")
            return False
        
        
        if LoginPass(hashedpass=userdata["Password"],
                              salt=userdata["Password Time Stamp"],
                              message="Enter your Password: "):
            print("Welcome, {firstname} {lastname} ".format(firstname=userdata["First Name"],lastname=userdata["Last Name"]).title())
            return (mail,userdata)
        else:
            print("Login failed")
            return False
    
    
if __name__ == "__main__":
    dictionary=register()
    
    
