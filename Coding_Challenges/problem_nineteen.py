
# ATM class
class Bank:
    
    balance = 0.0
    
    # interact method declaration
    def interact (self):
        
    # Operations array
        self.operations = ["Withdraw", "Deposit", "Current Balance", "Exit"]
    
       # you can access your account info such as your personnal info, balnce and make some operations such as withdrawing, make deposit and much more")
        self.resp = input("Do want to continue? (Y/N): ")
        
        if self.resp == "Y" or self.resp == "y":
            for n in range(0, len(self.operations)):
                print(n + 1, ".", self.operations[n])
            #select options or operations 

            self.option = int(input("Select an operation from the list: "))
            if self.option == 1:
                self.withdraw()
            elif self.option == 2:
                self.deposit()
            elif self.option == 3:
                self.current_balance()
            else:
                self.Exit()
        else:
            #if the operation is not matched, then exit the program
            self.Exit()

    # function withdrawing 
    def withdraw (self):
        if self.balance < 0:
            print("Sorry your account balance is zero.")
            self.result = input("Do you Want to deposit? (Y/N)")
                
            if self.result == "Y" or self.result == "y":
                self.deposit()
            else:
                self.Exit()
                    
        else:
            self.withdrawAmount = float(input("Enter amount you want to withdraw (RWF): "))
            if self.withdrawAmount < self.balance:
                self.balance = self.balance - self.withdrawAmount
            else:
                print("oohhh your account has insuficient funds!")
                self.result = input("Do you want to deposit? (Y/N)")
                
                if self.result == "Y" or self.result == "y":
                    self.deposit()
                else:
                    self.Exit()
         
    def deposit (self):
        self.depositAmount = float(input("Enter amount you want to deposit to your account (RWF): "))
        if self.depositAmount <= 0:
            print("You can't deposit negative or zero amount")
            self.Exit()
        else:
            self.balance = self.balance + self.depositAmount
            print("account balance is: ", self.balance, "RWF")
    
    def current_balance (self):
        print("Your account balance is: ", self.balance, "RWF")
            
    def Exit (self):
        print("Thank you for banking with us!")
        exit()
    
terminal = Bank()
terminal.interact()