# สร้างโปรแกรมรับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้
# และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามา
# เป็นเท่าใด แล้วแสดงผลทางหน้าจอ
# สูตร  
# ผลรวม = เลขตัวที่1 + เลขตัวที่2 + เลขตัวที่3 + เลขตัวที่4 + เลขตัวที่5
# ค่าเฉลี่ย = ผลรวมของเลข 5 จำนวน / 5
 
# ============================
# Program  Average  5  Number
# ============================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# รับค่าตัวเลขจากผู้ใช้
numbers = []
for i in range(5):
    num = int(input(f"กรุณาใส่ตัวเลขตัวที่ {i+1}: "))
    numbers.append(num)

# คำนวณผลรวมและค่าเฉลี่ย
total = sum(numbers)
average = total / 5

# แสดงผลลัพธ์
print(f"\nผลรวมของตัวเลขทั้ง 5 คือ: {total}")
print(f"ค่าเฉลี่ยของตัวเลขทั้ง 5 คือ: {average:.2f}")
