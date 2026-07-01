import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")

all_state_list = data.state.to_list()


guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is another state name? Or Exit").title()

    if answer_state == "Exit":
        missed_states = []
        for state in all_state_list:
            if state not in guessed_states:
                missed_states.append(state)

        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    

    if answer_state in all_state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

screen.exitonclick()