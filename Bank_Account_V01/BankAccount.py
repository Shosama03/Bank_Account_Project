import os
from datetime import datetime

class BankAccount:
    account_number=2025101
    interest_rate=5.5 #This interest is not specific to a user but every user that has a Bank Account, hence Class attribute instead of instance attribute.
    
    def __init__(self, account_holder: str, account_pin : int, balance = 0):
        #This istantiates the account for any person with their name, account_number, account_pin and their balance.
        
        self.account_number=BankAccount.account_number # Saves the specific user's account number.
        BankAccount.account_number+=1 #Incrementing the account number so the account number stays contiguous.
        self.account_holder=account_holder # Saves the specific user's Name.
        self.__balance=balance             # Saves the specific user's account Balance.
        self.__account_pin=account_pin     # Saves the specific user's account Pin.
        self.__transactions=[]             # Saves the specific user's account's Transaction History.
    
    # Checkes the balance of the user.
    def check_balance(self,pin:int):
        #If the entered pin is valid, we display the balance.
        
        if pin == self.__account_pin:
            return(f"You currently have {self.__balance}Rs in your Bank Account.")
        
        #If the entered pin does not match the user's account pin, we simply say Invalid Pin.
        else:
            return("Invalid Pin!!!")
            
    # This is used for deposition of money into the specific user's account.       
    def deposit(self,amount:int):
        #Only deposit money if the amount is greater than 0.
        if amount>0:
            self.__balance += amount
            self.__transactions.append(f"{datetime.now().strftime('%d-%m-%y %H-%M-%S')} -  Deposited {amount} Rs.")
            return(f"You have successfully deposited {amount}Rs in your Bank Account, New balance: {self.__balance}")
            
        
        #If the entered amount is less than 0, basically negative, we say the entered amount is invalid.
        else:
            return(f"Invalid amount {amount} entered. ")
        
    # This is to withdraw the money from specific user's account.
    def withdraw(self,amount:int,pin :int):
        #Works only if the pin is correct.
        if pin == self.__account_pin:
            #user can only withdraw if the balance is greater than the amount entered.
                if self.__balance>=amount:
                    #Bank has a policy of keeping minimum 500Rs in the account, so Withdrawal is Rejected if the balances goes below 500Rs while withdrawing.
                    if self.__balance - amount <500:
                        return("Minimum 500Rs Balance is mandatory, Withdrawal Rejected!!!")
                        
                    # If the minimum balance remains above 500, user can easily withdraw.
                    else:
                        self.__balance-=amount
                        self.__transactions.append(f"{datetime.now().strftime('%d-%m-%y %H-%M-%S')} - Withdrew {amount}Rs.")
                        return(f"Withdrawed {amount}Rs successfully, New balance: {self.__balance}")
                        
        #If the entered pin is wrong, display Invalid Pin, withdrawal Rejected.
        else:
            return(f"{pin} is an invalid pin, Withdrawal Rejected!!!")
            
    
    # This is to change the old pin with the new pin incase the user forgot his/her account pin.
    def change_pin(self,old_pin:int,new_pin:int):
        if old_pin == self.__account_pin:
            if new_pin == old_pin:
                return("You cannot Enter the same pin as previous one.")
            #If the new pin is not the same as old pin, the pin is changed.
            self.__account_pin = new_pin
            return(f"You have successfully changed your Pin from {old_pin} to {new_pin}.")
        else:
            return "Invalid Pin, Pin Change Rejected."
            
    #Keeps a record of all the transactions done in the user's account.
    def transaction_history(self):
        if not self.__transactions:
            return("No transactions yet.")
        else:
            history = "Transaction History:\n"
            history+="\n".join([f"{number} - {transaction}" for number,transaction in enumerate(self.__transactions,1)])
            return history
        
                
    #Adds the interest on the balance kept in user's account.
    def add_interest(self):
        #Calculatin the interest first.
        interest=self.__balance*(BankAccount.interest_rate/100)
        self.__balance+=interest
        return (f"Interest of {interest:.2f}Rs. added, New balance is {self.__balance:.2f}Rs. ")
        
        
        
    #To check the interest rates, no need to pass an instance, so using @staticmethod decorator.
    @staticmethod
    def check_interest_rates():
        return f"The interest rates of our bank is {BankAccount.interest_rate}%"
    
    #Displays user's information like Name, Acc number, and balance
    def account_information(self):
        return f"Name: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: {self.__balance}"
        

user1=BankAccount("Rajat",5433,1000)

bank_on=True
while bank_on:
    user_input=int(input("""What would you like to do?
1. Deposit money, Press 1
2. Withdraw money, Press 2
3. Check balance, Press 3
4. Change pin, Press 4
5. Check Transaction History, Press 5
6. Check Interest Rates, Press 6
7. Calculate Interest on Savings, Press 7
8. Show Account info, Press 8
9. Go Back, Press 9
"""))
    if user_input == 1:
        os.system('cls' if os.name=='nt' else 'clear')
        amount=int(input("Enter the amount to deposit."))
        print(user1.deposit(amount))
        
    elif user_input == 2:
        os.system('cls' if os.name=='nt' else 'clear')
        amount=int(input("Enter the amount to withdraw. "))
        pin=int(input("Enter the account pin: "))
        print(user1.withdraw(amount,pin))
        
    elif user_input == 3:
        os.system('cls' if os.name=='nt' else 'clear')
        pin=int(input("Enter your pin: "))
        print(user1.check_balance(pin))
        
    elif user_input == 4:
        os.system('cls' if os.name=='nt' else 'clear')
        old_pin=int(input("Enter the old pin: "))
        new_pin=int(input("Enter the new pin: "))
        print(user1.change_pin(old_pin,new_pin))
    elif user_input == 5:
        os.system('cls' if os.name=='nt' else 'clear')
        print(user1.transaction_history())
    elif user_input == 6:
        os.system('cls' if os.name=='nt' else 'clear')
        print(user1.check_interest_rates())
    elif user_input == 7:
        os.system('cls' if os.name=='nt' else 'clear')
        print(user1.add_interest())
    elif user_input == 8:
        os.system('cls' if os.name=='nt' else 'clear')
        print(user1.account_information())
    else:
        bank_on = False
