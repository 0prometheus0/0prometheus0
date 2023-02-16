def multiplier(num):
    total=1
    x=1
    while x<=num:
        total*=x
        x+=1
    return total
def multiplide_by2(num):
    return num*2
def sqrt(num):
    return num**0.5
num=int(input("Please enter a number: "))
print("Factorial of Number: ",multiplier(num),"Square Root of Number: ",sqrt(num))