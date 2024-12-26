def cal_grade(marks):
    if marks>90:
        return 'A'
    elif marks>80:
        return 'B'
    elif marks>=70:
        return 'P'
    else :
        return 'F'
def main():
    snum=input("enter roll number")
    sname=input("enter student name")
    c,cpp,java=map(float,input("enter marks").split())
    total=c+cpp+java
    avg=total/3
    if avg<70:
        result="Fail"
        grade="F"
    else:
        result="pass"
        grade=cal_grade(avg)
    print(f"Student Number: {snum}")
    print(f"Student Name: {sname}")
    print(f"Total Marks: {total:.2f}")
    print(f"Average Marks: {avg:.2f}")
    print(f"Result: {result}")
    print(f"Grade: {grade}")
main()
        