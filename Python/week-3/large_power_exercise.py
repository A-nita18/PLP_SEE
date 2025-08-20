#define function
def large_power(base,exponent):
    return(base**exponent >5000)

#prompt user for input
base = float(input("Enter the base: "))
exponent=float(input("Enter the exponent: "))
result = large_power(base,exponent)
print(result)
