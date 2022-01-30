from datetime import date
import os
from subprocess import IDLE_PRIORITY_CLASS
ad=[{"name":"swe","password":310,"admin id":"ad1"}]
usr=[{"name":"mythili","password":812,"user id":"us1","wallet":40000}]
car=[{"car name":"swift","count":15,"borrow count":0,"number plate":[],"specification":"AC"},{"car name":"adi","count":5,"borrow count":0,"number plate":[],"specification":"AC"},{"car name":"swift","count":5,"borrow count":0,"number plate":[],"specification":"Non AC"}]
bike=[{"bike name":"royal enfied","count":10,"borrow count":0,"number plate":[],"specification":"120cc"},{"bike name":"duke","count":5,"borrow count":0,"number plate":[],"specification":"120cc"}]
borrow=[]
borrowcar=[]
cart=[]
fne=[]
for i in bike:
    lb=[]
    b=i["bike name"]
    b=b[:2]
    cnt=i["count"]
    for j in range(cnt):
        s=b+str(len(lb)+1001)
        lb.append(s)
    i["number plate"]=lb
for i in car:
    lb=[]
    b=i["car name"]
    b=b[:2]
    cnt=i["count"]
    for j in range(cnt):
        s=b+str(len(lb)+1001)
        lb.append(s)
    i["number plate"]=lb
def viewvehicle():
    while(True):
        os.system('cls')
        print("\n1.Two wheeler\n2.Four wheeler\n3.Exit")
        c=int(input("\nEnter choice :"))
        if(c==1):
            os.system('cls')
            print("\t\t\tTWO WHEELER LIST")
            for i in bike:
                print("\n")
                for j in i:
                    print(j,":",i[j])
            input("\n\n\t\t\tPress any key to continue")
        elif(c==2):
            os.system('cls')
            print("\t\t\tFOUR WHEELER LIST")
            for i in car:
                print("\n")
                for j in i:
                    print(j,":",i[j])
            input("\n\n\t\t\tPress any key to continue")
        else:
            break
def addvehicle():
    while(True):
        os.system('cls')
        c=int(input("\n1.Two wheeler\n2.Four wheeler\n3.exit\n\nEnter choice :"))
        if(c==1):
            k=int(input("\nEnter count of bike you want to add      :"))
            for j in range(k):
                d={}
                d["bike name"]=input("\nEnter bike name    :").lower()
                d["count"]=int(input("Enter count        :"))
                d["borrow count"]=int(input("Enter borrow count :"))
                d["number plate"]=[]
                b=d["bike name"]
                lb=[]
                b=b[:2]
                for i in range(d["count"]):
                    s=b+str(len(lb)+1)
                    lb.append(s)
                d["number plate"]=lb
                d["specification"]=input("Enter specification   :")
                bike.append(d)
            input("\t\t\tPress any key to continue")
        elif(c==2):
            k=int(input("\nEnter count of car you want to add      :"))
            for j in range(k):
                d={}
                d["car name"]=input("\nEnter car name    :").lower()
                d["count"]=int(input("Enter count        :"))
                d["borrow count"]=int(input("Enter borrow count :"))
                d["number plate"]=[]
                b=d["car name"]
                lb=[]
                b=b[:2]
                for i in range(d["count"]):
                    s=b+str(len(lb)+1)
                    lb.append(s)
                d["number plate"]=lb
                d["specification"]=input("Enter specification   :")
                car.append(d)
            input("\t\t\tPress any key to continue")
        else:
            break
