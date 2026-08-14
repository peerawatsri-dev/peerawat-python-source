"""
# Example 3: Mathematical function

def calculate_rectangle_area(length, width):
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)


#geometry หาพื้นที่สามเหลี่ยม
def calculate_triangle_area(height, base):
    area = 0.5 * height * base
    print (f"area = 0.5 x {height} x {base} = {area}")

print("calculate")
calculate_triangle_area(4, 10)
"""
"""
เขียน Fucntion  ที่สามารถเเปลงเงินจาก
THB <-> USD : USD = 32 THB 


โดยใช้ชื่อ fuction convert_currency(100,USD)

เเสดงผล
100 THB = 3.3 USD
"""
def convert_currency(amount, currency):
    if currency == "USD":
        return amount / 32
    elif currency == "THB":
        return amount * 32
    else:
        return None
 
print(f"100 THB = {convert_currency(100, 'USD')} USD")
print(f"100 USD = {convert_currency(100, 'THB')} THB")



