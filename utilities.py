"""
Name: utilities.py
Author: Ari Bernstein
Description: This file contains a set of utilities which includes classes and functions used by the other
program tasks.
-Complaint class holds all data for each complaint
-read_complaint_data populates instances of class from spreadsheets
Pre-condition: csv files containing data for Complaint class instances are in subdirectory called 'data'
"""

from rit_lib import *
import csv
import time

class Complaint(struct):
    """
    Class containing all data in a given complaint. Data is read from rows in a spreadsheet using read_complaint_data function
    """
    _slots = ((str, "Date_received"), (str, "Product"), (str, "Sub_product"), (str, "Issue"), (str, "Sub_issue"),
              (str, "Consumer_complaint_narrative"), (str, "Company_public_response"),
              (str, "Company"), (str, "State"), (str, "ZIP_code"), (str, "Tags"), (str, "Consumer_consent_provided"),
              (str, "Submitted_via"), (str, "Date_sent_to_company"), (str, "Company_response_to_consumer"),
              (str, "Timely_response"), (str, "Consumer_disputed"), (str, "Complaint_ID"))


def read_complaint_data(filepath):
    """
    Populates instances of complaint data from inputted CSV files.

    :param filepath: A string, giving the path name of a CSV data file.

    :return: A dictionary mapping integer complaint ID values to unique Complaint ob- jects. For every ID, there is
    exactly one Complaint object. The function should preserve the case of all field content characters in each
    Complaint instance. See the examples.

    printed output:  timed file reading loop to understand the effort required to process the file. Prints the following
    as it does its work:
    • a message at the start of reading;
    • report of the total number of entries read;
    • elapsed time of reading the file; and
    • a message reporting the end of reading.
    """
    complaintDict = {}
    startTime = time.time()

    print("Reading " + filepath)

    with open(filepath) as csv_file:
        """opens csv file using csv module - this handles all otherwise invalid characters and oddly placed quotations
        and commas"""
        read_csv_file = csv.reader(csv_file, delimiter = ",")

        # print(read_csv_file)
        notHeadingRow = False
        for row in read_csv_file:
            """Loops through file (except for heading -first row- and builds instance of class. Adds to dictionary)"""
            if notHeadingRow == False:
                for i in row:
                    """in heading (first row of csb), replaces spaces, dashes with underscores
                    and removes question marks)"""
                    new_string = i.replace("-", "_")
                    new_string = new_string.replace(" ", "_")
                    new_string = new_string.replace("?", "")
                    row[row.index(i)] = new_string
                notHeadingRow = True

            elif notHeadingRow == True:
                complaintDict[int(row[17])] = Complaint(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                                   row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15],
                                                   row[16], row[17])
    endTime = time.time()
    totalTime = endTime - startTime

    print("Total entries: " + str(len(complaintDict)))
    print("Time elapsed: " + str(totalTime) + " seconds.")
    print("Reading complete.")
    return complaintDict

def dataFromPhrase(phrase, dictionary):
    """
    returns classes whose phrase appears in the product slot of a complaint class instance
    :param phrase: phrase which might appear in product of complaint class instance
    :param dictionary: dictionary of complaints from read_complaint_data
    :return: Not applicable
    printed output: Complaint_ID, Product, Company, and State if complaint class instance's company matches the phrase
    """
    results = []
    phrase = phrase.strip()
    # phrase = str.lower(phrase)

    for key in dictionary:
        if phrase.strip() == "":
            return "Phrase is empty."

        else:
            dictionary[key].Product = str.lower(dictionary[key].Product)

            if phrase in dictionary[key].Product:
                tempProduct = dictionary[key].Product.split()
                for i in tempProduct:
                    if i == phrase:
                        results.append(str(dictionary[key].Complaint_ID) + ",  " + dictionary[key].Product.title() + ", " +
                        dictionary[key].Company + ", " + dictionary[key].State)
    if results != []:
        for i in results:
            print(i)
    else:
        print(phrase + " does not appear in product name.")

def returnClassFromID(dictionary, id):
    """
    returns complaint class instance given class' ID
    :param dictionary: dictionary of complaints from read_complaint_data
    :param id: complaint ID as string or int
    :return: instance of class associated with class ID
    """
    if id == "":
        print("Complaint ID field is empty.")
        return None
    else:
        id = int(id)
        for key in dictionary:
            if key == id:
                return dictionary[key]

def getFilePath():
    """helper function to append CSV filname to its subdirectory, ./data/..."""
    filePath = "./data/" + input("Enter the dataset file: ")
    return filePath

def main():
    complaints = read_complaint_data(getFilePath())
    productPhraseList = []

    productPhrase = input("Enter Product phrase or press ENTER key to stop: ")
    while productPhrase != "":
        productPhraseList.append(productPhrase)
        productPhrase = input("Enter Product phrase or press ENTER key to stop: ")

    for i in productPhraseList:
        dataFromPhrase(i, complaints)

if __name__ == '__main__':
    main()