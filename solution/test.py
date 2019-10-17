
from data import matrixs
from base import TSP
from optimise import KOpt

names = [
    "Mumbai",
    "Delhi",
    "Bangalore",
    "Hyderabad",
    "Ahmedabad",
    "Surat",
    "Pune",
    "Kanpur",
    "Nagpur",
    "Bhopal",
    "Patna",
    "Chandigarh",
    "Noida"
    
]
# Load the distances
TSP.setEdges(matrixs)
initial_tour = KOpt(range(len(matrixs)))
path, cost = initial_tour.optimise()
print("Best path has cost: {}".format(cost))
print([names[i] for i in path])


