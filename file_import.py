from controller import *
import csv
       
def line_formatter(input):
    if (len(input) == 3):
        return (input[0], (input[1], float(input[2])))
    else:
        print("Malforned line item passed to line_formatter")

def import_csv(target_file = 'datafiles\LakeO_AmmoniaReports.csv'):
    with open(target_file, newline='') as csvfile:
        active_reader = csv.reader(csvfile, delimiter=',')
        for row in active_reader:
            formatted = line_formatter(row)
            insert_data(formatted[0], formatted[1])
    print(dataStorage)
            
import_csv()