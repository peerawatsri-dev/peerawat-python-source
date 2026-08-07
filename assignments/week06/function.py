""" เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:

รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
return string ที่จัดรูปแบบข้อมูลผู้ใช้
รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"
เขียนโปรเเกรมในส่วนการใช้งานด้วย
"""

def create_user_profile(username, age=18, premium =False):
    user = "Premium User" if premium else "Standard User"
    return f"{username} (age):{age} - {user}"

print(create_user_profile("mine"))
print(create_user_profile("boy",22))
print(create_user_profile("tom",25,True))

    