# About
Consider the following popular logistic issue: there are cities connected by a network roads (the lengths of all roads are known), need to find minimal distance between each pair. This problem is usually solved by using graph theory or dynamic programming methods. The method proposed in this application based on constructing a final sequence of matrixes of distances between cities, and the last matrix describes the length of shortest paths (along roads) between cities. That method was published by N.N.Rachkovsky.
So, we have path to initial matrix in numpy binary format. Lets name cities like C1, C2 ..., Сn and consider a square symmetric n × n-matrix D0 with lengths of available roads between cities. In other words, the element dij of this matrix is equal to the length of the road between the cities Сi  and Cj in the case when there is such a road, and zero for otherwise case. Among the properties of the matrix D0, we note that it. Besides addition, all elements dij where i=j of this matrix are equal to zero, since there is no road connecting any city with itself. To the matrix D0 lets apply following operation: for each pair Сi, Сj will try to find all cities Сk which related by roads with both cities Ci  and Cj, so we will find all routes leading from the city of Ci  to the city Сj  through any third city. Then we calculate the lengths of all these hops, and among these lengths including possibly direct route from the city Ci to the city Сj, choose the minimum.  
For the matrix D0 we construct the corresponding matrix of hops R0 where rij is equal to 0 (if dij of the matrix D0 is equal to zero) or 1. For each pair of cities Ci, Cj where i  < j and for every third city Ck we will calculate the value: rjk * dik + rik * djk. From all these numbers we compose a symmetric  n × n-matrix D1. The matrix D1 indicates the lengths of the shortest routes between cities explored at the first stage of solving the problem. Repeat that procedure while matrixes  Dn+1 and Dn are not equal.

# Run
For example will use path to 'matrix_distance' binary file as initial matrix:
```
from matrix_distance_searcher import RachkovskySearcher
searcher = RachkovskySearcher()
s('matrix_distance')
```
