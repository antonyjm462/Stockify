import json
import csv
dict_list = []
from datetime import date
today = date.today()
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys, getopt

def csv_return():
    file = BASE_DIR+"/dashboard/data/"+str(today)+".csv"
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
    # print("\n\n return csv")
    # print(csv_rows)
    return csv_rows


#Read CSV File
def read_csv(file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        print(csv_rows)
        for data in csv_rows:
            print(data['High'])
        return (json.dumps(csv_rows))
        
def dataparse():
    input_file = BASE_DIR+"/dashboard/data/"+str(today)+".csv"
    json_data = read_csv(input_file)
    print(json_data)
    return json_data
    

def main():
    dataparse()



if __name__ == "__main__":
    main()