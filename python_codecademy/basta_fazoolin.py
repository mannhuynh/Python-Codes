"""
You’ve started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.
"""

# At Basta Fazoolin’ with my Heart our motto is simple: when you’re here with family, that’s great! We have four different menus: brunch, early-bird, dinner, and kids.
# Create a Menu class .
class Menu:
  
  # Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  # Give our Menu class a string representation method that will tell you the name of the menu.
  # Also, indicate in this representation when the menu is available.
  def __repr__(self):
    return self.name + " Menu is available from " + str(self.start_time) + " to " + str(self.end_time) + "."

  # Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names of purchased items.
  # Have calculate_bill return the total price of a purchase consisiting of all the items in purchased_items.
  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      bill += self.items[item]
    return bill
      
# Let’s create our first menu: brunch. Brunch is served from 11am to 4pm.
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

# Create a Menu object and save it into the variable brunch. Call it with the arguments "brunch" and the items dictionary in the code block above.
# For the start_time and end_time, either you can use a 24-hour clock (11 & 16, respectively)
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)

# Let’s create our second menu item early_bird. Early-bird Dinners are served from 3pm to 6pm.
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)

# Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm.
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

# And let’s create our last menu, kids. The kids menu is available from 11am until 9pm.
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu("Kids", kids_items, 1100, 2100)

print(kids_menu)  # Kids Menu is available from 1100 to 2100.

# Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into brunch.calculate_bill() and print out the price.
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))  # 13.5

# What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli. Calculate the bill with .calculate_bill().
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)' ])) # 21.5
