def calculate_discount(price, discount_percentage):
   
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

userPrice = float(input('Enter the price of the chosen item: '))
userDiscount = float(input('Enter the discount percentage:'))

finalPrice = calculate_discount(userPrice, userDiscount)

if finalPrice != userPrice:
    print('Final price after discount :', finalPrice)
else:
    print('No discount available:', userPrice)
    