from modules.authorization import login,register
from modules.filemanipulation import readfile,writefile,lsfile
from modules.operations import CreatProject,ViewProjects,RemoveProject,EditProject
def Welcome_message():
    print("#####################################################")
    print(">>>>>>>>>>>>>Welcome to The Funding App<<<<<<<<<<<<<")
    print("#####################################################")

def menu(*args):
    for i,arg in enumerate(args):
        print(f"{i+1}) {arg}")
    
def authorize(selection):
    if selection == "1" or "register" in selection.lower():
        userdata=register(mailist=lsfile())
        writefile(filename=userdata["Mail"],Data=userdata)
        print("The account has been registered successfully")
        return False
    elif selection == "2" or "login" in selection.lower():
        return login(readfn=readfile,mailist=lsfile())[0]
    else:
        print ("please enter a correct menu input") 
        
def project_operation(selection,filename):
    if selection == "1" or "create" in selection.lower():
        if CreatProject(filename=filename):
            print("The project has been created successfully")
            return True
        return False
    elif selection == "2" or "view" in selection.lower():
        ViewProjects(filename,showindex=True)
        return True
    elif selection == "3" or "edit" in selection.lower():
        if EditProject(filename=filename):
            print("The project has been edited successfully")
        print("There is no edits")
        return False
    
    
    elif selection == "4" or "remove" in selection.lower():
        if RemoveProject(filename=filename):
            print("The project has been deleted successfully")
            return True
        return False
    elif selection == "5" or "view all" in selection.lower():
        projects = ViewProjects(*lsfile())
    else:
        print ("please enter a correct menu input") 

