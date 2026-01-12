class SwissBank:
    minbalance = 50000
    ifsccode = "SWISS000999" 

    def __init__(self, accno, name, mobno, adharno, balance, pin):
        self.accno = accno  
        self.name = name
        self.mobno = mobno
        self.adharno = adharno
        self.balance = balance 
        self.pin = pin

    def details(self):
        print(f"Bank IFSC: {SwissBank.ifsccode}") 
        print(f"Account No: {self.accno}")
        print(f"Name: {self.name}")
        print(f"Mobile Number: {self.mobno}")
        print(f"Adhar Number: {self.adharno}")
        print(f"Balance: {self.balance}")
        print("-" * 20)
    def withdraw(self):
        count = 3
        while count > 0:
            print(f"Attempts remaining: {count}")
            try:
                pin = int(input("Enter your 4 digit pin: "))
                if pin == self.pin:
                    amount = int(input("Enter the amount to withdraw: "))
                    
                    if amount > self.balance:
                        print('Insufficient balance')
                    elif 100 <= amount <= 50000:
                        if amount % 100 == 0:
                            self.balance -= amount
                            print("Amount debited successfully... Collect your cash.")
                            print(f"Remaining Balance: {self.balance}")
                        else:
                            print("Invalid Amount! Amount must be in multiples of 100.")
                    else:
                        print("Invalid limit (Min 100, Max 50000)")
                    break # Exit loop on success or limit fail
                else:
                    print("Incorrect PIN.")
                    count -= 1
            except ValueError:
                print("Please enter numbers only.")
        else:
            print("No attempts left. Try again after 10 minutes.")

    def deposite(self):
        count = 3
        while count > 0: 
            print(f"Attempts remaining: {count}")
            try:
                pin = int(input("Enter your 4 digit pin: "))
                if pin == self.pin:
                    amount = int(input("Enter the amount to deposit: "))
                    
                    if 100 <= amount <= 50000:
                        if amount % 100 == 0:
                            self.balance += amount
                            print("Amount credited successfully.")
                            print(f"Available Balance : {self.balance}")
                        else:
                            print("Invalid Amount! Amount must be in multiples of 100.")
                    else:
                        print("Invalid limit.")
                    break
                else:
                    print("Incorrect PIN.")
                    count -= 1
            except ValueError:
                 print("Please enter numbers only.")
        else:
            print("No attempts left. Try again after 36 hours.")

    def check_balance(self):
        count = 3
        while count > 0:
            try:
                pin = int(input("Enter your 4 digit pin: "))
                if pin == self.pin:
                    print(f'Available balance is {self.balance}')
                    break
                else:
                    print("Incorrect PIN")
                    count -= 1
            except ValueError:
                print("Please enter numbers only.")
        else:
            print("No attempts left.")

    def pinchange(self):
        oldpin = int(input("Enter old pin: "))
        if self.pin == oldpin:
            newpin = int(input("Enter new pin: "))
            self.pin = newpin
            print("PIN changed successfully")
        else:
            print("Old PIN is not correct")

    def adharchange(self):
        oldadhar = int(input("Enter old adhar: "))
        if self.adharno == oldadhar:
            newadhar = int(input("Enter new adhar: "))
            self.adharno = newadhar
            print("Adhar changed successfully")
        else:
            print("Old Adhar is not correct")

    @classmethod 
    def modifiedetails(cls):
        cls.minbalance = 0

# --- DRIVER CODE ---

customer1 = SwissBank(30901234567891, "Vijay Malya", 8888888888, 1001001001234, 50000000, 8789) 
customer2 = SwissBank(45019876543210, "Ambani", 9999999999, 123456789013, 2999999, 1124)
customer3 = SwissBank(67125555666677, "Tata", 9876543212, 123456789014, 80000000, 9101)        
         
# Testing
customer1.deposite() 
