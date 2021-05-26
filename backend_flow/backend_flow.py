import csv

employees = []

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
            reader = csv.reader(file, delimiter =';')
            for row in reader:
                employee = cls(row[0], row[1], row[2], row[3], row[4])
                employees.append(employee)





Employee.importFromCsv("input.csv")
print(employees)