from collections import deque

import heapq

class Station:
    def __init__(self, name):
        self.name = name
        self.connections: dict[Station, int] = {}

    def __eq__(self, other):
        return isinstance(other, Station) and self.name == other.name

    def __hash__(self):
        return hash(self.name)
        
    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f"Station({self.name})"
        
    def add_connection(self, station: Station, fare: int) -> None:
        self.connections[station] = fare

    def connect(station_a: Station, station_b: Station, fare: int):
        """Connect two stations together adding a fare to the edge weight"""
        station_a.add_connection(station_b, fare)
        station_b.add_connection(station_a, fare)

def dijkstra(start):
    # Stores the cheapest known fare from start to each station
    cheapest_fares = {start: 0}

    # For each station, the previous station on the cheapest route
    previous_station = {}

    # Stations we have fully processed
    visited = set()

    # Min-heap ordered by fare
    pq = [(0, start)]

    while pq:
        # Pop the unvisited station with the lowest known fare
        # This is the greedy choice
        current_fare, current = heapq.heappop(pq)

        # Skip station if we've already processed it
        if current in visited:
            continue
        visited.add(current)

        for neighbour, fare in current.connections.items():
            if neighbour in visited:
                continue

            # Cost to reach this neighbour via the current station
            new_fare = current_fare + fare

            # Update if this is the cheapest route we've found to a neighbour
            # or the first time we encounter a neighbour
            if (
                neighbour not in cheapest_fares
                or new_fare < cheapest_fares[neighbour]
            ):
                cheapest_fares[neighbour] = new_fare
                previous_station[neighbour] = current
                heapq.heappush(pq, (new_fare, neighbour))

    return cheapest_fares, previous_station

def shortest_route(start, destination):
    cheapest_fares, previous_station = dijkstra(start)

    route = []
    current = destination

    while current is not None:
        route.append(current.name)
        current = previous_station.get(current)

    route.reverse()

    fare = cheapest_fares.get(destination, None)
    
    print(f"Route: {' - '.join(route)}")
    print(f"Total fare: £{fare}")

manchester = Station("Manchester")
sheffield = Station("Sheffield")
london = Station("London")
leeds = Station("Leeds")
birmingham = Station("Birmingham")
bristol = Station("Bristol")

Station.connect(sheffield, london, 30)
Station.connect(bristol, london, 25)
Station.connect(birmingham, london, 22)
Station.connect(manchester, london, 55)
Station.connect(leeds, london, 45)

Station.connect(birmingham, bristol, 30)

Station.connect(manchester, birmingham, 28)
Station.connect(sheffield, birmingham, 15)

Station.connect(leeds, manchester, 12)
Station.connect(sheffield, manchester, 10)

Station.connect(leeds, sheffield, 8)

shortest_route(london, manchester)
# Route: London - Sheffield - Manchester
# Total fare: £40

'''
Exercise 1

    York Addition
'''

york = Station("York")

Station.connect(york, leeds, 5)
Station.connect(york, sheffield, 14)

'''
Exercise 2

    York Route
'''

shortest_route(london, york)
# Route: London - Sheffield - Leeds - York
# Total fare: 43