def removevehicle():
    while(True):
        os.system('cls')
        c=int(input("\n1.Two wheeler\n2.Four wheeler\n3.exit\n\nEnter choice :"))
        if(c==1):
            os.system('cls')
            print("\t\t\tBIKE LIST")
            for i in bike:
                print("\n")
                for j in i:
                    print(j,":",i[j])
            k=int(input("\nEnter count of bike you want to remove      :"))
            for j in range(k):
                b=input("\nEnter bike name      :").lower()
                no=input("Enter number plate   :")
                sp=input("Enter specification  :")
                for i in bike:
                    if(i["bike name"]==b and i["specification"]==sp):
                        i["count"]-=1
                        ls=i["number plate"]
                        ls.remove(no)
                        i["number plate"]=ls
            input("\t\t\tRemoved\n\t\tPress any key to continue")
        elif(c==2):
            os.system('cls')
            print("\t\t\tCAR LIST")
            for i in car:
                print("\n")
                for j in i:
                    print(j,":",i[j])
            k=int(input("\nEnter count of car you want to remove      :"))
            for j in range(k):
                b=input("\n\nEnter car name      :").lower()
                no=input("Enter number plate   :")
                sp=input("Enter specification  :")
                for i in car:
                    if(i["car name"]==b and i["specification"]==sp):
                        i["count"]-=1
                        ls=i["number plate"]
                        ls.remove(no)
                        i["number plate"]=ls
            input("\t\t\tRemoved\n\t\tPress any key to continue")
        else:
            break
def modifyvehicle():
    while(True):
        os.system('cls')
        c=int(input("\n1.Two wheeler\n2.Four wheeler\n3.exit\n\nEnter choice :"))
        if(c==1):
            os.system('cls')
            print("\t\t\tBIKE LIST")
            for i in bike:
                print("\n")
                for j in i:
                    print(j,":",i[j])
            k=int(input("\nEnter count of bike you want to modify     :"))
            for j in range(k):
                b=input("\nEnter bike name      :").lower()
                sp=input("Enter specification  :")
                for i in bike:
                    if(i["bike name"]==b and i["specification"]==sp):
                        i["count"]=int(input("Enter count(new)          :"))
                        lb=[]
                        b=b[:2]
                        for x in range(i["count"]):
                            s=b+str(len(lb)+1)
                            lb.append(s)
                            i["number plate"]=lb
            input("\t\t\tModified\n\t\tPress any key to continue")
        elif(c==2):
            os.system('cls')
            print("\t\t\tCAR LIST")
            for i in car:
                print("\n")
                for j in i:
                    print(j,":",i[j])
            k=int(input("\nEnter count of car you want to modify      :"))
            for j in range(k):
                b=input("\n\nEnter car name      :").lower()
                sp=input("Enter specification  :")
                for i in car:
                    if(i["car name"]==b and i["specification"]==sp):
                        i["count"]=int(input("Enter count(new)          :"))
                        lb=[]
                        b=b[:2]
                        for x in range(i["count"]):
                            s=b+str(len(lb)+1)
                            lb.append(s)
                            i["number plate"]=lb
            input("\t\t\tModified\n\t\tPress any key to continue")
        else:
            break
def search():
    while(True):
        os.system('cls')
        c=int(input("\n1.Two wheeler\n2.Four wheeler\n3.exit\n\nEnter choice :"))
        if(c==1):
            while(True):
                os.system('cls')
                p=int(input("\n1.Name based search\n2.Number plate based search\n3.Exit\n\nEnter choice :"))
                if(p==1):
                    b=input("\n\nEnter bike name    :").lower()
                    for i in bike:
                        if(i["bike name"]==b.lower()):
                            print("\n")
                            for j in i:
                                print(j,":",i[j])
                            break
                    else:
                        print("\t\t\tBike name not exist")
                    input("\t\t\tPress any key to continue")
                elif(p==2):
                    no=input("\nEnter number plate  :")
                    for i in bike:
                        if(no in i["number plate"]):
                            print("\n\nBike name    :",i["bike name"],"\nSpecification :",i["specification"])
                            break
                    else:
                        print("\n\t\t\tNumber plate is not exist")
                    input("\t\t\tPress any key to continue")
                else:
                    break
        elif(c==2):
            while(True):
                os.system('cls')
                p=int(input("\n1.Name based search\n2.Number plate based search\n3.Exit\n\nEnter choice :"))
                if(p==1):
                    b=input("\n\nEnter car name    :").lower()
                    for i in car:
                        if(i["car name"]==b.lower()):
                            print("\n")
                            for j in i:
                                print(j,":",i[j])
                    input("\t\t\tPress any key to continue")
                elif(p==2):
                    no=input("\nEnter number plate  :")
                    for i in car:
                        if(no in i["number plate"]):
                            print("\n\ncar name     :",i["car name"],"\nSpecification :",i["specification"])
                    input("\t\t\tPress any key to continue")
                else:
                    break
        else:
            break
