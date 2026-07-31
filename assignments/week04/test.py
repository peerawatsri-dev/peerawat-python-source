# รับชื่อจริง (ข้อความ) จาก user
#นับจำนวนสระทั้งหมดในข้อความ นั้นว่ามีกี่ตัว
#ตัวอย่างหน้าจอ 
#what is your name? pop
#your text have 3 vewels.
name = input("what is your name?: ")
count = 0
letter = list(name)
for letter in name:
    if letter == 'a' or letter =='A':
        count = count + 1
    elif letter == 'e' or letter =='E':
        count = count + 1
    elif letter == 'i' or letter =='I':
       count = count + 1
    elif letter == 'o' or letter =='O':
        count = count + 1
    elif letter == 'u' or letter =='U':
        count = count + 1
print(f"your text have {count} vowels")



