#programmed by Era Fazliu

class bank_account():

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        self.signIn = False

    def logIn(self, InputPin):
        if InputPin=="123456":
            self.signIn = True
            print("Login sucessfull.")
            return True
        else:
            print("Invalid pin.")    
            return False
    
    def Balance(self):
        if self.signIn:
            print("Balance: ",self.balance)
        else:
            print("LogIn to see the balance.")

    def deposit(self, amount):
        if self.signIn:
            self.balance += amount
            print("The deposit was sucessfull")
        else:
            print("LogIn to deposit.")

    def withdraw(self, amount):
        if self.signIn:
            if amount <= self.balance:
                self.balance -= amount
                print("Sucessfull withdraw.")
            else:
                print("Insuficient funds, withdraw failed!")
        else:
            print("LogIn to withdraw") 

ATM = bank_account("Era",1500)

#before Sucessful Login - ask only for PIN
NotLoged=True
while NotLoged:
    InputPin= str(input("Enter the pin number:"))
    if ATM.logIn(InputPin) ==True:
        NotLoged=False


Command=-1
while Command!=0:
    print("0-exit, 1-balance, 2-deposit 3-withdraw")
    Command=int(input("Enter your command (0,1,2 or 3):"))
    if Command==1:
        ATM.Balance()
    elif Command==2:
        Amount=int(input("Enter Deposit Amount:"))
        ATM.deposit(Amount)
    elif Command==3:
        Amount=int(input("Enter Withdrawal Amount:"))
        ATM.withdraw(Amount)

