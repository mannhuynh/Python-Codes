class GuessNumber:
    def __init__(self, picked_number, min = 0, max = 100):
        self.number = picked_number
        self.min = min
        self.max = max
        self.counter = 0

    def is_number_valid(self, input_number):
        try:
            number = int(input_number)
        except:
            return False
        return self.min <= number <= self.max

    def get_guess(self):
        print("I have picked a number for you to guess.")
        guess = input("Enter a number from {} to {} and start our guessing game: ".format(self.min, self.max))

        if self.is_number_valid(guess):
            return int(guess)
        print("Your number is not valid")
        return self.get_guess()   # recursion as a while loop to check the valid number

    def guessing(self):
        while True:
            self.counter += 1

            guess = self.get_guess()

            if guess < self.number:
                print("Your number is smaller than what I have picked!")
            elif guess > self.number:
                print("Your number is bigger than what I have picked!")
            else:
                break
        print("You are correct in {} time(s) of guessing!".format(self.counter))            

play = GuessNumber(45, 0, 100)
play.guessing()



    
