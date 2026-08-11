from pathlib import Path
import os


def readfileandfolder():
    path = Path('')
    items = list(path.glob('*'))

    for i, item in enumerate(items):
        print(f"{i + 1}: {item}")


def createfile():
    try:
        readfileandfolder()

        name = input("Please tell your file name :- ")
        p = Path(name)

        if not p.exists():
            with open(p, "w") as fs:
                data = input("What do you want to write in this file :- ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("THIS FILE ALREADY EXISTS")

    except Exception as err:
        print(f"AN ERROR OCCURRED: {err}")


def readfile():
    try:
        readfileandfolder()

        name = input("Which file do you want to read :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()

            print("\nFile Content:")
            print(data)
            print("FILE READ SUCCESSFULLY")

        else:
            print("FILE DOES NOT EXIST")

    except Exception as err:
        print(f"AN ERROR OCCURRED: {err}")


def updatefile():
    try:
        readfileandfolder()

        name = input("Please enter your file name :- ")
        p = Path(name)

        if p.exists() and p.is_file():

            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending some content in your file")

            res = int(input("Tell your response :- "))

            if res == 1:
                name2 = input("Tell your new file name :- ")
                p2 = Path(name2)

                p.rename(p2)
                print("FILE RENAMED SUCCESSFULLY")

            elif res == 2:
                with open(p, "w") as fs:
                    data = input("Tell what you want to write (this will overwrite existing data) :- ")
                    fs.write(data)

                print("FILE UPDATED SUCCESSFULLY")

            elif res == 3:
                with open(p, "a") as fs:
                    data = input("Tell what you want to append :- ")
                    fs.write(" " + data)

                print("CONTENT APPENDED SUCCESSFULLY")

            else:
                print("INVALID RESPONSE")

        else:
            print("FILE DOES NOT EXIST")

    except Exception as err:
        print(f"AN ERROR OCCURRED: {err}")


def deletefile():
    try:
        readfileandfolder()

        name = input("Please tell which file you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("FILE REMOVED SUCCESSFULLY")
        else:
            print("NO SUCH FILE EXISTS")

    except Exception as err:
        print(f"AN ERROR OCCURRED: {err}")


# Main Menu
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Please tell your response :- "))

if check == 1:
    createfile()

elif check == 2:
    readfile()

elif check == 3:
    updatefile()

elif check == 4:
    deletefile()

else:
    print("INVALID RESPONSE")
