want_instructions = input("Do you want to see the instructions?").lower()

# Check the user says yes/no
if want_instructions == "yes" or want_instructions == "y":
    print("You said yes.")
elif want_instructions == "no" or want_instructions == "n":
    print("You said no.")
else:
    print("Please enter yes/no.")
