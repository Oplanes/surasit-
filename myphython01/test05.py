# คำสั่งรับค่าข้อความ string ทางแป้นพิมพ์ ใช้ฟังก์ชัน input()
# **** ตัวแปร variable คือ ชื่อที่ Dev ตั้งขึ้นเอง (ต้องเป็นไปตามกฎการตั้งชื่อ) เอาไว้เก็บข้อมูลที่เกิดขึ้นในโปรแกรม
# ฟังก์ชั่นแปลงข้อวคามเป็นตัวเลข int() หรือ float()

fullname = input ('ใส่ชื่อ: ')
year_born = input ('ใส่ปีเกิด พ.ศ.: ')
print('------------------')
print(f'Hello {fullname}')
print(f'คุณเกิดปี {year_born} ตอนนี้คูณอายุ {2568 - int(year_born)} ปี')
print('------------------')
#ใช้ ,
print('Hello',fullname)
print('คุณเกิดปี ',year_born,' ตอนนี้คูณอายุ ',2568 - int(year_born),' ปี')
print('------------------')
#ใช้ +
print('Hello ' + fullname)
print('คุณเกิดปี ' + year_born + ' ตอนนี้คูณอายุ ' + str(2568 - int(year_born)) + ' ปี')
print('------------------')
#ใช้ format()
print('Hello {} คุณเกิดปี {} ตอนนี้คูณอายุ {} ปี'.format(fullname, year_born, 2568 - int(year_born)))