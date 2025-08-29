#โปรแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชื่อ และชั้นปีทางแป้นพิมพ์แล้วแสดงข้อความต้อนรับ ดังนี้
# กรณีป้อนชั้นปี 1 แสดงข้อความ "Welcome Freshman"
# กรณีป้อนชั้นปี 2 แสดงข้อความ "Welcome Sophomore"
# กรณีป้อนชั้นปี 3 แสดงข้อความ "Welcome Junior"
# กรณีป้อนชั้นปี 4 แสดงข้อความ "Welcome Senior"
# กรณีป้อน ปีอื่นๆ  แสดงข้อความ "Oh, no ...."

print('----------------------------')
print('      สวัสดีนักศึกษาหน้าใหม่  ')
print('----------------------------')

name = input('บอกชื่อ: ')
class_ = int(input('บอกปีของคุณ: '))
print('----------------------------')

if class_ == 1 :
    print(f'Welcome Freshman คุณ {name} ')
elif class_ == 2 :
    print(f'Welcome Sophomore คุณ {name}')
elif class_ == 3 :
    print(f'Welcome Junior คุณ {name}')
elif class_ == 4 :
    print(f'Welcome Senior คุณ {name}')
else :
    print(f'Oh, no .... คุณ{name}ไม่ได้ศึกษาอยู่ที่นี้')
 