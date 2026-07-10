# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal ราคาเต็ม
subtotal = item_price * quantity

# TODO: Calculate discount amount ส่วนลด
discount_amount = subtotal *(discount_percent/100)

# TODO: Calculate price after discount ราคาลดเเล้ว
price_after_discount =subtotal - discount_amount

# TODO: Calculate tax amount ภาษี
tax = price_after_discount* (tax_percent / 100)


# TODO: Calculate final total จ่ายเท่าไหร่
total = price_after_discount + tax

# TODO: Display itemized receipt เเสดงผล
print("Calculate subtota",subtotal)
print("Calculate discount amount",discount_amount)
print("Calculate price after discount",price_after_discount)
print("Calculate tax amount",tax)
print(" Calculate final total",total)