import time
import csv


class LogWriter:
    csvFile = open('names.csv', newline='')
    timestamp = time.time()
    fieldnames = ['event', 'time']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)

    def __init__(self) -> None:
        super().__init__()
        self.writer.writeheader()

    def toTxt(self, string, timestamp):
        self.writer.writerow({'first_name': string, 'last_name': timestamp})
