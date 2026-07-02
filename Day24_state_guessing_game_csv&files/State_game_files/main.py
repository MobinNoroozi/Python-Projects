# Import required libraries
import turtle
import pandas

# Create and configure the screen
screen = turtle.Screen()
screen.title("US State Game")

# Set up the background image (blank US map)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load state data from CSV file (contains state names and x, y coordinates)
data = pandas.read_csv("./50_states.csv")

# Create a list of all state names for validation
all_state_list = data.state.to_list()

# Initialize list to track correctly guessed states
guessed_states = []

# Main game loop - continues until all 50 states are guessed
while len(guessed_states) < 50:
    # Prompt user for a state name and display progress
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is another state name? Or Exit").title()

    # Handle exit condition - save missed states to a file for later study
    if answer_state == "Exit":
        missed_states = []
        # Find all states that were not guessed
        for state in all_state_list:
            if state not in guessed_states:
                missed_states.append(state)

        # Create a CSV file with the missed states
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    

    # Check if the guessed state is valid
    if answer_state in all_state_list:
        # Add the correct guess to the list
        guessed_states.append(answer_state)
        # Create a new turtle to display the state name on the map
        t = turtle.Turtle()
        t.hideturtle()  # Hide the turtle cursor
        t.penup()  # Prevent drawing lines
        # Retrieve the coordinates for the guessed state from the CSV data
        state_data = data[data.state == answer_state]
        # Move turtle to the state's location and write the state name
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

# Keep the window open until user clicks to close it
screen.exitonclick()
