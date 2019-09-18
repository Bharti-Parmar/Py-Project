import os
#to list all files and folders in a list
def listDir(path):
    ListOfFiles=os.listdir(path)
    print("files in folder: ")
    for i in range(len(ListOfFiles)):
        print(ListOfFiles[i])

def countFile(fullPath):
    f1=0
    f2=0
    f3=0
    if os.path.isfile(fullPath):
        if fullPath.endswith(".txt"):
            f1+=1
        elif fullPath.endswith(".html"):
            f2+=1
        elif fullPath.endswith(".py"):
            f3+=1
        else:
            pass
    else:
        pass
    return f1,f2,f3

def getFiles(fpath):
    ListofFiles=os.listdir(fpath)
    print("full path: ")
    for files in ListofFiles:
        #print("files is: "+files)
        fullPath=os.path.join(fpath,files)
        print(fullPath)
        f1,f2,f3=countFile(fullPath)
    print()
    tf=f1+f2+f3
    print("total files: "+str(tf))
    print("no of txt files: "+str(f1))
    print("no of html files: "+str(f2))
    print("no of python files: "+str(f3))




print("enter path: ")
path=input()
#listDir(path)
print()
getFiles(path)