def seevehicle():
    while(True):
        os.system('cls')
        print("\n1.Two wheeler\n2.Four wheeler\n3.Exit")
        c=int(input("\nEnter choice :"))
        if(c==1):
            os.system('cls')
            print("\t\t\tTWO WHEELER LIST")
            for i in bike:
                print("\nbike name  :",i["bike name"],"\nspecification :",i["specification"])
            input("\n\n\t\t\tPress any key to continue")
        elif(c==2):
            os.system('cls')
            print("\t\t\tFOUR WHEELER LIST")
            for i in car:
                 print("\n\ncar name  :",i["car name"],"\nspecification :",i["specification"])
            input("\n\n\t\t\tPress any key to continue")
        else:
            break
def borrowvehicle(id):
     while(True):
        os.system('cls')
        print("\n1.Two wheeler\n2.Four wheeler\n3.Exit")
        c=int(input("\nEnter choice :"))
        for i in usr:
                if(i["user id"]==id):
                    w=i["wallet"]
        if(c==1):
            os.system('cls')
            print("\t\t\tBIKE LIST")
            for i in bike:
                print("\n\nbike name :",i["bike name"],"\nSpecification :",i["specification"])
            bk=input("\n\nEnter Bike name   :").lower()
            sp=input("Enter specification   :")
            dt=input("Enter date    :")
            fl=True
            flag=True
            if(w<30000):
                print("\t\t\tWallet amount is not enough")
                flag=False
            for j in borrow:
                if(j["bike name"]==bk and j["user id"]==id):
                    print("\t\t\tYou cannot buy a same bike at same time")
                    fl=False
                    break
            else:
                if(flag):
                    for i in bike:
                        if(i["bike name"]==bk and i["specification"]==sp):
                            i["count"]-=1
                            i["borrow count"]+=1
                            ls=i["number plate"]
            p=""
            cnt=0
            if(len(borrow)>0 and fl):
                for i in ls:
                    if(cnt==0):
                        for j in borrow:
                            if(j["number plate"]==i):
                                continue
                            else:
                                p=i
                                cnt+=1
                                d={"user id":id,"bike name":bk,"specification":sp,"number plate":p,"Borrow date":dt}
                                borrow.append(d)
                                print("Number plate :",p)
                                break
                    elif(cnt==1):
                        break
            elif(len(borrow)==0 and fl and flag):
                p=ls[0]
                d={"user id":id,"bike name":bk,"specification":sp,"number plate":p,"Borrow date":dt}
                borrow.append(d)
                print("Number plate :",p)
            if(flag):
                for i in usr:
                    if(i["user id"]==id):
                        i["wallet"]-=30000
            input("\t\t\tpress any key to continue")
        elif(c==2):
            os.system('cls')
            print("\t\t\tCAR LIST")
            for i in car:
                print("\n\ncar name :",i["car name"],"\nSpecification :",i["specification"])
            bk=input("\n\nEnter car name   :").lower()
            sp=input("Enter specification   :")
            dt=input("Enter Date    :")
            fl=True
            flag=True
            if(w<30000):
                print("\t\t\tWallet amount is not enough")
                flag=False
            for j in borrowcar:
                if(j["car name"]==bk and j["user id"]==id):
                    print("\t\t\tYou cannot buy a same car at same time")
                    fl=False
                    break
            else:
                if(flag):
                    for i in car:
                        if(i["car name"]==bk and i["specification"]==sp):
                            i["count"]-=1
                            i["borrow count"]+=1
                            ls=i["number plate"]
            p=""
            cnt=0
            if(len(borrowcar)>0 and fl and flag):
                for i in ls:
                    if(cnt==0):
                        for j in borrowcar:
                            if(j["number plate"]==i):
                                continue
                            else:
                                p=i
                                cnt+=1
                                break
                    elif(cnt==1):
                        break
            elif(len(borrowcar)==0 and fl and flag):
                p=ls[0]
                d={"user id":id,"car name":bk,"specification":sp,"number plate":p,"Borrow date":dt}
                borrowcar.append(d)
                print("Number plate :",p)
            if(flag and fl):
                for i in usr:
                    if(i["user id"]==id):
                        i["wallet"]-=30000
            input("\t\t\tpress any key to continue")
        else:
            break   
