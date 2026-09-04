#รับค่า  text จากผู้ใช้
#รับอักขระ
#เเสดงผลจำนวนอักขระใน text
"""
text = 'Hello World'
for letter in text:
    if letter == 'l':
        count += 1
print(f"{count} letters 'l' found in '{text}'")

text = input("Enter name : ")
character = input("Enter character : ")
count = 0
for i in text:
    if i == character:
        count+= 1
print(f"Insert your text : {text} ")
print(f"character : {character} ")
print(f"{count} letters '{character}' found in '{text}' ")
"""


# ตรวจสอบความเเข็งเเรงของ  password
# นิยามของ s password , ยาวกว่า 8 ตัว ,มี char @ 1 ตัว , มีเลข ,มีตัวอักษร
# เเสดงผล 
# insert your password : test@123
# your password is strong/not !
"""
password = input("enter your password = ")
lenght = len(password) >= 8
at = password.count('@') == 1
h_digit = False
h_alpha = False

for i in password:
    if i.isdigit():
        h_digit = True
    elif i.isalpha():
        h_alpha = True

if lenght and at and h_digit and h_alpha:
    print("your password is strong")
else:
    print("your password is not strong")
"""

    