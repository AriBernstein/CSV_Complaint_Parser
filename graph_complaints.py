"""
Name: graph_complaints.py
Author: Ari Bernstein
Description: produces a bar graph of the number of complaints per state using Python Turtles.
Pre-conditions: utilities.py and state_complaints.py work correctly and are in same directory, csv files are in
subdirectory labeled 'data'
"""

from state_complaints import *
import turtle as t
import math

def axes(stateMap):
    """
    Finds the largest number of complaints per state and the number of states
    :param stateMap: (returned from make_state_map) A dictionary mapping upper case state abbreviation values to lists
    of Complaint objects originating in the state.
    :return: height(largest number of complaints for any state), number of states in stateMap
    """
    height = 0
    num_states = 0
    for key in stateMap:
        num_states += 1
        if len(stateMap[key]) > height:
            height = len(stateMap[key])
    return height, num_states

def drawYAxis(height):
    """
    Draws Y axis with increments according to its height
    :param height: max number of complaints per a given state
    :return: Not applicable, draws stuff
    """
    """rounds height down to the nearest 10s place"""
    height = (round(height, -2))

    """allows for y axis to height in 20 increments"""
    increment_per_complaint = (height/20)
    increments = int(round(height/increment_per_complaint))
    graphHeight = height/3 #setworldcoordinates takes care of scaling

    t.pendown()
    t.left(90)
    t.forward(graphHeight)
    t.penup()
    t.backward(graphHeight)
    level = 0
    for i in range(increments):
        level += increment_per_complaint
        t.forward(increment_per_complaint/3)
        t.pendown()
        t.left(90)
        t.forward(50)
        t.penup()

        t.right(90)
        t.forward(5)
        t.write(str(level))
        t.backward(5)
        t.left(90)

        t.backward(50)
        t.right(90)

    t.backward(graphHeight)
    t.right(90)

def drawGraph(num_states, statemap, height):
    """
    Draws entire graph apart from Y axis
    :param num_states: total number of states represented
    :param statemap: (returned from make_state_map) A dictionary mapping upper case state abbreviation values to lists
    of Complaint objects originating in the state.
    :param height: height(largest number of complaints for any state), number of states in stateMap
    :return: Not applicable - draws stuff
    """
    t.pendown()
    state_abrevs = []
    for key in statemap:
        state_abrevs.append(key)

    state_abrevs.sort() # sorts list of state abbreviations alphabetically
    state_abrevs.remove(state_abrevs[0])

    t.forward(15 * num_states)
    t.backward(15 * num_states)
    t.width(5)

    for i in state_abrevs:
        """Draws bars in bar graph"""
        t.penup()
        t.forward(15)
        t.left(90)
        t.pendown()
        t.forward(len(statemap[i])/3)
        t.penup()
        t.backward(len(statemap[i])/3)
        t.right(90)
    t.width(1)
    t.backward(15 * (num_states -2))
    count = 0

    t.penup()

    increment_per_state = (height/3)/35

    for i in state_abrevs:
        """Draws states below graph"""
        t.right(90)
        t.forward(increment_per_state)
        t.write(i)
        t.left(90)
        t.forward(15)
        count += 1
        if count == 4:
            t.left(90)
            t.forward(increment_per_state * 4)
            t.right(90)
            count = 0

    t.backward(15 * num_states)


def init(height, num_states):
    """Initiates starting point, speed, and world coordinates of graph"""
    # Sets screen aspect ratio depending on size of graph
    t.speed(0)
    t.penup()
    t.goto(-num_states, height/20)

def main():
    stateMap = make_state_map(read_complaint_data(getFilePath()))
    height, num_states = axes(stateMap)
    init(height, num_states)
    drawYAxis(height)
    drawGraph(num_states, stateMap, height)
    print("Please close the canvas to quit.")
    t.done()


if __name__ == '__main__':
    main()