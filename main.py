from modules.menu import Welcome_message,authorize,menu,project_operation

Welcome_message()
while True:
    try:
        menu("Register","login")
        selection=input("Enter Your selection: ")
        mail=authorize(selection=selection)
        if mail:
            while True:
                menu( "Create a Project","View my projects", "Edit a Project", "Remove a Project","View all Projects")
                selection=input("Enter Your selection: ")
                project_operation(selection=selection,filename=mail)
    except KeyboardInterrupt:
        print("\nThe App is terminating")
        exit()
    except Exception as e:
        raise e