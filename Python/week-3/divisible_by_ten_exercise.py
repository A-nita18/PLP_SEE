#prompt the user
num=float(input("Enter the number:"))
#define the function
def divisible_by_ten(num):
    if num%10==0:
        return f"True"
    else:
        return f"False"
    
print(divisible_by_ten(num))