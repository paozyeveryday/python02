try:
    w = int(input("นํ้าหนัก "))
    h = int(input("ส่วนสุง "))
    bmi = w/(h/100)**2

except:
    print("error ครับผม")
    
else:
    print("คำตอบ ",bmi)