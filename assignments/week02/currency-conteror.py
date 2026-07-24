"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
#code here (2)
print ("1.THB to USD")
print ("2.USD to THB")
choice = input("1 or 2: ")

rate = 35.5 
if choice == "1":
    thb = float(input("input amount (THB):"))
    usd = thb/rate
    print (f"formula: {thb:.2f} / {rate} = {usd:.2f}")
    print (f"result:{usd:.2f}")

elif choice =="2":
    usd = float(input("input amount (USD):"))
    thb = usd * rate
    print (f"formula: {usd:.2f} * {rate} = {thb:.2f}")
    print (f"result:{thb:.2f} ")
else :
    print("invalid!: ")