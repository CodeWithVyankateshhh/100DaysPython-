print("Welcome to the tip calculator")

Bill = float(input("What was the Total Bill? = "))

Tip = int(input("How much tip would you like to give? 10, 12 or 15 = "))

TotalPeopleSplit = int(input("How many people to split the bill? = "))

TipPercent = (Tip * Bill) /100
OrignalBill = TipPercent + Bill

FinalBill = OrignalBill / TotalPeopleSplit
print(f"Each Persone should pay {FinalBill} $")