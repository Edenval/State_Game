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

newlist = statefile["state"].to_list()
print(newlist)
gameison = True
guessstate = "Guess the state"
popo = rules.Write()

statelist = []

while gameison:
    popo.Ask()
    if popo.stet == "Exit":
        popo.bye()
        #if state not in statelist:
         #   dictionar["State"] = state
        break

    for state in statefile["state"]:
        if popo.stet == state:
            xe = statefile[statefile["state"] == state]
            x = int(xe.x)
            ye = int(xe.y)
            popo.Go(x, ye, state)
            popo.Score()
            statelist.append(state)
            #state = state
            print(state)
            newlist.remove(state)
            print(newlist)


new_data = pandas.DataFrame(newlist)
new_data.to_csv("states_to_learn.csv")

# for state in statefile["state"]:
#     if state not in statelist:
#         diction["State"] = "state"

#states_to_learn.csv


turtle.mainloop()
# x = state["x"].astype(int)
# y = int(state["y"])
# print(y)
#print(statefile)