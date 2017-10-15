class AccountInfo():
    users = {100 : 0, 101: 0,102: 0, 103: 0, 104: 0, 105: 0}
    total = 0
    rec = []
    def __init__(self):
        global total
        global users
        global rec
    def depositamount(self, deposit):
        if userac in user.users:
            depostam = int(input("Deposit Amount:\n"))
            self.rec.append("%d deposited: %d"%(userac,depostam))
            self.users[userac]+=depostam
            self.total+=depostam
            print(userac, "SUCCESSFUL DEPOSITED........................",depostam)
        else:
            print("NO ACCOUNT FOUND")
    def withdrawamount(self, deposit):
        if userac in user.users:
            if self.users[userac]<=0:
                print("YOUR BALANCE IS 0")
            else:
                witdrawam = int(input("Withdraw Amount:\n"))
                self.rec.append("%d withdrawn: %d"%(userac,witdrawam))
                self.users[userac]=int(self.users[userac]-witdrawam)
                print(self.users[userac])
                print(userac, "SUCCESSFUL WITHDRAWN........................",witdrawam)
        else:
            print("NO ACCOUNT FOUND")
    def balancefn(self, balance):
        if userac in user.users or userac in operators:
            print(10*"*",userac,"CURRENT BALANCE",10*"*",)
            print(14*"*",self.users[userac],14*"*")
        else:
            print("NO ACCOUNT FOUND")

    def totalincomefn(self):
            print(10*"*","TOTAL RECORDS",10*"*",)
            print(14*"*",self.total,14*"*",)
    def alltrans(self, balance):
            for i in range(0, len(self.rec)):
                print("Transaction :",i+1," = ", self.rec[i])

operators = ['Lamin','Krissie','Admin']
teller = tuple(operators)
if input("ENTER OPERATOR'S ID:\n") in operators:
    while True:
        if input("CONTINUE SERVICE? - YES = Y | NO = N:\n")!='n':
            total = 0
            services = {1: 'Deposit', 2: 'Withdraw',3: 'Acc Statement', 4: 'All Records'}
            for keys,value in services.items():
                print(keys, value)
            sel = int(input("...............\nSelect Service:\n"))
            if sel in services:
                    choice = services[sel]
                    if sel == 1:
                        user = AccountInfo()
                        userac = int(input("User Account\n"))
                        user.depositamount(userac)
                    if sel == 2:
                        user = AccountInfo()
                        userac = int(input("User Account\n"))
                        user.withdrawamount(userac)
                    if sel == 3:
                        sel = str(input("FROM A CUSTOMER'S ACC - YES = Y | ALL - NO:\n")).lower()
                        if sel == 'y':
                            user = AccountInfo()
                            userac = int(input("User Account\n"))
                            user.balancefn(userac)
                        if sel == 'n':
                            user = AccountInfo()
                            tellerid = input("Enter Operator ID\n")
                            if tellerid in teller:
                                print("WELCOME", tellerid.upper())
                                user.totalincomefn()
                            else:
                                print("NO OPERATOR ID FOUND")
                    if sel == 4:
                        sel = str(input("PRINT ALL TRANSACTIONS - YES = Y | ALL - NO:\n")).lower()
                        if sel == 'y':
                            user = AccountInfo()
                            userac = input("Operator ID\n")
                            user.alltrans(userac)
                        if sel == 'n':
                            user = AccountInfo()
                            tellerid = input("Enter Operator ID\n")

            else:
                print("NO SERVICE")
        else:
            break
else:
    print("NO OPERATOR FOUND")

