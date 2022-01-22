import os
usr=[{"Name":"swe","e-id":"swe@gmail.com","pin":310,"wallet":5000,"id":1,"frnds":[],"group":[]},{"Name":"mythili","e-id":"myma@gmail.com","pin":812,"wallet":15000,"id":2,"frnds":[],"group":[]},{"Name":"thiru","e-id":"thiru@gmail.com","pin":274,"wallet":15000,"id":3,"frnds":[],"group":[]},{"Name":"hari","e-id":"hari@gmail.com","pin":131,"wallet":2000,"id":4,"frnds":[],"group":[]}]
due=[]
grp=[]
def signin():
    s=input("\nEnter you name        :")
    id=input("Enter mail id         :")
    pin=int(input("Enter pin            :"))
    wal=int(input("Enter wallet amount  :"))
    uid=len(usr)+1
    d={"Name":s,"e-id":id,"pin":pin,"wallet":wal,"id":uid,"frnds":[],"group":[]}
    print("Your ID is :",uid)
    usr.append(d)
    input("\t\t\tAdded sucessfully\n\t\t\tPress anykey to continue")
def viewgrp(k):
    os.system('cls')
    print("\t\t\tGROUP LIST")
    for i in grp:
        l=list(i["Members"])
        if(k in l):
            print("\nGroup name   :",i["Group name"],"\nGroup id    :",i["Group id"])
            for j in range(len(l)):
                for x in usr:
                    if(x["id"]==l[j]):
                        if(j==0):
                            print("Admin    :",x["Name"],"--",x["id"])
                        else:
                            print("member   :",x["Name"],"--",x["id"])
