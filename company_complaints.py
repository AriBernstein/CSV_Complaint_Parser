"""
Name: company_complaints.py
Author: Ari Bernstein
Description: Organizes complaints by the company against which the complaint was filed. Then computes
and prints statistics, and lists the complaints of the top offending companies.

Pre-condition: utilities.py and display_complaints.py work correctly and are in same directory, csv files are in
subdirectory labeled 'data'
"""

from utilities import *
from display_complaints import *

def make_company_map(dataset):
    """
    A dictionary mapping integer complaint ID values to unique Complaint objects.
    :param dataset: (returned from read_complaint_data in utilities.py) a dictionary whose keys are complaint IDs and
    values are the associated instance of the complaint class

    :return: A dictionary mapping each company name value to a dictionary mapping each product value to lists of
    Complaint objects related to the company and product.
    """
    companyDict = {}
    for key in dataset:
        """iterates through every single complaint"""
        if dataset[key].Company not in companyDict:
            """Takes complaint, if the company is not in companyDict, add company as key and product as value, product
            is the key to its own dictionary, its value being a list containing the complaint class from which it is derived"""
            companyDict[dataset[key].Company] = {dataset[key].Product : [dataset[key]]}
        else:
            """If company is in companyDict as a key, but key does not have its product as a value, adds new product.
            Key to product is a list containing the complaint class from which it is derived. If product exists,
            appends complaint class to list which already exists"""
            if dataset[key].Product not in companyDict[dataset[key].Company]:
                companyDict[dataset[key].Company][dataset[key].Product] = [dataset[key]]
            else:
                companyDict[dataset[key].Company][dataset[key].Product].append(dataset[key])
    return companyDict


def make_company_map_for_stats(dataset):
    """Accidentally wrote make_company_map the wrong way and only realized after having written compute_statistics.
    Functions as a helper fucntion to compute_statistics

    :param dataset: (returned from read_complaint_data in utilities.py) a dictionary whose keys are complaint IDs and
    values are the associated instance of the complaint class

    :return: A dictionary whose keys are states and values are lists of complaints from those states.
    """
    companyDict_for_Stats = {}
    for key in dataset:
        if not dataset[key].Company in companyDict_for_Stats:
            companyDict_for_Stats[dataset[key].Company] = [dataset[key]]
        else:
            companyDict_for_Stats[dataset[key].Company].append(dataset[key])
    return companyDict_for_Stats


def make_product_map(dataset):
    """Similarly to 'make_company_map_for_stats', acts as helper function to compute_statistics.

    :param dataset: (returned from read_complaint_data in utilities.py) a dictionary whose keys are complaint IDs and
    values are the associated instance of the complaint class

    :return: A dictionary whose keys are products and values are lists of complaints from those products.
    """
    productDict = {}
    for key in dataset:
        if not dataset[key].Product in productDict:
            productDict[dataset[key].Product] = [dataset[key]]
        else:
            productDict[dataset[key].Product].append(dataset[key])
    return productDict


def compute_statistics(dataset):
    """

    :param dataset:(returned from read_complaint_data in utilities.py) a dictionary whose keys are complaint IDs and
    values are the associated instance of the complaint class
    :return: Not applicable
    :printed output: Print a report of basic statistics on the dataset.
    """
    companyMap = make_company_map_for_stats(dataset)
    productMap = make_product_map(dataset)

    worstCompany = [0, None]
    totalComplaints = 0
    totalCompanies = 0

    totalProducts = 0
    worstProduct = [0, None]

    medianlist = []

    for key in companyMap:
        """
        populates:
        totalCompany list
        worstCompany list
        medianlist
        """
        totalCompanies += 1
        totalComplaintsPerCo = 0

        for complaint in companyMap[key]:
            totalComplaintsPerCo += 1

        medianlist.append(totalComplaintsPerCo)
        totalComplaints += totalComplaintsPerCo

        if totalComplaintsPerCo > worstCompany[0]:
            worstCompany[0] = totalComplaintsPerCo
            worstCompany[1] = key

    for key in productMap:
        """
        Populates:
        totalProducts
        worstProduct
        """
        totalComplaintsPerProd = 0
        totalProducts += 1

        for complaint in productMap[key]:
            totalComplaintsPerProd += 1

        if totalComplaintsPerProd > worstProduct[0]:
            worstProduct[0] = totalComplaintsPerProd
            worstProduct[1] = key

    averageComplaintPerCo = totalComplaints/totalCompanies
    medianlist = sorted(medianlist)
    medianComplaints = medianlist[len(medianlist)//2]
    print(len(medianlist))
    worstCoPercent = '{:.3%}'.format(worstCompany[0]/totalComplaints)
    worstProdPercent = '{:.3%}'.format(worstProduct[0]/totalComplaints)

    print("\nStatistics: \nTotal Complaints: " + str(totalComplaints) + "\nTotal Companies: "+ str(totalCompanies)
          + "\nTotal Products: " + str(totalProducts) + "\n\nAverage Complaint Per Company: " +
          str(round(averageComplaintPerCo, 3)) + "\nMedian Number of Complaints Per Company: " +
          str(medianComplaints) + "\n\nMost Complained-About Company: " + worstCompany[1] + ': ' + str(worstCompany[0]) + ' (' + worstCoPercent + ') ' +
          "\nMost Complained-About Product: " + worstProduct[1] + ': ' + str(worstProduct[0]) + ' (' + worstProdPercent + ') ')



def getTotalComplaintsPerCo(companyDict, companyName):
    """Helper function to return number of complaints in regard to a company
    :param companyDict:
    :param companyName: company name as a string
    :return: (use make_company_map function) A dictionary mapping each company name value to a dictionary mapping each product value to lists of
    Complaint objects related to the company and product.
    """
    complaints = companyDict[companyName]
    totalComplaints = 0
    for key in complaints.keys():
        totalComplaints += len(complaints[key])
    return totalComplaints


def list_company_complaints(companymap, count=3):
    """

    :param companymap: A dictionary mapping company name values to a dictionary mapping product values to lists of
    Complaint objects related to the company and product. topnumber
    :param count: Number of complaints you would like to print per company (default is 3)
    :return: Not Applicable
    :printedOutput: The output has a heading ”Top < N > Companies” where the < N > is the number printed. The rest of
    the list prints summary information for the companies starting with the company with the largest number of
    complaints and proceeding to the next largest number, and so on.
    """
    print("\nTop " + str(count) + " Companies and their Complaints: ")

    list = []
    for key in companymap:
        """populates list of company names to be sorted"""
        val = (getTotalComplaintsPerCo(companymap, key))
        list.append([key, val])

#   newList = list.sort(key=lambda x: x[1])
    sorted_list = sorted(list, key=lambda x: x[1], reverse = True)
    """Sorts list by number of complaints per company"""

    for i in range(int(count)):
        """Handles printing"""
        print(sorted_list[i][0] + " : " + str(sorted_list[i][1]) + " complaints.")
        newKey = str(sorted_list[i][0])
        j = companymap[newKey]
        keys = j.keys()
        # print(keys)
        for l in keys:
            newk = str(l)
            print('\t\t\t' + str(len(j[newk])) + ' ' + newk + ' complaints.')

        print('')

def main():
    complaints = read_complaint_data(getFilePath())
    compute_statistics(complaints)
    companyMap = make_company_map(complaints)
    summaryCount = str(input("\nEnter number to change length of the summary(default=3) "))
    list_company_complaints(companyMap, summaryCount)


if __name__ == '__main__':
    main()
#
# map = read_complaint_data("./data/LongLines2.csv")
# coMap = make_company_map(map)
# list_company_complaints(coMap)