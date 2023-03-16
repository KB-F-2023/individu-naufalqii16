import random
import math

# Define some constants
CITY_COORDINATES = [
    (60, 200),
    (180, 200),
    (80, 180),
    (140, 180),
    (20, 160),
    (100, 160),
    (200, 160),
    (140, 140),
    (40, 120),
    (100, 120),
    (180, 100),
    (60, 80),
    (120, 80),
    (180, 60),
    (20, 40),
    (100, 40),
    (200, 40),
    (20, 20),
    (60, 20),
    (160, 20)
]
POPULATION_SIZE = 100
NUM_GENERATIONS = 1000
MUTATION_RATE = 0.01

# Define the City class
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, city):
        x_distance = abs(self.x - city.x)
        y_distance = abs(self.y - city.y)
        distance = math.sqrt((x_distance ** 2) + (y_distance ** 2))
        return distance

# Define the Route class
class Route:
    def __init__(self, cities):
        self.cities = cities
        self.distance = self.calculate_distance()

    def calculate_distance(self):
        distance = 0
        for i in range(len(self.cities)):
            from_city = self.cities[i]
            to_city = None
            if i + 1 < len(self.cities):
                to_city = self.cities[i + 1]
            else:
                to_city = self.cities[0]
            distance += from_city.distance_to(to_city)
        return distance

# Define the Population class
class Population:
    def __init__(self, size):
        self.routes = []
        for i in range(size):
            new_route = Route(random.sample(cities, len(cities)))
            self.routes.append(new_route)
        self.routes.sort(key=lambda x: x.distance)

    def crossover(self, parent1, parent2):
        gene1 = random.randint(0, len(parent1.cities) - 1)
        gene2 = random.randint(0, len(parent1.cities) - 1)
        start_gene = min(gene1, gene2)
        end_gene = max(gene1, gene2)
        child_cities = [city for city in parent1.cities[start_gene:end_gene]]
        for city in parent2.cities:
            if city not in child_cities:
                child_cities.append(city)
        return Route(child_cities)

    def mutate(self, route):
        index1 = random.randint(0, len(route.cities) - 1)
        index2 = random.randint(0, len(route.cities) - 1)
        route.cities[index1], route.cities[index2] = route.cities[index2], route.cities[index1]
        route.distance = route.calculate_distance()

    def evolve(self):
        elite_size = int(len(self.routes) * 0.2)
        elite_routes = self.routes[:elite_size]

        selection_probs = [1 / r.distance for r in self.routes]
        total_probs = sum(selection_probs)
        normalized_probs = [p / total_probs for p in selection_probs]

        new_routes = elite_routes

        while len(new_routes) < len(self.routes):
            parent1, parent2 = random.choices(self.routes, weights=normalized_probs, k=2)
            child = self.crossover(parent1, parent2)
            if random.random() < MUTATION_RATE:
                self.mutate(child)
            new_routes.append(child)

        new_routes.sort(key=lambda x: x.distance)
        self.routes = new_routes

if __name__ == '__main__':
    cities = [City(x, y) for x, y in CITY_COORDINATES]
    population = Population(POPULATION_SIZE)

    for i in range(NUM_GENERATIONS):
        print(f"Generation {i} - Best distance: {population.routes[0].distance}")
        population.evolve()

    print(f"Final distance: {population.routes[0].distance}")