def addexpense(k):
    while(True):
        os.system('cls')
        print("\n1.Non group expense\n2.Group expense\n3.Exit")
        choice=int(input("\nEnter choice    :"))
        if(choice==1):
            viewfrns(k)
            n=int(input("\nEnter friends count    :"))
            d=input("Enter discription  :")
            amt=int(input("Enter amount :"))
            print("\n1.Split equally\n2.Split not equally")
            d={"Discription":d,"Total amount":amt}
            ch=int(input("Enter choice  :"))
            l=[k]
            l1=["Not paid" for i in range(n+1)]
            if(ch==1):
                for i in range(n):
                    p=int(input("\nEnter Friend ID  :"))
                    l.append(p)
                    d["Members"]=l
                ls=[amt//(n+1) for i in range(n+1)]
                d["Each share"]=ls
                d["Payment"]=l1
                d["Status"]="Split equally"
                a=amt/(n+1)
                d["Due no"]="due"+str(len(due)+1)
                due.append(d)
                input("Press any key to continue")
            elif(ch==2):
                l1=[]
                l2=["Not paid" for i in range(n+1)]
                a=int(input("\nEnter your share :"))
                l1.append(a)
                for i in range(n):
                    p=int(input("\nEnter Friend ID  :"))
                    sh=int(input("Enter share   :"))
                    l.append(p)
                    l1.append(sh)
                    d["Members"]=l
                    d["Each share"]=l1
                d["Payment"]=l2
                d["Status"]="Not split equally"
                d["Due no"]="due"+str(len(due)+1)
                due.append(d)
                input("Press any key to continue")
        elif(choice==2):
            viewgrp(k)
            s=input("\nEnter group name   :")
            id=input("Enter group id    :")
            d=input("Enter discription  :")
            m=int(input("Enter amount :"))
            d={"Discription":d,"Total amount":m}
            for i in grp:
                if(i["Group name"]==s and id==i["Group id"]):
                    lm=list(i["Members"])
                    mn=len(lm)
                    eachshare=m/mn
                    ls=[eachshare for x in range(mn)]
                    l2=["Not paid" for i in range(mn)]
                    d["Members"]=lm
                    d["Each share"]=ls
                    d["Payment"]=l2
                    d["Due no"]="due"+str(len(due)+1)
            due.append(d)
            input("\t\t\tDone\n\t\t\tPress any key to continue")
        else:
            break       
def updatewallet(id):
    amt=int(input("\nEnter amount   :"))
    for i in usr:
        if(i["e-id"]==id):
            i["wallet"]+=amt
            print("Wallet amount    :",i["wallet"])
            break
    input("Press any key to continue")
def creategroup(k):
    s=input("\nEnter group name   :")
    n=int(input("\nEnter count of group members :"))
    id="GR"+str(len(grp)+1)
    d={"Group name":s,"Group id":id}
    l=[k]
    for i in range(n):
        b=int(input("Enter ID   :"))
        l.append(b)
        d["Members"]=l
    grp.append(d)
    input("\t\t\tCreated \n\t\t\tPress any key to continue")
def addfrnds(k):
    os.system('cls')
    for i in usr:
        if(i["id"]!=k):
            print("\nName   :",i["Name"],"\nID    :",i["id"])
        else:
            l=i["frnds"]
    n=int(input("\nEnter count  :"))
    for i in range(n):
        p=int(input("\nEnter friend ID   :"))
        for j in usr:
            l1=j["frnds"]
            if(j['id']==k):
                l.append(p)
                j["frnds"]=l
            if(j["id"]==p):
                l1.append(k)
                j["frnds"]=l1
    input("\t\t\tPress any key to continue")
def removefrnds(k):
    n=int(input("\nEnter count    :"))
    for i in range(n):
        id=int(input("Enter ID  :"))
        for j in usr:
            l=j["frnds"]
            if(j["id"]==id):
                l.remove(k)
                j["frnds"]=l
            if(j["id"]==k):
                l.remove(id)
                j["frnds"]=l
    input("\t\t\tRemoved\n\t\t\tPress any key to continue")
def viewfrns(k):
    os.system('cls')
    print("\t\t\tFRIENDDS LIST")
    for i in usr:
        if(k==i["id"]):
            l=i["frnds"]
            break
    for i in usr:
        for j in l:
            if(j==i["id"]):
                print("\nName   :",i["Name"],"\nId    :",i["id"])
def addfrndgrp(k):
    s=input("\nEnter group name   :")
    id=input("Enter gruop id")
    for i in grp:
        if(i["Group name"]==s and id==i["Group id"]):
            l=i["Members"]
            if(k==l[0]):
                m=int(input("Enter count of member  :"))
                for j in range(m):
                    b=int(input("Enter user ID  :"))
                    l.append(b)
                    i["Members"]=l
                input("\t\t\tAdded\n\t\t\tPress any key to continue")
            else:
                input("\t\t\tAdmin can add or remove a members")    
def removefrndgrp(k):
    s=input("\nGroup name :")
    id=input("Enter group id    :")
    for i in grp:
        if(s==i["Group name"] and i["Group id"]==id):
            l=list(i["Members"])
            if(k==l[0]):
                m=int(input("Enter count    :"))
                for j in range(m):
                    id=int(input("Enter user ID :"))
                    for x in usr:
                        if(x["id"]==id):
                            l.remove(id)
                            i["Members"]=l
                input("\t\t\tRemoved\n\t\t\tPress any key to continue")
            else:
                input("\t\t\tAdmins alone can add or remove members")
def viewdue(k):
    os.system("cls")
    print("\t\t\tDUE LIST")
    for i in due:
        l=list(i["Members"])
        l1=list(i["Payment"])
        ls=list(i["Each share"])
        f=False
        if(k in l):
            ind=l.index(k)
            if(l1[ind]=="Not paid"):
                print("\n\nDue No:",i["Due no"],"\nDescription  :",i["Discription"],"\nTotal amount :",i["Total amount"])
                f=True
        if(f):
            for i in range(len(l)):
                for x in usr:
                    if(x["id"]==l[i]):
                        if(i==0):
                            print("\tSender Name :",x["Name"],"\nShare :",ls[i],"\nStatus  :",l1[i])
                        else:
                            print("\tReceiver Name :",x["Name"],"\nShare :",ls[i],"\nStatus  :",l1[i])
def paydue(k):
    print("\n\n")
    n=input("Enter due no   :")
    for i in due:
        if(i["Due no"]==n):
            l=list(i["Members"])
            l1=list(i["Payment"])
            ls=list(i["Each share"])
            if(k in l):
                ind=l.index(k)
                for j in usr:
                    if(j["id"]==k):
                        a=ls[ind]
                        if(j["wallet"]>=a):
                            j["wallet"]-=a
                            l1[ind]="Paid"
                            i["Payment"]=l1
                        else:
                            print("\t\t\tWallet amount is not enough")
    input("\t\t\tDone")
def history(k):
    os.system("cls")
    print("\t\t\tHISTORY ")
    for i in due:
        l=list(i["Members"])
        l1=list(i["Payment"])
        ls=list(i["Each share"])
        f=False
        if(k in l):
            print("\n\nDue No:",i["Due no"],"\nDescription  :",i["Discription"],"\nTotal amount :",i["Total amount"])
            f=True
        if(f):
            for i in range(len(l)):
                for x in usr:
                    if(x["id"]==l[i]):
                        if(i==0):
                            print("\tSender Name :",x["Name"],"\nShare :",ls[i],"\nStatus  :",l1[i])
                        else:
                            print("\tReceiver Name :",x["Name"],"\nShare :",ls[i],"\nStatus  :",l1[i])
    input("\t\t\tPress any key to continue")
def login():
    id=input("\nEnter e-id    :")
    pin=int(input("Enter pin     :"))
    for i in usr:
        if(id==i["e-id"] and pin==i["pin"]):
            k=i["id"]
            while(True):
                os.system('cls')
                print("\n\t\t\tWelcome",i["Name"],"!!!\n1.Add a friend\n2.Remove a friend\n3.View frnds list\n4.Create a group \n5.Add fridends into group\n6.Remove friends from group\n7.view group\n8.Add an Expense\n9.View wallet\n10.Update wallet amount\n11.view pending dues\n12.Pay pending dues\n13.View their transaction history\n14.log out")
                c=int(input("\nEnter choice    :"))
                if(c==1):
                    addfrnds(k)
                    continue
                elif(c==2):
                    viewfrns(k)
                    removefrnds(k)
                    continue
                elif(c==3):
                    viewfrns(k)
                    input("\t\t\tPress any key to continue")
                    continue
                elif(c==8):
                    addexpense(k)
                elif(c==9):
                    print("\n\nWallet amount    :",i["wallet"])
                    input("Press any key to continue")
                elif(c==10):
                    updatewallet(id)
                elif(c==4):
                    viewfrns(k)
                    creategroup(k)
                elif(c==5):
                    viewfrns(k)
                    addfrndgrp(k)
                elif(c==6):
                    viewgrp(k)
                    removefrndgrp(k)
                elif(c==7):
                    viewgrp(k)
                    input("\t\t\tPress any key to continue") 
                    continue
                elif(c==11):
                    viewdue(k)
                    input("\t\t\tPress any key to continue")
                elif(c==12):
                    viewdue(k)
                    paydue(k)
                elif(c==13):
                    history(k)
                else:
                    break
while(True):
    os.system('cls')
    print("\n\t\t\tSPLITWISE APPLICATION\n1.Sign up\n2.Log in\n3.Exit")
    ch=int(input("\nEnter choice:"))
    if(ch==1):
        signin()
    elif(ch==2):
        login()
    else:
        print("\n\n\t\t\t\THANK YOU FOR USING SPLITWISE")
        break