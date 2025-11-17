#to find out whether a student has passed or failed it requres a total of 40% and atleast 33% in each marks as an input from the user
m1 = int(input("enter the marks:"))
m2 = int(input("enter the marks:"))
m3 = int(input("enter the marks:"))
s = int((m1+m2+m3)*100)/300
print("the percentage of the student is:",s)
if s>=40:
      print("the student has passed the exam")
elif m1>=33 and m2>=33 and m3>=33:
            print("the student has passed the exam")
else:
    print("the student has failed the exam")