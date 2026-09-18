### ex เครื่องคำนวณอย่างปลอดภัย
""" เขียน program รับตัวเลข 2  จำนวนเเละตัวดำเนินการ 1 ตัว + - * / เเล้วเเสดงผลลัพธ์
เงื่อนไข
-ผู้ใช้กรอกข้อมูลที่ไม่ใช้ตัวเลข #valueerror 
-ผู้ใช้เลือกตัวดำเนินการนอกเหนือจาก + - * / raise valueerror
-ผุ้ใช้พยายามหารด้วย 0 #zerodivisionerror
-โปรเเกรมต้องเเสดง จบการทำงาน เสมอด้วย finally

ตัวอยางผล
ตัวเลขที 1 : 10
       2 : 0
เครื่องหมาย (+ - * /)
ไม่สามารถหารด้วยศูนย์ได้
จบการทำงาน
"""
try:
    num1 = float(input("รับเลข (1)"))
    num2 = float(input("รับเลข (2)"))
    op = input("เครื่องห่มาย (+ - * / ) ")

    if op == "+":
        rs = num1 + num2
    elif op == "-":
        rs = num1 - num2
    elif op == "*":
        rs = num1 * num2
    elif op == "/":
        rs = num1 / num2
    else:
        raise ValueError("เครื่องหมายต้อง + - * / เท่านั้น")

    print(f"{num1} {op} {num2} = {rs}")

except ValueError:
    print("เห้ยไรว่าคนไทยบอกว่าขอเเค่เลข")

except ZeroDivisionError:
    print("พี่บอกเลยนะน้องจะหาคำตอบไม่ได้นะจ๊ะเบเบ้ พี่ไม่ชอบตัวหารเลข 0")

except Exception: #กรณีอื่น
    print("ทำงานไม่ได้ ไม่รู้ตรงไหนอ่ะ")

else: #จะทำก็ต่อเมื่อไม่มี exception
    print("คำนวนเสร็จล่ะ")
finally:
    print ("จบการทำงาน")
    





