import csv

class HandleCSV:
    filename = "employees.csv"

    @classmethod
    def GetData(cls):
        """classmethod returns csv to list of dictionary format"""
        l1 = []

        with open(cls.filename, mode='r') as f:
            data = csv.DictReader(f)
            for row in data:
                l1.append(dict(row))
            return (l1)


    @classmethod
    def read_entire_csv(cls):

        with open(cls.filename, "r") as foo:
            return foo.readlines()

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()

    @classmethod
    def convert(cls):
        Dict = {}
        with open(cls.filename) as bar:
            for line in bar:
                key,val = line.split()
                Dict[key] = val
            print(Dict)
