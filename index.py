# Function to calculate the final price after applying discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount)

    # Print result
    if discount >= 20:
        print(f"Discount applied. Final price: {final_price}")
    else:
        print(f"No discount applied. Final price: {final_price}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
