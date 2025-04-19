# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).

basket = [("Peaches", 3.0, 2.99),
          ("Pears", 5.0, 1.66),
          ("Plums", 2.5, 3.99)
          ]

# Calculate the total price for each item (weight times price per pound)
# and add them up to get a subtotal.

subtotal = 0.00
for item in basket:
    fruit, weight, unit_price = item
    subtotal = subtotal + (weight * unit_price)

# Now calculate the sales tax and total bill.

tax_rate = 0.06625  # 6.625% sales tax in New Jersey
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

# Print the receipt for the customer.

for item in basket:
    output = "You are buying {} pound of {} at {} per pound".format(item[0],item[1],item[2])
    print(output)

print("Subtotal:  ${:5,.2f}".format(subtotal))
print("Sales Tax: ${:5,.2f}".format(tax_amount))
print("Total:     ${:5,.2f}".format(total))