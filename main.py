import turtle
import csv
import pandas
import rules

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

statefile = pandas.read_csv("50_states.csv")

statefile["x"] = statefile["x"].astype(int)
statefile["y"] = statefile["y"].astype(int)

gameison = True
guessstate = "Guess the state"
popo = rules.Write()

while gameison:
    popo.Ask()
    for state in statefile["state"]:
        if popo.stet == state:
            print(state)
            xe = statefile[statefile["state"] == state]
            x = int(xe.x)
            ye = int(xe.y)
            popo.Go(x, ye, state)
            popo.Score()


turtle.mainloop()
# x = state["x"].astype(int)
# y = int(state["y"])
# print(y)
#print(statefile)