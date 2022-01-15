import os
import shutil
import time

path = input("Enter the name of a Directory to be updated: ")
time = input("What is the number of days you wish to set the limit to?: ")
listOfFiles = os.walk(path)

if os.path.exists(path):
    for file in listOfFiles:
        os.path.join()
        ctime = os.stat(path).st_ctime
        if ctime > time:
            os.remove(path)
        else:
            shutil.rmtree()
else:
    print("Path does not exist")