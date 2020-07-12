control_var = True

while control_var:
    number = input("Enter the number : ") # string '9474'

    if '.' in number:
        print("Please enter an integer number! ")
        continue
    elif number[0] == '-':
        print(" Please enter a positive number! ")
        continue
    elif not number.isdigit():
        print("Do not use any entries other than numeric values! ")
        continue

    else:
        control_var = False
n = len(number) # 4
# print(n)
sum_nth_pow = 0

for i in number: #'9474' => i-> '9' ->'4' -> '7' -> '4'
    sum_nth_pow += int(i)**n # sum_nth_pow=sum_nth_pow+int(i)*n
if int(number) == sum_nth_pow:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
