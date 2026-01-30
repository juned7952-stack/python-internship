class BankAccount:                   
    def __init__(self, account_holder, balance=0):
        # Encapsulation: private attributes
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        return self.__balance

    def get_holder(self):
        return self.__account_holder


# Inheritance Example
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: {interest}")


# Method Overriding (Polymorphism)
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        # Allow overdraft up to -500
        if self.get_balance() - amount >= -500:
            # Accessing private balance via name mangling
            self._BankAccount__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.get_balance()}")
        else:
            print("Overdraft limit reached.")


# Menu-driven simulation
def main():
    print("=== Bank Account Simulation ===")
    acc1 = SavingsAccount("Juned", 1000)
    acc2 = CurrentAccount("Team Account", 500)

    accounts = {
        "1": acc1,
        "2": acc2
    }

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Add Interest (Savings Only)")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "5":
            print("Exiting... Thank you!")
            break

        acc_choice = input("Select account (1: Savings, 2: Current): ")
        account = accounts.get(acc_choice)

        if not account:
            print("Invalid account selection.")
            continue

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            print(f"Balance for {account.get_holder()}: {account.get_balance()}")

        elif choice == "4":
            if isinstance(account, SavingsAccount):
                account.add_interest()
            else:
                print("Interest can only be added to Savings Account.")

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()