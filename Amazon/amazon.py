import os
os.system('cls')
ad=[{"name":"swe","pswd":310,"Id":1},{"name":"mythili","pswd":812,"Id":2}]
mar=[{"name":"thiru","pswd":274,"id":101},{"name":"hari","pswd":432,"id":102}]
usr=[{"name":"raji","pswd":807,"usr id":"u101","amnt":50000,"count":0},{"name":"raj","pswd":271,"usr id":"u102","amnt":60000,"count":0}]
products=[{"merchant":"thiru","id":101,"product name":"iphone","product id":"p101","prize":50000,"discount":10,"stock":5,"count":0},{"merchant":"hari","id":102,"product name":"smart watch","product id":"p102","prize":5000,"discount":20,"stock":15,"count":0},{"merchant":"hari","id":102,"product name":"iphone","product id":"p103","prize":60000,"discount":5,"stock":20,"count":0},{"merchant":"thiru","id":101,"product name":"laptop","product id":"p104","prize":65000,"discount":10,"stock":10,"count":0}]
nmd=[]
cart=[{"usr":"raji","usr id":"u101","merchant":"thiru","id":101,"product name":"iphone","product id":"p101","prize":50000,"discount":10},{"usr":"raj","usr id":"u102","merchant":"hari","id":102,"product name":"smart watch","product id":"p102","prize":5000,"discount":20}]
orders=[]
def newmerchant(nmd,status):
    os.system('cls')
    res1="Pending"
    if(status=="Access"):
        if(len(nmd)==0):
            print("\t\tNo request is received..........")
            input("press any key to continue...")
        else:
            for i in nmd:
                print("\n\t\t\tRequest:")
                for j in nmd:
                    print("\n")
                    for x in j:
                        print(x,":",j[x])
                print("\t\t\n1.Approve a merchant\n2.Reject a merchant\n3.Exit")
                q=int(input("Enter yes(1) or no(2):"))
                if(q==1):
                    res1="Approved"
                    l=len(mar)
                    i["id"]=l+101
                    mar.append(i)
                    nmd.remove(i)
                    print("\t\tAccount added....")
                    input("Press key to continue....")
                    continue
                elif(q==2):
                    nmd.remove(i)
                    res1="Disapproved"
                    print("\t\tAccount removed...")
                    input("Press key to continue....")
                    continue
                elif(q==3):
                    break
    else:
        return res1
def addmer():
    os.system('cls')
    print("\t\tAdmin->add merchant")
    q=int(input("No of merchants u have to add:"))
    for i in range(q):
        dic={}
        dic["name"]=input("\nEnter merchant name    :")
        dic["pswd"]=int(input("Enter merchant pswd      :"))
        dic["id"]=len(mar)+101
        print("\t\t\tID :",dic["id"])
        mar.append(dic)
def removemer():
    os.system('cls')
    print("\t\tAdmin->remove merchant")
    q=int(input("No of merchants u have to remove:"))
    for i in range(q):
        dic={}
        dic["name"]=input("Enter merchant name    :")
        dic["id"]=int(input("Enter merchant's id    :"))
        for i in mar:
            if(dic["name"]==i["name"] and dic["id"]==i["id"]):
                mar.remove(i)
def addproduct(s,p):
    os.system('cls')
    print("\t\tMerchant->add products...")
    id=int(input("Enter ur id"))
    m=int(input("Enter no of products u have to add:"))
    for j in range(m):
        d={}
        l=len(products)
        for i in mar:
            if(i["name"]==s and i["pswd"]==p and i["id"]==id):
                d["merchant"]=s
                d["id"]=id
                d["product name"]=input("\nEnter ur product name:")
                d["product id"]="p"+str(l+101)
                d["prize"]=int(input("Enter prize:"))
                d["discount"]=int(input("Enter discount:"))
                d["stock"]=int(input("Enter stock:"))
                d["count"]=0
                products.append(d)
                print("\t\tproduct added succcessfully")
                break
def removeproduct(s,id):
    os.system('cls')
    for i in products:
        print("\n")
        if(i["merchant"]==s and i["id"]==id):
            for j in i:
                print(j,":",i[j])
    print("\n")
    n=int(input("Enter bo of products:"))
    for j in range(n):
        pr_id=input("Enter product id:")
        for i in products:
            if(pr_id==i["product id"]):
                products.remove(i)
                break
