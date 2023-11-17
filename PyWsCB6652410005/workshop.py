import os

def crefile():
    filename = input("กรุณาตั้งชื่อไฟล์ (ภาษาอังกฤษ) โดยใส่นามสกุล .txt: ")
    if not filename.endswith(".txt"):
        print("ชื่อ-นามสกุลไฟล์ไม่ถูกต้อง กรุณาป้อนใหม่")
        return
    
    with open(filename, 'w') as file:
        stuname = input("ป้อน ชื่อ-สกุลนักเรียน: ")
        midscore = float(input("ป้อน คะแนนสอบกลางภาค: "))
        finalscore = float(input("ป้อน คะแนนสอบปลายภาค: "))
        kscore = float(input("ป้อน คะแนนเก็บ: "))
        
        totalscore = midscore + finalscore + kscore
        result = "ผ่าน" if totalscore > 50 else "ไม่ผ่าน"
        
        file.write(f"{stuname},{midscore},{finalscore},{kscore},{totalscore},{result}\n")
    
    print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")

def listfiles():
    files = [f for f in os.listdir('.') if f.endswith('.txt')]
    if not files:
        print("ไม่มีไฟล์ใดๆ อยู่เลย")
        return
    
    print("รายชื่อไฟล์ทั้งหมด:")
    for file in files:
        print(file)

def addfile():
    listfiles()
    filename = input("เลือกไฟล์ที่ต้องการเพิ่มข้อมูล (ระบุชื่อไฟล์): ")
    
    if filename not in os.listdir('.'):
        print("คุณพิมพ์ชื่อไฟล์ผิด")
        return
    
    with open(filename, 'a') as file:
        stuname = input("ป้อน ชื่อ-สกุลนักเรียน: ")
        midscore = float(input("ป้อน คะแนนสอบกลางภาค: "))
        finalscore = float(input("ป้อน คะแนนสอบปลายภาค: "))
        kscore = float(input("ป้อน คะแนนเก็บ: "))
        
        totalscore = midscore + finalscore + kscore
        result = "ผ่าน" if totalscore > 50 else "ไม่ผ่าน"
        
        file.write(f"{stuname},{midscore},{finalscore},{kscore},{totalscore},{result}\n")
    
    print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")

def readfile():
    listfiles()
    filename = input("เลือกไฟล์ที่ต้องการอ่านข้อมูล (ระบุชื่อไฟล์): ")
    
    if filename not in os.listdir('.'):
        print("คุณพิมพ์ชื่อไฟล์ผิด")
        return
    
    with open(filename, 'r') as file:
        data = file.read()
        print(data)

def deletfile():
    listfiles()
    filename = input("เลือกไฟล์ที่ต้องการลบ (ระบุชื่อไฟล์): ")
    
    if filename not in os.listdir('.'):
        print("คุณพิมพ์ชื่อไฟล์ผิด")
        return
    
    os.remove(filename)
    print("ลบไฟล์เรียบร้อยแล้ว")

while True:
    print("\nเมนู:")
    print("1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล")
    print("2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์")
    print("3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล")
    print("4. เลือกวิชาและลบไฟล์")
    print("0. จบการทำงาน")
    
    choice = input("เลือกเมนู: ")

    if choice == '1':
        crefile()
    elif choice == '2':
        addfile()
    elif choice == '3':
        readfile()
    elif choice == '4':
        deletfile()
    elif choice == '0':
        print("จบการทำงานของโปรแกรม")
        break
    else:
        print("กรุณาเลือกเมนู 1, 2, 3, 4, หรือ 0 เท่านั้น")