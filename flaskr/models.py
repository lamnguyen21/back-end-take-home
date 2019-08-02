from collections import defaultdict

# Routes holds possible routes from A to B
class Routes(object):

    def __init__(self):
        self.routes = defaultdict(list)

    def add_route(self, start, end, airline_id):
        self.routes[start].append((end, airline_id))

    def get_routes_from(self, start):
        return self.routes[start]
