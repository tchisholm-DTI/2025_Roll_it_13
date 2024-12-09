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


def make_statement(statement, decoration):
    """Adds emoji/additional characters to the start and end of the headings"""

    ends = decoration * 3
    print(f"{ends} {statement} {ends}")


# Main routine
# At the start of the game, the computer/user scores are both zero (initialise them)
comp_score = 0
user_score = 0
game_goal = 0

game_goal = initial_points("Game Goal")  # should be a function call

# Play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    # Start of round loop
    # For testing purposes, ask the user what the points for the user/computer were
    comp_points = int(input("Enter the computer points at the end of the round: "))
    user_points = int(input("Enter the user points at the end of the round: "))

    # Outside rounds loop - update score with round points, only add points to the score of the
    comp_score += comp_points
    user_score += user_points
    # Show overall scores (add this to rounds loop)
    make_statement("Game Update", "*")
    print(f"User Score: {user_score} | Computer Score: {comp_score}")

# end of entire game, output final results
print()
if user_score > comp_score:
    make_statement("The user won.", "=")
else:
    print("The computer won.")