def stockcheck(s,id):
    os.system('cls')
    j=0
    for i in products:
        j+=1
        if(i["merchant"]==s and i["id"]==id):
            print("\n\nproduct",j,":\nmerchant name:",i["merchant"],"\nproduct name:",i["product name"],"\nproduct id:",i["product id"],"\nPrize:",i["prize"],"\ndiscount:",i["discount"],"\nstock:",i["stock"])
def compare():
    os.system('cls')
    print("\t\tMerchant->compare")
    while(True):
        os.system('cls')
        print("1.product based compare\n2.merchant based compare\n3.Exit")
        k=int(input("Enter choice:"))
        if(k==1):
            os.system('cls')
            prt=input("Enter product name:")
            j=0
            for i in products:
                if(prt==i["product name"]):
                    j+=1
                    print("\n\nproduct",j,"\nmerchant name:",i["merchant"],"\nproduct name:",i["product name"],"\nPrize:",i["prize"],"\ndiscount:",i["discount"])
            input("\t\tPress any to continue...")        
            continue
        if(k==2):
            os.system('cls')
            mn=input("Enter merchant name:")
            id=int(input("Enter merchant's id"))
            j=0
            for i in products:
                if(mn==i["merchant"] and id==i["id"]):
                    j+=1
                    print("\n\nproduct",j,"\nmerchant name:",i["merchant"],"\nproduct name:",i["product name"],"\nPrize:",i["prize"],"\ndiscount:",i["discount"])
            input("\t\tPress any to continue...")  
            continue
        else:
            break
def edit(s,id):
    os.system('cls')
    h=int(input("Enter no of products u want to edit:"))
    for j in range(1,h+1):
        prt=input("Enter product "+str(j)+" name:")
        for i in products:
            if(i["merchant"]==s and i["id"]==id and i["product name"]==prt):
                i["prize"]=int(input("edit  prize:"))
                i["discount"]=int(input("Edit discount:"))
def search(s,id):
    l=[]
    os.system('cls')
    prt=input("Enter product name u want to search:")
    for i in products:
        if(prt==i["product name"]):
            for j in i:
                print(j,":",i[j])
        l.append(i)
    while(True):
        print("\n1.Add to cart\n2.Exit")
        print("\n")
        ch=int(input("choice:"))
        if(ch==1):
            print("\n")
            prt_id=input("Enter product id:")
            for i in l:
                if(i["product id"]==prt_id):
                    i["usr"]=s
                    i["usr id"]=id
                    cart.append(i)
                    print("\t\t\tAdded sucessfully...")
            continue
        else:
            break
def showcart(s,id):
    os.system('cls')
    print("\t\t\tWelcome",s)
    for i in cart:
        if(i["usr"]==s and i["usr id"]==id):
            print("\n")
            for j in i:
                print(j,":",i[j])
def neworder(s,id):
    print("\n")
    pr=input("enter product id:")
    st=int(input("Enter no of products:"))
    ad=False
    for i in products:
        if(i["product id"]==pr and st<=i["stock"]):
            j=i
            j["user name"]=s
            j["user id"]=id
            w=int(i["prize"])
            d=i["discount"]
            w1=w*(d/100)
            w2=w-w1
            ad=True
            break
    else:
        print("not enough stock")
    if(ad):
        for i in usr:
            if(i["name"]==s and int(i["amnt"])>=w2):
                i["amnt"]=int(i["amnt"])-w2
                i["count"]=int(i["count"])+1
                print("\t\t\torder placed.....")
                st=True
                break
        else:
            print("\t\t\tWallet amnt is not enough....")
    if(st):
        j["review"]=""
        orders.append(j)
        for i in products:
            if(pr==i["product id"]):
                i['count']+=1
                i["stock"]-=1                  
                break
def order(s,id):
    os.system('cls')
    while(True):
        os.system('cls')
        print("\n1.order from cart\n2.order by search\n3.exit")
        print("\n")
        ch=int(input("choice:"))
        if(ch==1):
            showcart(s,id)
            neworder(s,id)
            input("\t\t\tPress any key to continue..")
            continue
        elif(ch==2):
            print("\n")
            pr=input("enter product name:")
            for i in products:
                print("\n")
                if(pr==i["product name"]):
                    for j in i:
                        print(j,":",i[j])
            neworder(s,id)
            input("\t\t\tPress any key to continue..")
            continue
        elif(ch==3):
            break
