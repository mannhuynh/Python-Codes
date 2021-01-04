"""
The Nile fullfilment agency brings everything you could possibly want straight to your door! Use your knowledge of Python functions and how to manipulate arguments to help automate practices for the biggest world-changing company.
At The Nile our biggest concern is our consumers, and our biggest cost is delivering their goods to them. We want to develop a program that will help us minimize these costs so we can continue making everyone happy.
"""
from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# First we’ll need to calculate these costs using a function that you’re going to write called calculate_shipping_cost().
# Give calculate_shipping_cost three parameters: from_coords, to_coords, and shipping_type.
# What about our shoppers who hastily purchase goods without indicating their shipping type? Let’s give our function a default argument for shipping_type. Since they’re in such a hurry let’s make the default argument 'Overnight'. They’ll be happier to get what they ordered earlier, and we’ll be happier because they paid more money for it. It’s a win-win!
def calculate_shipping_cost(from_coords, to_coords, shipping_type = 'Overnight'):
    # Both from_coords and to_coords are tuples, containing first the latitude and then the longitude. Since our get_distance() function looks for all four as separate arguments, we’ll need to separate these variables out.
    # Inside calculate_shipping_cost unpack those tuples into from_lat, from_long, to_lat, and to_long.
    from_lat, from_long = from_coords
    to_lat, to_long = to_coords

    # Now call get_distance(from_lat, from_long, to_lat, to_long) and save the result as distance.
    distance = get_distance(from_lat, from_long, to_lat, to_long)   # get_distance() from nile.py
        # One way is to use the * spread operator, which would unpack those coordinates in the function call.
        # distance = get_distance(*from_coords, *to_coords)
    
    # Next, get the shipping_rate by using the provided SHIPPING_PRICES dictionary and fetching the key passed in as shipping_type.
    shipping_rate = SHIPPING_PRICES[shipping_type]  #SHIPPING_PRICES from nile.py

    # Calculate the price by multiplying the distance by the shipping_rate.
    price = distance * shipping_rate

    # Finally, return the formatted price, created by calling the provided format_price() on the price itself.    
    return format_price(price)  # format_price() from nile.py

# Want to make sure you wrote the function correctly? Try calling test_function(calculate_shipping_cost) after your function definition.
test_function(calculate_shipping_cost)

"""
At The Nile, we have a joke. Without our fantastic drivers, who fulfill orders every day, we’d just be sitting with millions of toys, electronics, and clothing in warehouses to ourselves.
Our team is important, and we want to make sure the hardest workers find their home in our careers. In order to do that, we need to figure out who the best person is for each job.
"""
# Write a function called calculate_driver_cost() with distance as the first parmameter, and as many drivers as are available as positional arguments after that, as drivers.
def calculate_driver_cost(distance, *drivers):
    # In order to find the best person, we need to calculate how much it would cost for any of the drivers to fulfill this order.
    # Create two new variables, cheapest_driver and cheapest_driver_price. Set them both to None.
    cheapest_driver = None
    cheapest_driver_price = None

    # Now let’s iterate over every driver in drivers. Use a for loop.
    for driver in drivers:
        # First calculate the driver_time for each driver by multiplying driver.speed by distance.
        driver_time = driver.speed * distance

        # Next calculate the price_for_driver by multiplying driver.salary by driver_time
        price_for_driver = driver.salary * driver_time

        # Now we want to check if the current driver is the cheapest driver we’ve looked at.
        # First, we’ll check if cheapest_driver is None, this likely means this is the first driver we’ve looked at.
        # In that case, set cheapest_driver equal to driver and then set cheapest_driver_price equal to price_for_driver.
        if cheapest_driver in None:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver      
      
        # In an elif statment, check if price_for_driver is less than cheapest_driver_price. This means that our current driver is cheaper than the driver stored in cheapest_driver.
        # Update cheapest_driver to be equal to driver and update cheapest_driver_price to be equal to price_for_driver.
        elif price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
    return cheapest_driver_price, cheapest_driver

test_function(calculate_shipping_cost)

# Great first day, friend! Let’s try and figure out all the money you’ve saved us today.
# Let’s define a function called calculate_money_made().
# This function will be passed a number of Trip IDs with corresponding trip information as arguments, so let’s just take any keyword arguments passed into it. Store them all as trips!
def calculate_money_made(**trips):
    # Let’s start a counter at 0. Create a variable called total_money_made that will count up for us.
    total_money_made = 0

    # Iterate through every trip_id and trip in the trips dictionary.
    for trip_id, trip in trips.items():
        # Calculate the trip revenue into the variable trip_revenue by calculating trip.cost minus trip.driver.cost.
        trip_revenue = trip.cost - trip.driver.cost

        # Add up that sweet revenue by incrementing total_money_made by trip_revenue.
        total_money_made += trip_revenue

    # Outside your for loop, return the total!
    return total_money_made

# Congratulations! You’ve been a real life-saver around these parts. We broke up functions using arbitrary and default parameters! Remember you can test your function by calling test_function(calculate_money_made) afterwards!
test_function(calculate_money_made)
