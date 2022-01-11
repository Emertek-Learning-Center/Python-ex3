########################################################
#this exercice is detailed the usage of files in python#
########################################################
def createFileIsNotExist(filename):
    try:
       with open(filename, 'a+') as f:
           pass
           f.close()
           print(f"{filename} is alredy exist")
           return True
    except:
        f = open(filename, "w")
        f.close()
        print(f"create new file calld {filename}")
        return False
    
def writeInFiles(ligne,filename):
    with open(filename, 'a+') as f:
        try:
            f.write(ligne)
            return True
        except:
            return False
    f.close()

def showFilesContent(filename):
    with open(filename, 'r') as f:
        for ligne in f:
            print(ligne)
    f.close()

if __name__ == '__main__':

    filename="file1.txt"
    createFileIsNotExist(filename)
    while True:
        client_name=input("Client name: ")
        client_age=float(input("Client age: "))
        client_email=input("Client email: ")
        string = client_name+" "+str(client_age)+" "+client_email+"\n"
        if writeInFiles(string,filename):
            print("Record add succesfully.")
        else:
            print("error in writing files.")
        print("Did you want to add annother record (Y/N): ")
        rep = input()
        if rep.lower() =='n':
            break
    showFilesContent(filename)
    




