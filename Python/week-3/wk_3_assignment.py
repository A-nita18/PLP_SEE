#define the function
def calculate_discount(price, discount_percent):
    if discount_percent>20:
        return price* (100-discount_percent)/100
    else:
        return price
    
#prompt user
price=float(input("Enter the original price:"))
discount_percent=float(input("Enter the discount percentage:"))

print("Final price is:",calculate_discount(price, discount_percent))