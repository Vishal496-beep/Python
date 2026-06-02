from pathlib import Path
import os 
def createfile():
    try:
        name = input("Enter file name you want to create:-  ")
        path = Path(name)
        if not path.exists():
            with open(path, "w") as fs:
                data = input("What you want to write:- ")
                fs.write(data)
            print("file created successfully")
        else:
            print("Error file name already exists")

    except Exception as err:
        print(f"an error occured {err}")


def readfile():
    try: 
       name = input("Enter name of the file you want to read:- ")
       path = Path(name)
       if path.exists():
           with open(path, "r") as fs:
               content = fs.read()
               print(f"your file content is \n {content}")
       else:
         print("file doesn't exists")
           
    except Exception as err:
        print(f"an error occured as {err}")

def updatefile():
    try: 
        name = input("Enter the file name you want to update:- ")
        path = Path(name)
        if path.exists():
            print("operations:- ")
            print("1. renaming the file:- ")
            print("2: appending the file:- ")
            print("3. overwriting the file:- ")
            choice = int(input("Enter your choice as <1> for rename <2> for append <3> for overWrite:- "))
            if choice == 1:
                newname = input("Enter new file name:- ")
                new_path = Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("renamed successfully")
                else:
                    print("file already exists")
            elif choice == 2:
                with open(path,"a") as fs:
                    data = input("What do you want to append:- ")
                    fs.write("\n"+data)
                    print("successfully appended")
            elif choice == 3:
                with open(path,"w") as fs:
                    data = input("what do you want you overwrite:- ")
                    fs.write(data)
                    print("successfully overwritten")
    except Exception as err:
        print(f"an error occured while upding file as {err}")

def deletefile():
    try: 
        name = input("Enter file name you want to delete:- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("file deleted successfully")
        else:
            print("file doesnt exists")
    except Exception as err:
        print(f"error occured as {err}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")




a = int(input("\n tell your response:- "))

if a == 1:
    createfile()

if a == 2:
    readfile()

if a == 3:
    updatefile()

if a == 4:
    deletefile()