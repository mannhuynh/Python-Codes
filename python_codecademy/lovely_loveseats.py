
"""We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street.
 With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.
In this project, we will be storing the names and prices of a furniture store’s catalog in variables. 
You will then process the total price and item list of customers, printing them to the output terminal."""

# Create variables Lovely Seat description and price 
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

# Create variables Stylish Settee description and price 
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

# Create variables Luxurious Lamp description and price 
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Sale tax should be initialized
sales_tax = 0.088

# We have the first customer, just declare as below
customer_one_total = 0
customer_one_itemization = ""

#The first customer buy a Lovely Seat. Update the price and description to the first customer
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description + "\n"

# The first customer also decided to purchase the Luxurious Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description + "\n"

# Create a variable called customer_one_tax and set it equal to customer_one_total times sales_tax
customer_one_tax = customer_one_total * sales_tax

# Customer one's total with tax
customer_one_total += customer_one_tax

# Print Customer One Items puchased and total cost with 2 decimal point
print("Customer One Items: \n" + customer_one_itemization)
print("Customer One Total: \n" + str("%.2f" % customer_one_total)) 


