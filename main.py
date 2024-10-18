fees = 150000
classes = 60
std_atd = int(input("Enter No. of Classes Attended: "))
std_fee_paid = int(input("Enter Amount of School Fees Paid: "))

if std_fee_paid<(100/100)*fees:
    print("Student is not eligible to write exams!!")
elif std_atd<=(79/100)*classes:
    print("Student is not eligible to write exams!!")
else:
    print("Student is eligible to write exams!!")    