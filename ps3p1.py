stksym = input("Enter stock ticker symbol: ")
numofshr = float(input("Enter number of shares: "))
cpshr = float(input("Enter cost per share: "))

amtinv = numofshr * cpshr

print(f"You have invested ${amtinv:.2f} in {stksym}.")