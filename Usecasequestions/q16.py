class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, city1, city2):
        if city1 not in self.graph:
            self.graph[city1] = []
        if city2 not in self.graph:
            self.graph[city2] = []
            
        self.graph[city1].append(city2)
        self.graph[city2].append(city1)
        
    def display(self):
        for city in self.graph:
            print(city, "->", self.graph[city])

city_map = Graph()
city_map.add_edge("Mumbai", "Pune")
city_map.add_edge("Mumbai", "Delhi")
city_map.add_edge("Pune", "Hyderabad")

city_map.display()