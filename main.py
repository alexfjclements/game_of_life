import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import calculations as calc

print("Welcome to the Game of Life!")
print("The game takes place on a square 100x100 grid.")
GridSize = int(100)

# Initialise arrays with correct dimensions
current = np.empty([GridSize, GridSize], dtype=bool)


# Initialize useful variables
newXY = 0

# Define cell update function
def Update(data):

    global current
    global newXY
    global GridSize

    update = current.copy()

    for y in range(GridSize):

        for x in range(GridSize):

            gridsize = GridSize - 1

            # Initialize other variables

            xMinOne = x - 1
            xPlusOne = x + 1
            yMinOne = y - 1
            yPlusOne = y + 1

            # Set boundary conditions
            if xMinOne < 0:
                xMinOne = gridsize

            if xPlusOne > gridsize:
                xPlusOne = 0

            if yMinOne < 0:
                yMinOne = gridsize

            if yPlusOne > gridsize:
                yPlusOne = 0

            SurroundSumBottom = sum(current[[xMinOne], [yMinOne]]) + sum(current[[x], [yMinOne]]) + sum(current[[xPlusOne], [yMinOne]])
            SurroundSumMiddle = sum(current[[xMinOne], [y]]) + sum(current[[xPlusOne], [y]])
            SurroundSumTop = sum(current[[xMinOne], [yPlusOne]]) + sum(current[[x], [yPlusOne]]) + sum(current[[xPlusOne], [yPlusOne]])

            SurroundSum = SurroundSumTop + SurroundSumMiddle + SurroundSumBottom

            if current[[x], [y]] == True:

                if SurroundSum in range(0,1):
                    newXY = False
                    update[[x], [y]] = newXY

                elif SurroundSum in range(2,3):
                    newXY = True
                    update[[x], [y]] = newXY

                elif SurroundSum > 3:
                    newXY = False
                    update[[x], [y]] = newXY

            elif current[[x], [y]] == False:

                if SurroundSum == 3:
                    newXY = True
                    update[[x], [y]] = newXY




    mat.set_data(update)
    current = update

    return [mat]

# Populate Array

for y in range(GridSize):

    for x in range(GridSize):
        i = calc.RandPop()
        i = i.Pop()

        current[[x], [y]] = i



# set up animation
fig, ax = plt.subplots()
mat = ax.matshow(current)
ani = animation.FuncAnimation(fig, Update, interval=50, save_count=50)
plt.show()