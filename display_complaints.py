"""
Name: company_complaints.py
Author: Ari Bernstein
Description: Prints contents of instances of complaint classes in a clear, concise, and pretty way.
Pre-conditions, utilities.py works correctly and is the in same directory, csv files are in
subdirectory labeled 'data'
"""

from utilities import *

def eightSpace(slotName, value):
    """
    Helper function print slot's name, indent first line of each slot's value, and print UNKNOWN if slot is empty
    :param slotName: Name of slot as string eg.Company, Product, State, etc.
    :param value: value of complaint slot
    :return: Not applicable
    """
    if value is not "":

        return slotName + "\n        " + value
    else:
        return slotName + " UNKNOWN"

def returnClassFromID(dictionary, id):
    """
    Helper function to return Complaint class instance given its ID
    :param dictionary: (returned from read_complaint_data in utilities.py) a dictionary whose keys are complaint IDs and
    values are the associated instance of the complaint class

    :param id: Complaint ID of a given Complaint Class as string or int

    :return:
    """
    if id == "":
        print("Complaint ID field is empty.")
        return None
    else:
        id = int(id)
        for key in dictionary:
            if key == id:
                return dictionary[key]
    print(str(id) + " is not in dataset.")


def formatChars(slot):
    """
    Formats long lines so that they stack every 67 characters
    :param slot: String from the value of a slot in an instance of complaint class
    :return: string formatted so that it has a newLine character every 67 characters
    """
    if slot is not '':
        slot = slot.split()
        line = ''
        fullString = ''
        for i in slot:
            if len(line) + len(i) < 66:
                line += i + ' '
            else:
                fullString += line + '\n' + (' ' * 8)
                line = ''
        fullString += line + (' ' * 8)
        return fullString
    else:
        return slot




def display_complaint(complaint):
    """

    :param complaint: instance of Complaint class
    :return: Not Applicable
    printed output: All data from an instance of the complaint class in a pretty manner
    """
    if complaint is not None:
        print(eightSpace("Date_received :", complaint.Date_received))
        print(eightSpace("Product :", formatChars(complaint.Product)))
        print(eightSpace("Sub_product :", formatChars(complaint.Sub_product)))
        print(eightSpace("Issue :", formatChars(complaint.Issue)))
        print(eightSpace("Sub_issue :", formatChars(complaint.Sub_issue)))
        print(eightSpace("Consumer_complaint_narrative :", formatChars(complaint.Consumer_complaint_narrative)))
        print(eightSpace("Company_public_response :", formatChars(complaint.Company_public_response)))
        print(eightSpace("Company :", formatChars(complaint.Company)))
        print(eightSpace("State :", complaint.State))
        print(eightSpace("ZIP_code :", complaint.ZIP_code))
        print(eightSpace("Tags :", formatChars(complaint.Tags)))
        print(eightSpace("Consumer_consent_provided :", complaint.Consumer_consent_provided))
        print(eightSpace("Submitted_via :", formatChars(complaint.Submitted_via)))
        print(eightSpace("Date_sent_to_company :", complaint.Date_sent_to_company))
        print(eightSpace("Company_response_to_consumer :", formatChars(complaint.Company_response_to_consumer)))
        print(eightSpace("Timely_response :", complaint.Timely_response))
        print(eightSpace("Consumer_disputed :", complaint.Consumer_disputed))
        print(eightSpace("Complaint_ID :", complaint.Complaint_ID))

    elif complaint is None:
        return
    else:
        print(str(complaint) + " not in dataset")


def main():
    complaintIDList = []
    filePath = "./data/" + input("Enter CSV file name: ")
    complaints = read_complaint_data(filePath)

    id = input("Enter a Complaint_ID (e.g. 13002) or press ENTER key to stop: ")
    complaintIDList.append(id)
    while id is not "":
        id = input("Enter a Complaint_ID (e.g. 13002) or press ENTER key to stop: ")
        if id is not "":
            complaintIDList.append(id)
    print("===================================================================")


    for i in complaintIDList:
        complaintInstance = returnClassFromID(complaints, i)
        display_complaint(complaintInstance)
        print("===================================================================")

if __name__ == '__main__':
    main()
