"""
The Fender, a notorious computer hacker and general villain of the people, has compromised several top-secret passwords including your own. Your mission, should you choose to accept it, is threefold. You must acquire access to The Fender‘s systems, you must update his "passwords.txt" file to scramble the secret data. The last thing you need to do is add the signature of Slash Null, a different hacker whose nefarious deeds could be very conveniently halted by The Fender if they viewed Slash Null as a threat.
"""
# First import the CSV module, since we’ll be needing it to parse the data.
import csv

# We need to create a list of users whose passwords have been compromised, create a new list and save it to the variable compromised_users.
compromised_users = []

# Next we’ll need you to open up the file itself. Store it in a file object called password_file.
# Pass the password_file object holder to our CSV reader for parsing. Save the parsed csv.DictReader object as password_csv.
with open("python_codecademy\\hacking_the_fender\\passwords.csv") as password_file:
    password_csv = csv.DictReader(password_file)

# Now we’ll want to iterate through each of the lines in the CSV.
# Create a for loop and save each row of the CSV into the temporary variable password_row.
# We want to add each username to the list of compromised_users. Use the list’s .append() method to add the username to compromised_users instead of printing them.
    for row in password_csv:
        compromised_users.append(row["Username"])
    print(compromised_users)

# Exit out of your with block for "passwords.csv". We have all the data we need from that file.
# Start a new with block, opening a file called compromised_users.txt. Open this file in write-mode, saving the file object as compromised_user_file.
with open("python_codecademy\\hacking_the_fender\\compromised_users.txt", "w") as compromised_user_file:

# Inside the new context-managed block opened by the with statement start a new for loop.
# Iterate over each of your compromised_users.
# Write the username of each compromised_user in compromised_users to compromised_user_file.
    for user in compromised_users:
        compromised_user_file.write(user)

# Your boss needs to know that you were successful in retrieving that compromised data. We’ll need to send him an encoded message over the internet. Let’s use JSON to do that.
# First we’ll need to import the json module.
# Open a new JSON file in write-mode called boss_message.json. Save the file object to the variable boss_message.
import json

with open("python_codecademy\\hacking_the_fender\\boss_message.json", "w") as boss_message:
    
# Create a Python dictionary object within your with statement that relays a boss message. Call this boss_message_dict.
# Give it a "recipient" key with a value "The Boss".
# Also give it a "message" key with the value "Mission Success".
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}

# Write out boss_message_dict to boss_message using json.dump().
    json.dump(boss_message_dict, boss_message)

# Now that we’ve safely recovered the compromised users we’ll want to remove the "passwords.csv" file completely.
# Create a new with block and open "new_passwords.csv" in write-mode. Save the file object to a variable called new_passwords_obj.
with open("python_codecademy\\hacking_the_fender\\new_passwords.csv", "w") as new_password_obj:

# Enemy of the people, Slash Null, is who we want The Fender to think was behind this attack. He has a signature, whenever he hacks someone he adds this signature to one of the files he touches. Save that as a multiline string to the variable slash_null_sig.
    slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
# Write slash_null_sig to new_passwords_obj. Now we have the file to replace passwords.csv with!
    new_password_obj.writelines(slash_null_sig)