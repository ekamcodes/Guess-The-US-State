# Importing required libraries
import turtle
import pandas

# Reading state data from the CSV file
data = pandas.read_csv('50_states.csv')

# Setting up the turtle screen
screen = turtle.Screen()
screen.title = 'U.S. States Game'

# Adding the U.S. map image to the turtle screen
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Converting the state column to a list for easy lookup
all_states = data.state.to_list()
guessed_states = []

# Game loop: keep asking for state names until 50 are guessed
while len(guessed_states) < 50:
    # Prompting user for the next state guess
    answer_state = screen.textinput(
        title=f'{len(guessed_states)}/50 | Guess the state',
        prompt="What's the next state?"
    )

    # Defensive check in case user closes the prompt
    if not answer_state:
        break

    capitalized_answer_state = answer_state.strip().title()  # normalize input

    # Exit conditiondd .

    if capitalized_answer_state == 'Exit':
        break

    # If the guess is correct and hasn't been guessed before
    if capitalized_answer_state in all_states and capitalized_answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()  # Hide the turtle cursor
        t.penup()       # Prevent drawing lines while moving

        # Get the state's x, y coordinates from the CSV
        state_data = data[data.state == capitalized_answer_state]
        t.goto(state_data.x.item(), state_data.y.item())

        # Write the guessed state on the map
        t.write(capitalized_answer_state)

        # Add to guessed list
        guessed_states.append(capitalized_answer_state)

# Generate a list of states that were not guessed
not_guessed = list(set(all_states) - set(guessed_states))

# Save unguessed states to a CSV file
not_guessed_csv = pandas.DataFrame(not_guessed)
not_guessed_csv.to_csv('Unanswered.csv')
