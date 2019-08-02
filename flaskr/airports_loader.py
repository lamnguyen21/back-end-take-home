from .airport_repository import AirportRepository

'''
    AirportsLoader loads airport data from a CSV data source
'''
class AirportsLoader(object):

    def __init__(self):
        pass

    def load(self, csv_path):
        airport_repo = AirportRepository()

        file = open(csv_path, 'r')
        if file.mode == 'r':
            header = True
            for line in file:
                if header:
                    header = False
                    continue
                splits = line.split(',')
                airport_repo.add(splits[3].strip())

        return airport_repo
