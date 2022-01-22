import os
os.system('cls')
ad=[{"name":"swe","pswd":310}]
usr=[{"name":"mythili","pswd":812,"id":"u1"}]
trains=[]
wl=[]
def declarestations(tn,stop):
    print("\t\tstation declaration....")
    l=[]
    for i in range(stop):
        l.append(input("Enter station "+str(i+1)+": "))
    for i in trains:
        if(i["train name"]==tn):
            i["stations"]=l
def viewtrains():
    os.system('cls')
    for i in trains:
        print("\ntrain name:",i["train name"],"\ntime:",i['time'],"\nseat availability:")
        for j in i["seat availability"]:
            print(j)
        j=0
        print("\n\nStations")
        for x in i["stations"]:
            j+=1
            print("station",j,x)
        print("--------------------------------------------------------------------------------------------------------------------------------------")
def bookticket(s,id):
    os.system('cls')
    print("\t\tWelcome",s,"!!!")
    for i in usr:
        if(i["id"]==id):
            tr=input("Plz enter train name:")
            se=int(input("Plz enter no of seats:"))
    temp=0
    for i in trains:
        if(tr==i["train name"]):
            for x in range(1,se+1):
                ls=i["seat availability"]
                mx=0
                for pas in range(len(ls)):
                    for pas1 in range(len(ls[pas])):
                        if(ls[pas][pas1]>mx):
                            mx=ls[pas][pas1]
                mx+=1
                ml=mx
                bp=input("Enter boding point:")
                dp=input("Enter Departure point:")
                bp_ind=0
                dp_ind=0
                for j in i["stations"]:
                    if(j==bp):
                        bp_ind=(i["stations"].index(j))+1
                    elif(j==dp):
                        dp_ind=(i["stations"].index(j))+1
                for j in range(i["seat"]):
                    if(sum(i["seat availability"][j][bp_ind-1:dp_ind-1])==0):
                        print("Seat allocated",j)
                        for k in range(bp_ind-1,dp_ind):
                            i["seat availability"][j][k]=mx
                        for k in i["seat availability"]:
                            print(k)
                        print("ur id is",mx)
                        print("\n")
                        break
                else:
                    ml+=temp
                    temp+=1
                    l={"train name":tr,"usr id":id,"boding point":bp_ind,"depature point":dp_ind,"status":"pending","id":ml}
                    wl.append(l)
                    print("Seat not allocated......ur booking is added waiting list...")
                    print("\n")
def ticketcancel():
    os.system('cls')
    print("\t\tticket cancel page....")
    tr=input("Enter train name:")
    for i in trains:
        if(tr==i["train name"]):
            ls=i["seat availability"]
            n=int(input("Enter ur registration id:"))
            for j in range(i["seat"]):
                for k in range(i["stop"]):
                    if(i["seat availability"][j][k]==n):
                        i["seat availability"][j][k]=0
    print("\t\tTicket cancelled.....")
    if(len(wl)>0):
        for i in trains:
            if(i["train name"]==tr):
                seat1=i["seat"]
            break
        for i in wl:
            if(i["train name"]==tr and i["status"]=="pending"):
                print(tr)
                bp_ind=i["boding point"]
                dp_ind=i["depature point"]
                id=i["id"]
                for j in range(seat1):
                    if(sum(ls[j][bp_ind-1:dp_ind-1])==0):
                        for k in range(bp_ind-1,dp_ind):
                            ls[j][k]=id
                            i["status"]="Booking Confirm"
    else:
        pass
def admin():
    os.system('cls')
    print("\t\tAdmin page")
    s=input("Enter Nmae:")
    p=int(input("Enter pswd:"))
    for i in ad:
        if(s==i["name"] and p==i["pswd"]):
            while(True):
                os.system('cls')
                print("\t\tWlcome",s,"!!\n1.Add trains,Routes and Stations\n2.show trains\n3.Exit")
                ch=int(input("Enter choice:"))
                if(ch==1):
                    os.system('cls')
                    print("\t\tAdd trains,Routes and Stations")
                    n=int(input("No of trains u want to add:"))
                    for x in range(n):
                        d={}
                        l=len(trains)
                        print("\n\n")
                        d['bpdp']=input("enter boding point and depature point:")
                        d['train name']=input("Enter train name:")
                        tn=d['train name']
                        d['train id']="t"+str(int(l+1))
                        d["stop"]=int(input("Enter no of stops:"))
                        stop=d["stop"]
                        d['seat']=int(input("No of seats:"))
                        seat=d["seat"]
                        d['time']=input("enter time:")
                        d['seat availability']=[[0 for i in range(stop)] for j in range(seat)]
                        d['stations']=[]
                        trains.append(d)
                        declarestations(tn,stop)
                    input("Press any key to continue...")
                    continue
                elif(ch==2):
                    os.system('cls')
                    k=0
                    for i in trains:
                        k+=1
                        print("\ntrain:",k)
                        for j in i:
                            if(j=="seat availability:"):
                                print(j)
                                for x in i[j]:
                                    print(i[j][x])
                            elif(j=="stations"):
                                st=0
                                for x in i[j]:
                                    st+=1
                                    print("station",st,x)
                            else:
                                print(j,":",i[j])
                    input("Press any key to continue...")
                    continue
                else:
                    break
def user():
    os.system('cls')
    while(True):
        os.system('cls')
        print("\t\tUser!!\n1.new user\n2.Existing user\n3.Exit")
        ch=int(input("Enter choice:"))
        d={}
        if(ch==1):
            os.system('cls')
            s=input("Enter name:")
            p=int(input("Enter pswd :"))
            l=len(usr)
            d["name"]=s
            d["pswd"]=p
            d["id"]="u"+str(l+1)
            usr.append(d)
            print("\n\t\t\tAccount created....\n\t\t\tUr id is",d["id"])
            input("Press any key to continue...")
        elif(ch==2):
            os.system('cls')
            s=input("Enter name :")
            id=input("Enter id  :")
            p=int(input("Enter pswd :"))
            for i in usr:
                if(id==i["id"]):
                    while(True):
                        os.system('cls')
                        print("\t\tWelcome",s,"!!!\n1.view trains and availability\n2.book ticket\n3.ticket cancel\n4.waiting list\n5.exit")
                        choice=int(input("Enter choice:"))
                        if(choice==1):
                            viewtrains()
                            input("\t\tPress any key to continue")
                            continue
                        elif(choice==2):
                            bookticket(s,id)
                            input("\t\tPress any key to continue")
                            continue
                        elif(choice==3):
                            ticketcancel()
                            input("\t\tPress any key to continue")
                            continue
                        elif(choice==4):
                            os.system('cls')
                            tr=input("enter train name")
                            for i in wl:
                                if(i['train name']==tr):
                                    if(len(wl)>0):
                                        print("\n")
                                        for k in i:
                                            print(k,":",i[k])
                                    else:
                                        print("\t\tNo waiting list....")
                            input("\t\tpress any key to continue.....")
                        else:
                            break
        else:
            break
while(True):
    os.system('cls')
    print("\t\tRailway Booting\n1.Admin\n2.user\n3.Exit")
    n=int(input("Enter choice:"))
    if(n==1):
        admin()
        continue
    elif(n==2):
        user()
        input("\t\tPress any key to continue....")
        continue
    elif(n==3):
        print("\t\tThank you!!")
        break