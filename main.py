from bank import Bank
from customer import Customer
from transaction import Deposit, Withdraw

# Create a bank instance
bank = Bank("State Bank of Python")

def main():
    while True:
        print("\n🏦 Bank Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Account Details")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            acc_num = input("Enter account number: ")
            customer = Customer(name, acc_num)
            bank.add_customer(customer)
            print("✅ Account Created Successfully!")

        elif choice == "2":
            acc_num = input("Enter account number: ")
            customer = bank.get_customer(acc_num)
            if customer:
                amount = float(input("Enter amount to deposit: "))
                transaction = Deposit()
                print(transaction.execute(customer, amount))
            else:
                print("❌ Account not found!")

        elif choice == "3":
            acc_num = input("Enter account number: ")
            customer = bank.get_customer(acc_num)
            if customer:
                amount = float(input("Enter amount to withdraw: "))
                transaction = Withdraw()
                print(transaction.execute(customer, amount))
            else:
                print("❌ Account not found!")

        elif choice == "4":
            acc_num = input("Enter account number: ")
            customer = bank.get_customer(acc_num)
            if customer:
                print(customer.get_account_details())
            else:
                print("❌ Account not found!")

        elif choice == "5":
            print("Thank you for using the Bank Management System! 👋")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