def viewupdatewallet(id):
    for i in usr:
        if(i["user id"]==id):
            print("\nWallet amount    :",i["wallet"])
            c=int(input("\n1.Update\n2.Exit\n\nEnter choice :"))
            if(c==1):
                w=int(input("\n\nEnter amount   :"))
                i["wallet"]+=w
                input("\n\t\t\tUpdated\n\t\t\tPress any key to continue")
            else:
                break
def searchandcart(id):
    while(True):
        os.system('cls')
        c=int(input("\n1.Two wheeler\n2.Four wheeler\n3.exit\n\nEnter choice :"))
        f=False
        if(c==1):
            b=input("\n\nEnter bike name    :").lower()
            for i in bike:
                if(i["bike name"]==b):
                    f=True
                    print("\n")
                    print("Bike name    :",i["bike name"],"\nSpecifications   :",i["specification"])
            if(f):
                print("\n1.Add to cart\n2.Exit")
                ch=int(input("\nEnter choice    :"))
                if(ch==1):
                    sp=input("\nEnter specification :")
                    d={"user id":id,"vehicle":"bike","name":b,"specification":sp}
                    cart.append(d) 
                    print("\t\t\tAdded")
                input("\t\t\tPress any key to continue")
        elif(c==2):
            b=input("\n\nEnter car name    :").lower()
            for i in car:
                if(i["car name"]==b):
                    f=True
                    print("\n")
                    print("car name    :",i["car name"],"\nSpecifications   :",i["specification"])                        
            if(f):
                print("\n1.Add to cart\n2.Exit")
                ch=int(input("\nEnter choice    :"))
                if(ch==1):
                    sp=input("\nEnter specification :")
                    d={"user id":id,"vehicle":"car","name":b,"specification":sp}
                    cart.append(d) 
                    print("\t\t\tAdded")
                input("\t\t\tPress any key to continue")  
        else:
            break 
def viewcart(id):
    os.system('cls')
    print("\t\t\tCART LIST")
    for i in cart:
        if(i["user id"]==id):
            print("\n")
            for j in i:
                print(j,":",i[j])
    input("\t\t\tPress any key to continue")
