import csv
with open("emails.csv", 'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    for item in emails:
        wr.writerow([item,])
