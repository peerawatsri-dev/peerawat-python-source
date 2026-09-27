def deposit(money):
    total = 1000
    try:
        amount = float(money)
        try:
            if amount <= 0:
                raise ValueError
            total = total + amount

        except ValueError:
            print("เกิดข้อผิดพลาด: จำนวนเงินฝากต้องมากกว่า 0")
        else:
                print("ฝากเงินสำเร็จ")
                print(f"ยอดเงินคงเหลือ:{total}")
    except ValueError:
        print("เกิดข้อผิดพลาด: กรุณากรอกจำนวนเป็นตัวเลขเท่านั้น")
    finally:
        print("สิ้นสุดรายการฝากเงิน ")

print("ยอดเงินเริ่มต้น : 1000 บาท")
user_input = input("จำนวนเงินที่ต้องการฝาก : ")
deposit(user_input)