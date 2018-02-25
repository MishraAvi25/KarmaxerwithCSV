import csv
from Title_Counter import all_titles
from Hour_Cutter import all_hours

myData = [[all_titles()],[all_hours()]]

myFile = open('TheData.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)