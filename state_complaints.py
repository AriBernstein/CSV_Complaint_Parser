"""
Name: state_complaints.py
Author: Ari Bernstein
Description:  Organizes all the complaints according to the state in which they were reported.
Pre-condition: utilities.py and display_complaints.py work correctly and are in same directory, csv files are in
subdirectory labeled 'data'
"""

from utilities import *
import display_complaints

def make_state_map(dataset):
    """
    Builds a dictionary organizing complaint objects by state

    :param dataset: (returned from read_complaint_data in utilities.py) a dictionary whose keys are complaint IDs and
    values are the associated instance of the complaint class

    :return:A dictionary mapping upper case state abbreviation values to lists of
    Complaint objects originating in the state.
    """
    stateDict = {}
    for key in dataset:
        if not dataset[key].State in stateDict:
            stateDict[dataset[key].State] = [dataset[key]]
        else:
            stateDict[dataset[key].State].append(dataset[key])
    return stateDict

def list_state_complaints(statemap):
    """

    :param statemap: (returned from make_state_map) A dictionary mapping upper case state abbreviation values to lists
    of Complaint objects originating in the state.
    :return: Not applicable
    printed output: A list of the number of complaints by state. The list is sorted from the largest
    number to the smallest number.
    """
    sortedBySize = []
    for key in statemap:
        sortedBySize.append([key, len(statemap[key])])

    """Sorts by number of complaints per state"""
    sortedBySize = sorted(sortedBySize, key = lambda x: int(x[1]), reverse = True)

    for i in sortedBySize:
        if i[0] == "":
            i[0] = "Undefined"
        print(i[0] + " :   " + str(i[1]) + " entries.")

    #return sortedBySize # (so that we can access the list if we want)


def query_state_complaints(statemap, statelist, max_count=10):
    """
    Allows one to search for complaints by given states (in a list of strings representing state abbreviations)

    :param statemap: (returned from make_state_map) A dictionary mapping upper case state abbreviation values to lists
    of Complaint objects originating in the state.

    :param statelist: A list of upper case state abbreviation values.

    :param max_count: A number limiting the number of complaints to show per state. Because there may be hundreds of
    complaints. the max_count is an optional parameter. If it is not given an argument value, the default maximum is 10.
     A number limiting the number of complaints to show per state.

    :return: Not applicable

    Printed output: For every valid state in the state list, pretty print the first max count number of entries, stopping
    if there are fewer entries in the map than requested. Print “: no entries” after an invalid state name, and
    precede each valid entry with a line of text which contains that entry’s count in square brackets, the state name,
    and a line of 30 ‘=’ characters as shown in the examples.
    """
    for key in statemap:
        for i in statelist:
            if i == key:
                count = 0
                for complaint in statemap[key]:
                    if count != max_count:
                        print('[ ' + str(count+1) + ' ]  ' + i + "  ==============================")
                        display_complaints.display_complaint(complaint)
                        count += 1
                        print('\n')


def main():
    newStateMap = make_state_map(read_complaint_data(getFilePath()))
    list_state_complaints(newStateMap)

    stateList = []
    i = (input(str.upper("Enter State (e.g. NY) or press ENTER key to stop: ")))
    stateList.append(str.upper(i))
    while i is not "":
        i = (input(str.upper("Enter State (e.g. NY) or press ENTER key to stop: ")))
        if i is not "":
            stateList.append(str.upper(i))

    count = input("Enter how many to display or press ENTER to see 10 entries: ")
    if count is not "":
        query_state_complaints(newStateMap, stateList, int(count))
    else:
        query_state_complaints(newStateMap, stateList)


if __name__ == '__main__':
    main()


# newStateMap = make_state_map(read_complaint_data("./data/Short-05k.csv"))
# query_state_complaints(newStateMap, ["NY", "MN"], 3)