sec_num = 5
num_of_guess = 0
end_of_guess = False
guess_limit = 5
guess = None


print("You can guess 5 times in this WHILE LOOP.")
while guess != sec_num and not end_of_guess:
    
    if num_of_guess < guess_limit:
        guess = int(input("Enter a number: "))

        if num_of_guess  + 1 == 1:
            print(f"You have tried { num_of_guess + 1 } time. Try again")
        elif num_of_guess  + 1 == guess_limit:
            print(f"You have tried { num_of_guess + 1 } times. You LOSE")
        else:
            print(f"You have tried { num_of_guess + 1 } times. Try again")
    else:
        end_of_guess  = True

    num_of_guess += 1

if end_of_guess:
    print("LOSE")
else:
    print("WIN")




print("You can guess 5 times in this FOR LOOP.")

for num_of_guess  in range(guess_limit):
    
    guess = int(input("Enter a number: "))

    if guess != sec_num :
        if num_of_guess  + 1 == 1:
            print(f"You have tried { num_of_guess +1 } time. Try again")
        elif num_of_guess  + 1 == guess_limit:
            print(f"You have tried { num_of_guess +1 } times. You LOSE")
        else:
            print(f"You have tried { num_of_guess +1 } times. Try again")

    else:
        print("WINNNNNN!!!!")
        break
    
