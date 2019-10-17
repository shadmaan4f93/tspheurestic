# TSP-Heuristic-solution

Heuristic approach provides a fast solution to tsp problem.The Quality of solution depends on the techniques we choose.There are various
techniques:
Greedy
2-opt
3-opt
nearest-neighbour
Research shows that L-k algorithm tends to give best solution within lower bound of Held-karper dynamic algorithm.And Helsgaun further
improved it with increasing its speed using opt tecniques.

This code uses L-K approach with 2-opt & 3-opt tecniques to make the tour calculation faster.

usage--------
python test.py

code flow:
first make edges using setedges()
At each iteration calculate a temp tour   
then uses opt-2 or opt-3 techniques to improve the tour

TSP.setEdges(matrixs)
initial_tour = KOpt(range(len(matrixs)))
path, cost = initial_tour.optimise()



