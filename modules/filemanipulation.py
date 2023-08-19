from os import makedirs,listdir,path
import json
Dir="Database"

def readfile(filename:str,Dir=Dir):
    filepath = path.abspath(path.join(Dir,filename))
    makedirs(Dir, exist_ok=True)
    with open(filepath,mode="r")as json_file:
        return json.load(json_file)
         

def writefile(Data:dict,filename:str,Dir=Dir):
    filepath = path.abspath(path.join(Dir,filename))
    makedirs(Dir, exist_ok=True)
    with open(filepath,mode="w")as json_file:
        json.dump(Data,fp=json_file)

def lsfile(Dir=Dir):
    return listdir(Dir)

# decorator
def modifyfile(func):
    def inner(filename:str,Dir=Dir,*args, **kwargs):
        filepath = path.abspath(path.join(Dir,filename))
        makedirs(Dir, exist_ok=True)
        with open(filepath,mode="r+")as json_file:
            userdata=json.load(json_file)
            userdata=func(userdata=userdata,*args, **kwargs)
            if userdata :
                json_file.seek(0, 0)
                json.dump(userdata,fp=json_file)
                json_file.truncate()
                return True
            return False
    return inner

@modifyfile
def test(userdata,message):
    return userdata
if __name__ == "__main__":
    test(message='hi',filename="ahmed@gmail.com")
    
def getprojects(*args):
    projects=[]
    for file in args:
        userdata=readfile(filename=file)
        projects.extend(userdata["Projects"])
    return projects