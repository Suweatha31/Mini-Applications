import os
import datetime
os.system('cls')
a=[{"name":"Swetha","pswd":3110},{"name":"Mythili","pswd":8120}]
u=[{"name":"Raji","pswd":8070,"balance":40000,"bank":"LVB","count":0,"acnt":10000},{"name":"Govind","pswd":2712,"balance":30000,"bank":"SBI","count":0,"acnt":100001}]
amt={"100":0,"200":0,"500":0,"2000":0}
def load():
    os.system('cls')
    z="->Date and Time:"+str(datetime.datetime.now())
    r="Admin->Load"+z
    print("\t\t\tAdmin-load page")
    l3.append(r)
    for i in amt:
        print("Enter",i,"count:")
        q=int(input())
        amt[i]+=q
def show():
    os.system('cls')
    z="->Date and Time:"+str(datetime.datetime.now())
    r="Admin->show"+z
    l3.append(r)
    for i in amt:
        print(i,"=",amt[i])
def balance(s1):
    z="->Date and Time:"+str(datetime.datetime.now())
    r="Customer->Balance"+z
    l3.append(r)
    os.system('cls')
    print("\t\t\tCustomer->Balance page")
    for i in u:
        if(i["name"]==s1):
            print(i["balance"])
def withdraw(s1,p1):
    z="->Date and Time:"+str(datetime.datetime.now())
    r="Customer->Withdraw"+z
    l3.append(r)
    os.system('cls')
    print("\t\t\tCustomer-Withdraw page")
    m=0
    amt1=amt
    for i in u:
        if(i["name"]==s1 and i["pswd"]==p1):
            l1=[]
            for j in amt1:
                t=int(input("Enter "+str(j)+" rupee note u want: "))
                if(amt1[j]>=t):
                    amt1[j]-=t
                    m+=int(j)*t
                    l1.append(t)
                else:
                    print("\t\t\tAvailability of",j,"repees note is",amt1[j])
                    break
            else:
                if(m<=i["balance"]):
                    if(i["bank"]=="SBI" or (i["bank"]!="SBI" and i["count"]<3)):
                        i["balance"]-=m
                        i["count"]+=1
                    else:
                        i["balance"]-=(m+50)
                        i["count"]+=1
                        print("\t\t\t50 Rupees extra charge for bank limit exceeded")
                else:
                    print("\t\t\tInsuffient balance in ur account")
def deposite(s1,p1):
    os.system('cls')
    z="->Date and Time:"+str(datetime.datetime.now())
    r="Customer->Deposite"+z
    print("\t\t\tCustomer->Deposite")
    l3.append(r)
    m=0
    for i in amt:
        print("Enter",i,"count:")
        q=int(input())
        amt[i]+=q
        m+=(int(i)*q)
    for i in u:
        if(i["name"]==s1 and i["pswd"]==p1):
            i["balance"]+=m
            i["count"]+=1
    print("\t\t\tAmount deposited successfully.....")
def account_transfer(s1,p1):
    os.system('cls')
    z="->Date and Time:"+str(datetime.datetime.now())
    r="Customer->Account Transfer"+z
    print("\t\t\tCustomer->Account Transfer")
    l3.append(r)
    s=input("Enter receiver name    :")
    ac=int(input("Enter acnt num    :"))
    m=0
    os.system('cls')
    for i in amt:
        print("Enter",i,"count:")
        q=int(input())
        m+=(int(i)*q)
    for i in u:
        if(i["name"]==s1 and i["pswd"]==p1):
            if(m<=i["balance"]):
                d=i["balance"]
                if(i["bank"]=="SBI" or (i["bank"]!="SBI" and i["count"]<3)):
                    i["balance"]-=m
                    i["count"]+=1
                else:
                    i["balance"]-=(m-50)
                    i["count"]+=1
                    print("\t\t\t50 Rupees extra charge for bank limit exceeded")
            else:
                print("\t\t\tInsuffient balance in ur account")
        elif(i["name"]==s and i["acnt"]==ac):
            i["balance"]+=m
            print("\t\t\tamount transferred successfully.....")
        else:
            for j in u:
                if(j["name"]==s1 and j["pswd"]==p1):
                    j["balance"]=d
            print("\t\t\tReceiver name or acnt number or ifsc is wrong....")          
def ministatements(l3):
    os.system('cls')
    l4=l3[-1:-4:-1]
    for i in l4:
        print(i,end="\n\n")
def pinchange(s1,p1):
    os.system('cls')
    z="->Date and Time:"+str(datetime.datetime.now())
    r="Customer->Pin changer"+z
    print("\t\t\tCustomer->Pin change")
    l3.append(r)
    for i in u:
        if(i["name"]==s1 and i["pswd"]==p1):
            int(input("Enter ur new pin :"))
            i["pswd"]=int(input("Confirm ur pin :"))
            input("\t\t\tpin changed successfully\n\t\t\tPress any key to continue....")
            break
def adminpage():
        os.system('cls')
        print("\t\t\tAdmin!!!")
        s=input("Enter user name    :")
        p=int(input("Enter password :"))
        for i in a:
            if(i["name"]==s and i["pswd"]==p):
                while(True):
                    os.system('cls')
                    print("\t\t\tWELCOME",i["name"],"\n1.Load\n 2.show\n 3.Exit")
                    p=int(input("\nchoice:"))
                    if(p==1):
                        load()
                        print("\t\t\tAmount added sucessfully")
                        input("\t\t\tpress any key to continue......")
                    elif(p==2):
                        show()
                        input("\t\t\tPress any key to continue.......")
                        continue
                    elif(p==3):
                        print("\t\t\tThankyou for using this ATM......")
                        break
def customer(attempt):
    os.system('cls')
    print("Customer")
    s1=input("Enter user name   :")
    p1=int(input("Enter password    :"))
    for i in u:
        if(i["name"]==s1 and i["pswd"]==p1):
            break
    else:
        attempt-=1
        input("\t\t\tInvalid user name or password\n\t\t\tPress any key to continue..")
        if(attempt==0):
            print("\t\t\tLimit exceeded...plz try again later....")
            exit()
        else:
            customer(attempt)
    while(True):
        os.system('cls')
        print("\t\t\tWELCOME",i["name"],"!!!\n1.Balance check\n2.Withdraw\n3.Ministatements\n4.Pin change\n5.Deposite\n6.Amount Transfer\n7.Exit")
        r=int(input("choice:"))
        if(r==1):
            balance(s1)
            input("\t\t\tEnter any key to continue....")
            continue
        elif(r==2):
            x=withdraw(s1,p1)
            input("\t\t\tEnter any key to be continue.....")
            continue
        elif(r==3):
            ministatements(l3)
            input("\t\t\tEnter any key to continue...")
            continue
        elif(r==4):
            pinchange(s1,p1)
        elif(r==5):
            deposite(s1,p1)
            input("\t\t\tEnter any key to continue...")
            continue
        elif(r==6):
            account_transfer(s1,p1)
            input("\t\t\tEnter any key to continue...")
            continue
        else:
            print("Thank you for using this ATM....")
            break 
l3=[]
while(True):
    os.system('cls')
    print("\t\t\tATM Machine\n 1.Admin\n 2.Customer\n 3.Exit")
    n=int(input("choice:"))
    if(n==1):
        print("Admin")
        adminpage()
        continue
    elif(n==2):
        attempt=3
        print("Customer")
        customer(attempt)
        continue
    elif(n==3):
        print("\t\t\tThank you for banking with us.........")
        break
    else:
        print("Invalid Input")
        continue