from collections import deque
from .errors import InvalidOriginError
from .errors import InvalidDestinationError

'''
    RoutesFinder uses BFS to compute the shortest path between the origin
    and the destination. As a result, the method find has time complexity
    O(V+E) where V is the number of airports and E the connections between them.
    Space complexity is O(V) since queue holds at most V airports in the worst case.
'''
class RoutesFinder(object):

    def __init__(self, routes, airports):
        self.routes = routes
        self.airports = airports

    def find(self, start, end):
        if not self.airports.has(start):
            raise InvalidOriginError(start)
        if not self.airports.has(end):
            raise InvalidDestinationError(end)

        bfs_queue = deque([(start, [])])
        seen = set([start])

        while bfs_queue:
            airport, path = bfs_queue.popleft()
            path.append(airport)

            if airport == end:
                return path

            for next_airport, _ in self.routes.get_routes_from(airport):
                if next_airport not in seen:
                    seen.add(next_airport)
                    bfs_queue.append((next_airport, path[::]))

        return []

