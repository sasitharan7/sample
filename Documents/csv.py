import csv

with open('sasi.csv','r') as csv_file:
   csv_read = csv.reader(csv_file)
   for line in csv_read:
       print(line)
