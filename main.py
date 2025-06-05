
import CMS as c
b=int(input("enter number:\n1-add contact\n2-view contacts\n3-search contect\n4-update contact\n5-delete contact-->"))
if b==1:
    m=input("enter name to add: ")
    n=input("enter number to add: ")
    c.addnumber(m,n)
    print(f"your contact has been added")

elif b==2:
    print("**your contacts list**")
    c.viewlist()
elif b==3:
    h=input("enter name to find: ")
    c.find_contact("mummy")
elif b==4:
    h1=input("enter name to update: ")
    c.update(h1)
elif b==5:
    h2=input("enter name to remove: ")
    c.r(h2)
    print(f"contact {h2} has been deleted")
else:
    print("please enter number between 1 to 5")