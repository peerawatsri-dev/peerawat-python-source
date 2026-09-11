def calculate_electricity_cost(u):
    total = 0.0
    if u > 200:
        total = (2.50 * 50)+(3.00 * 50)+(100 * 3.50)+((u - 200)*4.00)+25
        print("1-50 หน่วย: 120.00 บาท ")
        print("51-100 หน่วย: 150.00 บาท ")
        print("101-200 หน่วย: 350.00 บาท ")
        print(f"200 - {u}หน่วย: {(u - 200)*4.00} บาท ")
        print("ค่าบริการ 25.00 บาท ")
        print(f"รวม {total}")
    elif u > 100:
         total = (2.50 * 50)+(3.00 * 50)+((u - 100)*3.50)+25
         print("1-50 หน่วย: 120.00 บาท ")
         print("51-100 หน่วย: 150.00 บาท ")
         print(f"101 -{u} หน่วย: {(u - 100)*3.50} บาท ")
         print("ค่าบริการ 25.00 บาท ")
         print(f"รวม {total}")
    elif u > 50:
        total = (2.50 * 50)+((u - 50)*3.00)+25
        print("1-50 หน่วย: 120.00 บาท ")
        print(f"51-{u} หน่วย: {(u - 50)*3.00} บาทบาท ")
        print("ค่าบริการ 25.00 บาท ")
        print(f"รวม {total}")
    elif u >=0:
        total = (2.50 * u )+25
        print(f"1 - {u} หน่วย : {u * 2.50} บาท")
        print("ค่าบริการ 25.00 บาท ")
        print(f"รวม {total}")
    else:
        print("จำนวนไม่ถูกต้อง")



print("โปรเเกรคำนวนค่าไฟฟ้า")
while(True):
    print("1 คำนวนค่าไฟฟ้า")
    print("2 ออกโปรเเกรม")
    choice = input("เลือกเมนู = ")

    if choice == "1":
        u = int(input("กรอกจำนวนหน่วยไฟฟ้า = "))
        calculate_electricity_cost(u)
    elif choice == "2":
        break
    else:
        print("ข้อมูลไม่ถูกต้อง")
  
