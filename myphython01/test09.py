# สร้างโปรแกรมคำนวณเงินเดือนสุทธิที่ต้องจ่ายหลังจากหักภาษีแล้ว 7% ของเงินเดือน  และหักค่าประกันสังคม 3% ของเงินเดือน
# โดยรับค่ารหัสพนักงาน ชื่อพนักงาน เงินเดือน ทางแป้นพิมพ์ และแสดงผลข้อมูลที่รับมา
# พร้อมกับรายละเอียดว่าต้องเสียภาษีกี่บาท หักค่าประกันสังคมกี่บาท และต้องจ่ายเงินเดือนสุทธิกี่บาท

print('=========================')
print('เครื่องคำนวณเงินเดือน')
print('=========================')
print("\n")
print('-------------------------')
emp_code = input("ใส่รหัสพนักงาน: ")
emp_name = input("ใส่ชื่อพนักงาน: ")
emp_salary = input("ใส่เงินเดือน: ")
print('-------------------------')
print("\n")
tax = float(emp_salary) * 0.07
social_security = float(emp_salary) * 0.03
emp_salary_net = float(emp_salary) - tax - social_security
print("\n--- Salary Details ---")
print(f'รหัสพนักงาน : {emp_code} ชื่อพนักงาน : {emp_name} เงินเดือน : {emp_salary}')
print(f'เสีย Tax : {tax} บาท')
print(f'เสีย social_securit : {social_security} บาท')
print(f'ต้องจ่ายเงินเดือนทั้งสิ้น : {emp_salary_net} บาท')
print('-------------------------')
# ใช้ ,
print('-------------------------')
print('รหัสพนักงาน : ',{emp_code},'ชื่อพนักงาน : ',{emp_name},'เงินเดือน : ',{emp_salary})
print('เสีย Tax : ' ,{tax},'บาท')
print('เสีย social_securit : ',{social_security},'บาท')
print('ต้องจ่ายเงินเดือนทั้งสิ้น : ',{emp_salary_net},'บาท')
print('-------------------------')
# ใช้ +
print('-------------------------')
print('รหัสพนักงาน : '+ str(emp_code) +'ชื่อพนักงาน : '+ str(emp_name) +'เงินเดือน : '+ str(emp_salary))
print('เสีย Tax : ' + str(tax) +'บาท')
print('เสีย social_securit : '+ str(social_security) +'บาท')
print('ต้องจ่ายเงินเดือนทั้งสิ้น : '+ str(emp_salary_net) +'บาท')
print('-------------------------')
# ใช้ format
print('-------------------------')
print('รหัสพนักงาน : {} ชื่อพนักงาน : {} เงินเดือน : {}'.format(emp_code,emp_name,emp_salary))
print('เสีย Tax : {} บาท'.format(tax))
print('เสีย social_securit : {} บาท'.format(social_security))
print('ต้องจ่ายเงินเดือนทั้งสิ้น : {} บาท'.format(emp_salary_net))
print('-------------------------')
