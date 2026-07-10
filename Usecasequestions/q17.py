class MatrixGraph:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.matrix = []
        for i in range(num_cities):
            row = []
            for j in range(num_cities):
                row.append(0)
            self.matrix.append(row)
        self.cities = {}
        self.index = 0
        
    def add_city(self, city):
        if city not in self.cities:
            self.cities[city] = self.index
            self.index += 1
            
    def add_edge(self, city1, city2):
        idx1 = self.cities[city1]
        idx2 = self.cities[city2]
        self.matrix[idx1][idx2] = 1
        self.matrix[idx2][idx1] = 1
        
    def display(self):
        for row in self.matrix:
            print(row)

g = MatrixGraph(3)
g.add_city("Mumbai")
g.add_city("Pune")
g.add_city("Delhi")

g.add_edge("Mumbai", "Pune")
g.add_edge("Mumbai", "Delhi")

g.display()