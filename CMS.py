#add new contact.
def addnumber(name,number):
    with open("J:/Aimicrodegree/module_2_python/contact_management_system/contacts.txt","a+") as f1:
        if len(number)==10 and number.isdigit():
            f1.write(f"{name}={number}\n")
        else:
            print("please enter valid number")
def viewlist():
    with open("J:/Aimicrodegree/module_2_python/contact_management_system/contacts.txt","r") as f2:
        print(f2.read())
#search contact.
def find_contact(name):
    with open("J:/Aimicrodegree/module_2_python/contact_management_system/contacts.txt","r") as f3:
        l1=f3.readlines()
        found=0
        for i in l1:
            name1,num=i.strip().split("=")
            if name1==name:
                print(f"{name} is avaliable")
                found=1
                break
        if found==0:
                print(f"{name} is not avaliable")
#update contact.
def update(a):
    with open("J:/Aimicrodegree/module_2_python/contact_management_system/contacts.txt","r") as f3:
        l1=f3.readlines()
        found=0
        for i in range(len(l1)):
            name1,num=l1[i].strip().split("=")
            if name1==a:
                newname=input("enter new name: ")
                newnum=input("enter new number: ")
                l1[i]=(f"{newname}={newnum}\n")
                print(f"{a} is avaliable")
                found=1
                break
        if found==0:
                print(f"{a} is not avaliable")
    with open("J:/Aimicrodegree/module_2_python/contact_management_system/contacts.txt","w") as f3:
         f3.writelines(l1)
#delete contact.
def r(n):
    with open("J:/Aimicrodegree/module_2_python/contact_management_system/contacts.txt","r+") as f3:
        l1=f3.readlines()
        found=0
        for i in range(len(l1)):
            name1,num=l1[i].strip().split("=")
            if name1==n:
                del l1[i]
                found=1
                break
        if found==0:
                print(f"{n} is not avaliable")
        with open("J:/Aimicrodegree/module_2_python/contact_management_system/contacts.txt","w") as f3:
         f3.writelines(l1)