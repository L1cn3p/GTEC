import csv
import os
import pickle

# 1) Count words in a text file 
file = "lorem.txt"
my_word = "lorem"

with open(file, 'r') as f:
    old_data = f.read()
    print(len([word for word in old_data.split(' ') if my_word in word.lower()]))

# 2) replace a word with another word
new_data = old_data.replace('Lorem', 'foo')

with open(file, 'w') as f:
    f.write(new_data)

# 3) put data in csv
file_exists = os.path.isfile("this_file.csv")
values = {}
# values['student name'] = input("Enter student name: ")
# values['course'] = input("Enter course: ")
# values['fees'] = input("Enter fees: ")
# values['GST'] = round((float(values['fees'])*0.14),2)
# values['Total Fees'] = int(values['fees'])+float(values['GST'])


with open("this_file.csv", "a") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['student name','course','fees','GST','Total Fees'])
    if not file_exists:
        writer.writeheader()
    if values:
        writer.writerow(values)

# 4) csv to console
with open('this_file.csv') as f:
    print(f.read())
    
# 5) patient class
class Patient():
    def __init__(self):
        self.name = input("Patient name: ")
        self.contact = input("Patient contact: ")
        self.address = input("Patient address: ")
        self.complaint = input("Patient complaint: ")

    def cured(self):
        self.complaint = None
        print("Patient is cured")

    def complain(self, complaint):
        self.complaint = complaint

# my_patient = Patient()
# print(vars(my_patient))
# my_patient.cured()
# print(vars(my_patient))
# my_patient.complain("Back Pain")
# print(vars(my_patient))

# 6) Pickle
# with open("binary.dat", "wb") as f:
#     pickle.dump(my_patient, f)

# with open("binary.dat", "rb") as f:
#     data = pickle.load(f)
#     print(vars(data))

# 7 & 8) list all files in a dir the a given extension
extension = input("Input a file extension (eg. .py or .jpg): ")
for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith(str(extension)):
             print(os.path.join(root, file))

