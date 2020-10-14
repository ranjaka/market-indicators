# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  ----------------------------------------------------------------

# Read data from csv but only "Price" column for now
rawData = pd.read_csv("data/APT Historical Data.csv", usecols=["Date","Price"])

# Setting date as index
rawData["Date"] = pd.to_datetime(rawData.Date, format='%b %d, %Y')
rawData.index = rawData["Date"]

# Sorting data in ascending order using Date
rawDataAsc = rawData.sort_index(ascending=True,axis=0)

# Creating a new dataframe with the dimensions of rawData
modelInputs = pd.DataFrame(index=range(0,len(rawDataAsc)), columns=["Price"])

for i in range(0,len(rawDataAsc)):
    modelInputs["Price"][i] = rawDataAsc["Price"][i]

# Period for indicator
period = 25
# Setting up training data
xInputs = []
# Build inputs for construcitng indicator
for i in range(period,len(modelInputs)-period):
    xInputs.append(modelInputs[i-period:i].values)

aroonUp, aroonDown = [], []
for i in range (0, len(xInputs)):

    # Aroon Up calculation
    up = (period - (period-np.where(xInputs[i] == np.amax(xInputs[i]))[0][0]))*(100/period)
    aroonUp.append(up)

    # Aroon Down calculation
    down = (period - (period-np.where(xInputs[i] == np.amin(xInputs[i]))[0][0]))*(100/period)
    aroonDown.append(down)

# Plotting
plt.plot(aroonUp[100:], color='green')
plt.plot(aroonDown[100:], color='red')
plt.ylabel('Aroon Strength in the scale 0 - 100')
plt.grid(True)
plt.show()