def ordercheck(s,id):
    j=0
    for i in orders:
        if(i["merchant"]==s and i["id"]==id):
            j+=1
            print("\n\nproduct",j,"\nproduct name:",i["product name"],"\nproduct id:",i["product id"],"\nprize:",i["prize"],"\ndiscount:",i["discount"])
def porders():
    for i in orders:
        print("\n")
        for j in i:
            print(j,":",i[j])
    input("\t\t\tEnter any key to continue....")
def frequentcustomer():
    os.system('cls')
    mx=0
    for i in usr:
        if(i["count"]>mx):
            mx=i["count"]
            j=i
    print(j)
def frequentproduct():
    os.system('cls')
    mx=0
    for i in products:
        if(i["count"]>mx):
            mx=i["count"]
            j=i
    print(j)
def adminpage():
    os.system('cls')
    print("\tAdmin!!!")
    s=input("Enter User name:")
    p=int(input("enter pswd:"))
    for i in ad:
        if(s==i["name"] and p==i["pswd"]):
            while(True):
                os.system('cls')
                print("\t\tAdmin!!!\n1.add\n2.remove\n3.approve\n4.show\n5.exit")
                k=int(input("Enter choice:"))
                if(k==1):
                    addmer()
                    input("\tAccount added successfully.....\n\tPress any key to continue.......")
                    continue
                elif(k==2):
                    removemer()
                    input("\tAccount removed.....\n\tPress any key to continue.......")
                    continue
                elif(k==3):
                    newmerchant(nmd,"Access")
                    print("\t\tPress any key to continue....")
                    continue
                elif(k==4):
                    os.system('cls')
                    for j in mar:
                        print("\n")
                        for x in j:
                            print(x,":",j[x])
                    input("Press any to continue...")
                    continue
                elif(k==5):
                    break
                continue
def merchant():
    os.system('cls')
    while(True):
        os.system('cls')
        print("\tMerchant!!!!\n1.New merchant\n2.Existing merchant\n3.Exit")
        m=int(input("Enter choice:"))
        if(m==1):
            os.system('cls')
            d={}
            print("\tNew merchant!!")
            s1=input("Enter ur name :")
            p1=int(input("Enter pswd    :"))
            f=False
            for i in mar:
                if(i["name"]==s1 or i["pswd"]==p1):
                    f=True
            if(f==False):
                d["name"]=s1
                d["pswd"]=p1
                nmd.append(d)
                ch=newmerchant(nmd,"Pending")
                if(ch=="Pending"):
                    print("\tRequest is sent....wait for some more time......")
                    input("Press any key to continue....")
                    break
            else:
                print("\tUser name or pswd is already exist.....\nplz enter any other user name or pswd......")
                input("\tpress any key to continue....")
                continue
        elif(m==2):
            os.system('cls')
            print("\t\tExisting merchant")
            s2=input("Enter ur name :")
            p2=int(input("Enter pswd    :"))
            f=False
            k=0
            while(True):
                for i in mar:
                    if(i["name"]==s2 and i["pswd"]==p2):
                        id=i["id"]
                        f=True
                        os.system('cls')
                        print("\t\tWelcome",s2,"\n1.Add a product\n2.Remove a product\n3.stock check\n4.compare\n5.edit\n6.sales report\n7.frequent customer\n8.frequent prouct\n9.Show product review \n9.Exit")
                        p=int(input("choice:"))
                        if(p==1):
                            addproduct(s2,p2)
                            input("\t\tPress any key to continue........")
                            continue
                        elif(p==2):
                            removeproduct(s2,id)
                            input("\t\tPress any key to continue........")
                            continue
                        elif(p==3):
                            stockcheck(s2,id)
                            input("\t\tPress any key to continue........")
                            continue
                        elif(p==4):
                            compare()
                            input("\t\tPress any key to continue........")
                            continue
                        elif(p==5):
                            edit(s2,id)
                            input("\t\tPress any key to continue........")
                            continue
                        elif(p==6):
                            ordercheck(s2,id)
                            input("\t\tPress any key to continue........")
                            continue
                        elif(p==7):
                            frequentcustomer()
                            input("\t\tPress ay key to continue.....")
                            continue
                        elif(p==8):
                            frequentproduct()
                            input("\t\tpress any to continue....")
                            continue
                        elif(p==9):
                            os.system('cls')
                            id=input("Enter product id:")
                            for i in orders:
                                if(i["product id"]==id):
                                    print("\n\n")
                                    print("user name:",i["user name"])
                                    print("review:",i["review"])
                            input("\t\tPress any key to continue......")
                        else:
                            k=1
                if(f==False):        
                    print("Doesnt have an account...")
                    input("Press any key to continue...")
                    continue
                if(k!=1):
                    continue
                else:
                    break
        elif(m==3):
            break
