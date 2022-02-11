
f = open('data', 'wb')
txt = bytes('ยินดีตอนรับสู่ Python \n','utf-8')
f.write('โดย สมเกียรติ Python','utf-8')
f.write(txt)
f.close()

print("อ่านข้อมูลจาก binary file \n")
f = open('data','rb)
print(f.read(50))
close 