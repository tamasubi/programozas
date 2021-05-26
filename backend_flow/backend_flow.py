import csv

class Employee():

    def __init__(self, name, status, salary, expectedSalary, numberOfMonths):
        self.name = name
        self.status = status
        self.salary = salary
        self.expectedSalary = expectedSalary
        self.numberOfMonths = numberOfMonths

    @classmethod
    def importFromCsv(cls, filename):
        with open("data_sources/" + filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)





Employee.importFromCsv("input.csv")