def finelist(bk,np,id,dl):
    td=date.today()
    td=str(td)
    td=td[::-1]
    t=str(td).split(":")
    t=str(t)
    t1=t[2:4]
    t2=t[5:7]
    t3=t[8:12]
    t4=t1+":"+t2+":"+t3
    f=0
    for i in borrow:
        if(bk==i["bike name"] and np==i["number plate"] and id==i["user id"]):
            kms=int(input("Enter kms    :"))
            if(kms<=500):
                if(dl=="None"):
                    f=0
                    print("\n\t\t\tyour rent amount is 3000 balance 27,000 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=27000
                elif(dl=="Low"):
                    f=600
                    print("\n\t\t\tyour rent amount is 3000\nfine amount is 600\n\t\t\tbalance 26,400 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=26400
                elif(dl=="Medium"):
                    f=1500
                    print("\n\t\t\tyour rent amount is 3000 \n\t\t\tFine is 1500\n\t\t\tbalance 25,500 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=25500
                elif(dl=="High"):
                    f=2250
                    print("\n\t\t\tyour rent amount is 3000\n\t\t\tFine is 2250\n\t\t\t balance 24,750 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=24750
                d={"user id":id,"bike name":bk,"borrow date":i["Borrow date"],"return date":t4,"Fine":f,"status":"Paid","vehicle return":"yes"}
            else:
                if(dl=="None"):
                    f=1000
                    print("\n\t\t\tyour rent amount is 3000\n\t\t\tFine is 1000\nbalance 26,000 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=26000
                elif(dl=="Low"):
                    f=1600
                    print("\n\t\t\tyour rent amount is 3000\n\t\t\tfine amount is 1600\n\t\t\tbalance 25,400 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=25400
                elif(dl=="Medium"):
                    f=2500
                    print("\n\t\t\tyour rent amount is 3000 \n\t\t\tFine is 2500\n\t\t\tbalance 24,500 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=24500
                elif(dl=="High"):
                    f=3250
                    print("\n\t\t\tyour rent amount is 3000\n\t\t\tFine is 3250\n\t\t\tbalance 23,750 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=23750
                d={"user id":id,"bike name":bk,"borrow date":i["Borrow date"],"return date":t4,"Fine":f,"status":"Paid","vehicle return":"yes"}
            fne.append(d)
            borrow.remove(i)
    for i in borrowcar:
        if(bk==i["car name"] and np==i["number plate"] and id==i["user id"]):
            kms=int(input("Enter kms    :"))
            if(kms<=500):
                if(dl=="None"):
                    f=0
                    print("\n\t\t\tyour rent amount is 10000 balance 20,000 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=20000
                elif(dl=="Low"):
                    f=2000
                    print("\n\t\t\tyour rent amount is 10000\n\t\t\tfine amount is 2000\n\t\t\tbalance 18,000 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=18000
                elif(dl=="Medium"):
                    f=5000
                    print("\n\t\t\tyour rent amount is 10000 \n\t\t\tFine is 5000\n\t\t\tbalance 15,000 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=15000
                elif(dl=="High"):
                    f=7500
                    print("\n\t\t\tyour rent amount is 10000\n\t\t\tFine is 7500\n\t\t\tbalance 12500 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=24750
                d={"user id":id,"car name":bk,"borrow date":i["Borrow date"],"return date":t4,"Fine":f,"status":"Paid","vehicle return":"yes"}
            else:
                if(dl=="None"):
                    f=1000
                    print("\n\t\t\tyour rent amount is 10000\nFine is 1000\nbalance 19,000 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=19000
                elif(dl=="Low"):
                    f=3000
                    print("\n\t\t\tyour rent amount is 10000\n\t\t\tfine amount is 3000\n\t\t\tbalance 17,000 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=17000
                elif(dl=="Medium"):
                    f=6000
                    print("\n\t\t\tyour rent amount is 10000 \n\t\t\tFine is 6000\n\t\t\tbalance 14000 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=14000
                elif(dl=="High"):
                    f=8500
                    print("\n\t\t\tyour rent amount is 10000\n\t\t\tFine is 8500\n\t\t\tbalance 11500 is refunded to your account")
                    for j in usr:
                        if(id==j["user id"]):
                            j["wallet"]+=11500
                d={"user id":id,"car name":bk,"borrow date":i["Borrow date"],"return date":t4,"Fine":f,"status":"Paid","vehicle return":"yes"}
            borrowcar.remove(i)
            fne.append(d)
def returnvehicle(id):
    bk=input("\n\nEnter Vehicle name                       :")
    np=input("Enter Number plate                       :")
    sp=input("Enter specification                      :")
    dl=input("Enter damage label(Low/High/Medium/None) :")
    finelist(bk,np,id,dl)
    for i in borrow:
        if(bk==i["bike name"] and np==i["number plate"] and id==i["user id"] and i["specification"]==sp):
            borrow.remove(i)
            break
    input("\t\t\tPress any key to continue")
def fine():
    print("\t\t\tFINE LIST OR RETURN LIST")
    for i in fne:
        print("\n")
        for j in i:
            print(j,":",i[j])
    input("\t\t\tPress any key to continue")
def adminreport():
    while(True):
        os.system('cls')
        m=int(input("1.Borrow list\n2.Return list or fine list\n3.Exit\n\nEnter choice   :"))
        if(m==1):
            os.system('cls')
            print("\t\t\tBORROW LIST")
            for i in borrow:
                print("\n")
                for j in i:
                    print(j,":",i[j])
            for i in borrowcar:
                print("\n")
                for j in i:
                    print(j,":",i[j])
            input("\t\t\tPress any key to continue")
        elif(m==2):
            os.system('cls')
            fine()
        else:
            break
def report(id):
    while(True):
        os.system('cls')
        m=int(input("1.Borrow list\n2.Return list\n3.Exit\n\nEnter choice   :"))
        if(m==1):
            os.system('cls')
            print("\t\t\tBORROW LIST")
            for i in borrow:
                if(i["user id"]==id):
                    print("\n")
                    for j in i:
                        print(j,":",i[j])
            for i in borrowcar:
                if(i["user id"]==id):
                    print("\n")
                    for j in i:
                        print(j,":",i[j])
            input("\t\t\tPress any key to continue")
        elif(m==2):
            os.system('cls')
            print("\t\t\tFINE LIST OR RETURN LIST")
            for i in fne:
                if(i["user id"]==id):
                    print("\n")
                    for j in i:
                        print(j,":",i[j])
            input("\t\t\tPress any key to continue")
        else:
            break
def removecart(id):
    vn=input("\n\nEnter vehicle name    :")
    sp=input("Enter specification   :")
    for i in cart:
        if(i["user id"]==id and i["name"]==vn and i["specification"]==sp):
            cart.remove(i)
    input("\t\t\tRemoved\n\t\t\tPress any key")
def admin():
    s=input("\nEnter ID       :")
    p=int(input("Enter password :"))
    for i in ad:
        if(s==i["admin id"] and p==i["password"]):
            while(True):
                os.system('cls')
                print("\t\t\tWelcome",i["name"],"\n1.View vehicle\n2.Add vehicle\n3.Remove vehicle\n4.Modify vehicle details\n5.Search\n6.Report\n7.Exit")
                ch=int(input("\nEnter choice    :"))
                if(ch==1):
                    viewvehicle()
                elif(ch==2):
                    addvehicle()
                elif(ch==3):
                    removevehicle()
                elif(ch==4):
                    modifyvehicle()
                elif(ch==5):
                    search()
                elif(ch==6):
                    adminreport()
                else:
                    break
def user():
    os.system('cls')
    while(True):
        os.system('cls')
        print("\t\t\tUser\n1.New user\n2.Existing user\n3.Exit")
        ch=int(input("\nEnter choice:"))
        if(ch==1):
            s=input("\nEnter name             :")
            p=int(input("Enter password         :"))
            k=int(input("\n\t\t\tPay Rs.30000 to create an account\n1.Yes\n2.No"))
            if(k==1):
                l=len(usr)
                id="u"+str(l+1)
                d={"name":s,"password":p,"user id":id,"wallet":30000}
                usr.append(d)
                print("\n\t\t\tAccount created....\n\t\t\tyour user id is",id)
                input("Press any key to continue...")
        elif(ch==2):
            id=input("\nEnter user id  :")
            p=int(input("Enter password :"))
            for i in usr:
                if(id==i["user id"]):
                    w=i["wallet"]
                    while(True):
                        os.system('cls')
                        print("\t\t\tWelcome",i["name"],"\n1.View vehicle\n2.view and update wallet\n3.Search\n4.View cart\n5.remove from cart\n6.borrow vehicle\n7.Return vehicle\n8.Report\n9.Exit")
                        p=int(input("\n\nEnter choice   :"))
                        if(p==1):
                            seevehicle()
                        elif(p==2):
                            viewupdatewallet(id)
                        elif(p==3):
                            searchandcart(id)
                        elif(p==4):
                            viewcart(id)
                        elif(p==5):
                            removecart(id)
                        elif(p==6):
                            borrowvehicle(id)
                        elif(p==7):
                            returnvehicle(id)
                        elif(p==8):
                            report(id)
                        elif(p==9):
                            break
                        else:
                            print("Invalid input")
        elif(ch==3):
            break
        else:
            print("\n\t\t\tInvalid Input")
while(True):
    os.system('cls')
    print("\t\t\tVEHICLE RENTAL SYSTEM\n1.Admin\n2.user\n3.Exit")
    n=int(input("\nEnter choice :"))
    if(n==1):
        admin()
        continue
    elif(n==2):
        user()
        continue
    elif(n==3):
        print("\t\tThank you!!")
        break
    else:
        print("\t\t\tInvalid Input")
        continue