"""
Sal’s Shippers has several different options for a customer to ship their package. 
They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. 
Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight.
Write a program that asks the user for the weight of their package 
and then tells them which method of shipping is cheapest 
and how much it will cost to ship their package using Sal’s Shippers.

Ground Shipping:
Weight of Package(lb)               Price per Pound     Flat Charge
2 >= weight                         $1.50               $20.00
2 < weight <= 6                     $3.00               $20.00
6 < weight <= 10                    $4.00               $20.00
10 < weight                         $4.75               $20.00

Drone Shipping
2 >= weight                         $4.50               $0.00
2 < weight <= 6                     $9.00               $0.00
6 < weight <= 10                    $12.00               $0.00
10 < weight                         $14.25               $0.00

Premium Ground Shipping: Flat charge - $125.00

"""
# Write a function for the cost of ground shipping. 
# This function should take one parameter, weight, and return the cost of shipping a package of that weight.
def ground_cost(weight):
    if weight <= 2:
        cost = weight * 1.50 + 20
    elif 2 < weight <= 6:
        cost = weight * 3.00 + 20
    elif 6 < weight <= 10:
        cost = weight * 4.00 + 20
    else:
        cost = weight * 4.75 + 20
    return cost
#A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:
print("Ground Shipping cost for 8.4 lbs is $" + str(ground_cost(8.4)))

# Premium ground shipping cost
premium_cost = 125.00

#Write a function for the cost of drone shipping
def drone_cost(weight):
    if weight <= 2:
        cost = weight * 4.50 
    elif 2 < weight <= 6:
        cost = weight * 9.00
    elif 6 < weight <= 10:
        cost = weight * 12.00
    else:
        cost = weight * 14.25
    return cost
#A package that weighs 1.5 pounds should cost $6.75 to ship by drone
print("Drone Shipping cost for 1.5 lbs is $" + str(drone_cost(1.5)))

# Using those two functions for ground shipping cost and drone shipping cost, 
# as well as the cost of premium ground shipping, write a function that takes one parameter, weight 
# and prints a statement that tells the user
# The shipping method that is cheapest.
# How much it would cost to ship a package of said weight using this method.

def cheapest_method(weight):
    if premium_cost < ground_cost(weight) and premium_cost < drone_cost(weight):
        return f"With {weight} lbs, you should use Premium Shipping with the cost of ${premium_cost}"
    elif ground_cost(weight) < premium_cost and ground_cost(weight) < drone_cost(weight):
        return f"With {weight} lbs, you should use Ground Shipping with the cost of ${ground_cost(weight)}"
    else:
        return f"With {weight} lbs, you should use Drone Shipping with the cost of ${drone_cost(weight)}"

# Test
print(cheapest_method(17))
print(cheapest_method(3.2))
print(cheapest_method(4.8))
print(cheapest_method(41.5))
