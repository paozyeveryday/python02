def BMT(w,h):
    bmi = w/pow(h,2)  #หรือ w/h**2
    return bmi

w = int(input("รับค่านํ้าหนัก w:" ))
h = int(input("รับค่าส่วนสูง h:" ))

print("ดัชนีมวลหาย(BMT)", BMT(w,h/100))

ิbmi =BMT(w,h/100)
if bmi <18.5 :
    print("นํ้าหนักตํ่ากว่า์เกณ")
elif bmi >= 18.5 and bmi <= 22.9:
    print("สมส่วน")
elif bmi >= 23 and bmi <= 24.9:
    print("นํ้าหนักเกิน")
elif bmi >= 25 and bmi <= 29.9:
    print("โรคอ้วน")
elif bmi>30:
    print("โรคอ้วนอันตราย")
