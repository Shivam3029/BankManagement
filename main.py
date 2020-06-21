def addAccount():
    name = input("Enter the account holder name : ")
    deposit = int(input("Enter The Initial amount : "))
    f=open("accounts.txt",'r')
    num_lines=1
    for lines in f:
        lines=lines.strip("\n")
        num_lines=num_lines+1
    
    # print(nl)

    new_file=open("A"+str(num_lines)+".txt","x")
    new_file=open("A"+str(num_lines)+".txt","a")
    new_file.write("0"+":"+"C"+":"+str(deposit)+":"+str(deposit)+"\n")
    new_file.close()

    f = open("accounts.txt", "a")
    

    f.write(str(name)+" "+str(deposit)+" "+str(num_lines)+" "+"\n")

    f.close()

    f = open("accounts.txt", "r")

    print(f.read())

def transaction():
    accNo=input("Enter your account number : ")

    f=open("accounts.txt",'r')
    # new_file_content = ""
    new_file_content = ""
    for line in f.readlines():
        #print(type(line))
        # stripped_line = line.strip()
        # print(line)
        lastchar=line.strip()[-1]
        # print(lastchar)
        s=line.split()
        # print(s)
        # bb=s[1]
        # print(bb)

        if(lastchar==accNo):
            ch=""
            while(ch!=3):
                # stripped_line = line.strip()
                # print(s[1])
                # bb=s[1]

                print("\t1. DEPOSIT")
                print("\t2. WITHDRAW")
                print("\t3. QUIT")

                ch=input("Enter your choice : ")
                if ch == '1':
                    # print(line)
                    fin=open("accounts.txt",'r')
                    data=fin.read()
    


                    amount=int(input("Enter the amount :"))
                    bb=s[1]
                    print(bb)
                    print(type(bb))
                    s[1]=int(s[1])+amount           
                    new_line = line.replace(str(bb), str(s[1]))
                    print(new_line)
                    line=new_line
                    data = data.replace(str(bb), str(s[1]))
                    fin.close()
                    fin = open("accounts.txt", "w")
                    fin.write(data)
                    #close the file
                    fin.close()
                    new_file=open("A"+str(accNo)+".txt","r")
                    for ln in new_file:
                        bal=ln.split(':')
                        print(bal[3].rstrip("\n"))

                    new_file=open("A"+str(accNo)+".txt","a")
                    new_file.write(bal[3].rstrip("\n")+":"+"C"+":"+str(amount)+":"+str(s[1])+":"+"\n")
                    new_file.close()
        
                    # new_file_content += new_line +"\n"
                    print(s[1])
                    print("Make deposit")
                    # f.close()
                    # writing_file = open("accounts.txt", "w")
                    # writing_file.write(new_file_content)
                    # writing_file.close()
                elif ch =='2':
                    fin=open("accounts.txt",'r')
                    data=fin.read()
    


                    amount=int(input("Enter the amount :"))
                    bb=s[1]
                    print(bb)
                    print(type(bb))
                    s[1]=int(s[1])-amount           
                    new_line = line.replace(str(bb), str(s[1]))
                    print(new_line)
                    line=new_line
                    data = data.replace(str(bb), str(s[1]))
                    fin.close()
                    fin = open("accounts.txt", "w")
                    fin.write(data)
                    #close the file
                    fin.close()
                    new_file=open("A"+str(accNo)+".txt","r")
                    for ln in new_file:
                        bal=ln.split(':')
                        print(bal[3].rstrip("\n"))

                    new_file=open("A"+str(accNo)+".txt","a")
                    new_file.write(bal[3].rstrip("\n")+":"+"D"+":"+str(amount)+":"+str(s[1])+":"+"\n")
                    new_file.close()
        
                    # new_file_content += new_line +"\n"
                    print(s[1])
                    print("Make Withdraw")
                elif ch == '3':
                    print("Thank you for using the software")
                    break
                else:
                    print("Invalid Choice")
    print("Invalid acc no")


choice=""
num=0

while choice!=3:
    print("\tMAIN MENU")
    print("\t1. ADD A NEW ACCOUNT")
    print("\t2. TRANSACTION")
    print("\t3. QUIT")

    choice=input("Enter your choice : ")
    if choice == '1':
        addAccount()
    elif choice =='2':
        transaction()
    elif choice == '3':
        print("Quit")
        break
    else:
        print("Invalid Choice")