import random


def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""
    double = "no"

    # Roll the dice for the user and note if they got a double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total} ")

    return total, double


# Roll the dice for the user and note of they got a double
initial_user = initial_points("User")
initial_comp = initial_points("Comp")

print("Initial User", initial_user)
print("Initial Computer", initial_comp)

# Retrieve user points (first item returned from function)
user_points = initial_user[0]
comp_points = initial_comp[0]

double_user = initial_user[1]


# Let the user know if they qualify for double points
if double_user == "yes":
    print("Great news - if you win, you will earn double points!")
