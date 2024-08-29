Food_bill = float(input("Whats your total bill??\n"))#100
tip_percentage = float(input("what percent would you tip\n")) #10%
conversion:float = (tip_percentage/100) *100
print(f"your total tip will be {conversion}")
print(f"Total amount to be paid is:",Food_bill + conversion)