def user():
    os.system('cls')
    while(True):
        os.system('cls')
        print("\t\t\tcustomer!!!!\n1.New user\n2.Existing user\n3.Exit")
        print("\n")
        x=int(input("Enter choice:"))
        if(x==1):
            os.system('cls')
            d1={}
            print("\t\t\tNew customer!!")
            print("\n")
            s1=input("Enter ur name:")
            p1=int(input("Enter pswd"))
            f=False
            for i in usr:
                if(i["name"]==s1 and i["pswd"]==p1):
                    f=True
                    break
            if(f==False):
                l=len(usr)
                d1["name"]=s1 
                d1["pswd"]=p1
                d1["usr id"]="u"+str(l+101)
                d1["amt"]=int(input("Enter ur initial wallet amount"))
                d1["count"]=0
                usr.append(d1)
                input("\t\t\tEnter any key to continue....")
                continue
            else:
                print("\tUser name or pswd is already exist.....\nplz enter any other user name or pswd......")
                input("\tpress any key to continue....")
                continue
        elif(x==2):
            os.system('cls')
            print("\t\t\tEXISTING CUSTOMER!!!!!")
            s1=input("Enter ur id:")
            p1=int(input("Enter pswd:"))
            for i in usr:
                if(i["usr id"]==s1 and i["pswd"]==p1):
                    id=i["usr id"]
                    s=i["name"]
                    while(True):
                        os.system('cls')
                        print("\t\tWelcome",s,"!!!\n1.Show available products\n2.Search\n3.order\n4.perivious orders\n5.show cart\n6.Check wallet\n7.wallet amount update\n8.Add review\n9.exit")
                        print("\n")
                        q=int(input("Enter choice:"))
                        if(q==1):
                            for i in products:
                                print("\n")
                                for j in i:
                                    print(j,":",i[j])
                            input("\t\t\tperss any key to continue...")
                        elif(q==2):
                            search(s,id)
                            continue
                        elif(q==3):
                            order(s,id)
                            continue
                        elif(q==4):
                            porders()
                            continue
                        elif(q==5):
                            showcart(s,id)
                            input("\t\t\tPress any key to continue..")
                            continue
                        elif(q==6):
                            os.system('cls')
                            print("Welcome",s)
                            print("wallet amount:",i["amnt"])
                            input("\t\t\tPress any key to continue..")
                            continue
                        elif(q==7):
                            os.system('cls')
                            i["amnt"]+=int(input("enter wallet amount:"))
                            input("\t\t\tWallet amount updated!!!\n\t\tPress any key to contniue....")
                            continue
                        elif(q==8):
                            os.system('cls')
                            print("\t\t\tOrdered Products")
                            for i in orders:
                                if(i["user name"]==s and i["user id"]==id):
                                    print("\n")
                                    for j in i:
                                        print(j,":",i[j])
                            print("\n")
                            m=int(input("Enter no of products:"))
                            for i in range(m):
                                print("\n")
                                sw=input("Enter product id:")
                                for j in orders:
                                    if(j["product id"]==sw):
                                        j["review"]=input("Enter review:")
                            print("\n")
                            input("\t\t\tPress any key to continue...")
                            continue
                        else:
                            break
        elif(x==3):
            break
while(True):
    os.system('cls')
    print("\t\t\tAMAZON!!!!\n1.Admin\n2.Merchant\n3.User\n4.exit")
    n=int(input("Choice:"))
    if(n==1):
        adminpage()
        print("\t\t\tPress any to continue....")
        continue
    elif(n==2):
        merchant()
        print("\t\t\tPress any to continue....")
        continue
    elif(n==3):
        user()
        print("\t\t\tPress any to continue....")
    elif(n==4):
        os.system('cls')
        print("\t\t\tTank you for using amazon.....\n\tHave a Happy day:)")
        break
    else:
        print("Ivalid Input")
        print("\t\t\tPress any to continue....")
        continue
