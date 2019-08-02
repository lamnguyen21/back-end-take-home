from .models import Routes

'''
    RoutesLoader loads routes from a csv data source
'''
class RoutesLoader(object):

    def load(self, csv_path):
        routes = Routes()

        file = open(csv_path, 'r')
        if file.mode == 'r':
            header = True
            for line in file:
                if header:
                    header = False
                    continue
                splits = line.split(',')
                routes.add_route(splits[1].strip(), splits[2].strip(), splits[0].strip())

        return routes


