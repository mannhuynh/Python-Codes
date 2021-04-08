class Water:
    """
    How do you access a class variable (e.g., boiling_temperature ) from within a method (e.g., from state)?
    The answer is: You can access class variables by using self. So, in our example,
    you would write self.boiling_temperature. See the state method below for an illustration.
    The key takeaway here is that even though boiling_temperature is a class variable
     (i.e., it belongs to the class and not to the instance of the class),
     such a variable can still be accessed
     through the instance (i.e., through self).
     So, class variables belong to the class,
     but they also belong to the instance created by that class.
    """
    boiling_temperature = 100
    freezing_temperature = 0

    def __init__(self, temperature):
        self.temperature = temperature

    def state(self):
        # Return 'solid' if water temp is less or equal than 0
        if self.temperature <= self.freezing_temperature:
            return 'solid'
        # Return 'liquid' if water temp is between 0 and 100
        elif self.freezing_temperature < self.temperature < self.boiling_temperature:
            return 'liquid'
        # Return 'gas' in other scenarios (water temp higher than 100)
        else:
            return 'gas'
