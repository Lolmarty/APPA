# import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import json


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

jsonSource = "C:\git\embarrasment 4.25\Intermediate\ProjectFiles\HARDCODEISHARD"
with open(jsonSource) as file:
    a = json.load(file)
heads = [i['head'] for i in a]
handsL = [i['hand_l'] for i in a]
handsR = [i['hand_r'] for i in a]

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)

ax1.plot([i["x"] for i in handsR])
ax1.set_title("headX")
ax2.plot([i["y"] for i in handsR])
ax2.set_title("headY")
ax3.plot([i["z"] for i in handsR])
ax3.set_title("headZ")
ax4.plot([i["Roll"] for i in handsR])
ax4.set_title("headRoll")
ax5.plot([i["Pitch"] for i in handsR])
ax5.set_title("headPitch")
ax6.plot([i["Yaw"] for i in handsR])
ax6.set_title("headYaw")
plt.show()
