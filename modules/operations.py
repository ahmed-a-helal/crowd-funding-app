from modules.inputs import inputdate,inputdescription,inputfund,inputitle,insertyes,getindex,editdate,editdescription,editfund,edititle
from modules.filemanipulation import modifyfile,getprojects
from tabulate import tabulate
@modifyfile
def CreatProject(userdata):
    projectdict={}
    print("\tnote ==> Title doesn't accept symbols or uncorrectly formatted words like p@ss or l44t or teSt")
    projectdict["Title"]=inputitle("Insert the project title: ")
    print("\tnote ==> The Money is in 'number < 3 character-currencycode>' ex: 25000EGP or 25000 USD")
    projectdict["Total Target"]=inputfund("Insert the project Total Target: ")

    print("\tnote ==> The Date is in this formaula yyyy-mm-dd")
    while True:
        projectdict["Start Date"]=inputdate("Insert the project Start Date: ")
        projectdict["End Date"]=inputdate("Insert the project End Date: ")
        
        if projectdict["End Date"] > projectdict["Start Date"]:
            break
        print ("Project end Date must be after project start date")
    print("\tnote ==> Enter at least 6-word description")
    projectdict["Description"]=inputdescription("Insert the project description: ")
    if not insertyes():
        print("The process have been halted")
        return False
    userdata["Projects"].append(projectdict)
    return userdata

def ViewProjects(*args,showindex:bool=False):
    projects=getprojects(*args)
    print(tabulate(projects,showindex=showindex,headers="keys"))
    
    
@modifyfile    
def RemoveProject(userdata):
    index=int(getindex(message="Insert the index of the selected project: "))
    if index >= len(userdata["Projects"]):
        print("There is no project with this index")
        return False
    elif not insertyes():
        print("The process have been halted")
        return False
    else:
        userdata['Projects'].pop(index)
        print("Deleting the project")
        return userdata
    
@modifyfile
def EditProject(userdata):
    index=int(getindex(message="Insert the index of the selected project: "))
    if index >= len(userdata["Projects"]):
        print("There is no project with this index")
        return False
    else:
        print('Current Project entries: ')
        print(tabulate([userdata['Projects'][index],],headers="keys"))
        print('\n\tInsert Enter if you do not want to change current value\n')
        print("\tnote ==> Title doesn't accept symbols or uncorrectly formatted words like p@ss or l44t or teSt")
        userdata['Projects'][index]["Title"]=edititle("Insert the project title: ",oldvalue=userdata['Projects'][index]["Title"])
        print("\tnote ==> The Money is in 'number < 3 character-currencycode>' ex: 25000EGP or 25000 USD")
        userdata['Projects'][index]["Total Target"]=editfund("Insert the project Total Target: ",userdata['Projects'][index]["Total Target"])

        print("\tnote ==> The Date is in this formaula yyyy-mm-dd")
        while True:
            userdata['Projects'][index]["Start Date"]=editdate("Insert the project Start Date: ",oldvalue=userdata['Projects'][index]["Start Date"])
            userdata['Projects'][index]["End Date"]=editdate("Insert the project End Date: ",oldvalue=userdata['Projects'][index]["End Date"])
            
            if userdata['Projects'][index]["End Date"] > userdata['Projects'][index]["Start Date"]:
                break
            print ("Project end Date must be after project start date")
        if not insertyes():
            print("The process have been halted")
            return False
        else:
            return userdata
        
        