print("Welcome to First Financial Credit Union!")
print("What would you like to do today?")
print("1. Deposit")
print("2. Withdraw")
print("3. Transfer")
print("4. List All Accounts")
print("5. Add Account")
print("6. Remove Account")



action =input(":")

actnames = ["Micha"]
actbalance = [1,000]


for i in range(len(actnames)):
    print (f"Bank records for {actnames[i]}, actbalance: {actbalance[i]}")