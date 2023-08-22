#รับคำ คือ หยุดให้ user ป้อนทางแป้นพิมพ์ 
#variable (ตัวแปร) = identifier คือ ชื่อที่ต้องตั้งขึ้นมาเอง เป็นไปตามกฎของภาษานั้น

#การแปลงข้อมูล (casting/type conversion) -> str( ) ,int( ) , float( )
studentID = input('ป้อน STUDENT ID: ')
stu_name = input('ป้อน STUDENT Name: ')
stu_birth_year = input('ป้อน STUDENT Birth Year: ')
print(f"ยินดีต้อนรับ {studentID} {stu_name} สู่ SAU")
print(f"คุณเกิดปี {stu_birth_year} แปลว่าคุณอายุ {2023 - int(stu_birth_year)} ปี") 
print("ยินดีต้อนรับ",studentID,stu_name,"สู่ SAU")
print("คุณเกิดปี" ,stu_birth_year,"แปลว่าคุณอายุ",2023 - int(stu_birth_year), "ปี")
print("ยินดีต้อนรับ "+str(studentID)+' '+str(stu_name)+' '+str("สู่ SAU"))
print("คุณเกิดปี "+str(stu_birth_year)+' '+str("แปลว่าคุณอายุ ")+' '+str(2023 -int(stu_birth_year))+' '+str("ปี "))
print("ยินดีต้อนรับ {} {}" .format(studentID,stu_name))
print("คุณเกิดปี   {0} {1} {2} } " .format(stu_birth_year(2023 -int(stu_birth_year))))