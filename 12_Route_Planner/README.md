# Route Planner

- `PYTHON` `2D ARRAY` `ALGORITHMIC THINKING` `GRAPHS` `NEW` `PUBLIC`
- Difficulty: Hard
- Duration: 30min

As a part of the route planner, the route_exists method is used as a quick filter if the destination is reachable, before using more computationally intensive procedures for finding the optimal route.

The roads on the map are rasterized and produce a matrix of boolean values - True if the road is present or False if it is not. The roads in the matrix are connected only if the road is immediately left, right, below or above it.

Finish the route_exists method so that it returns True if the destination is reachable or False if it is not. The from_row and from_column parameters are the starting row and column in the map_matrix. The to_row and to_column are the destination row and column in the map_matrix. The map_matrix parameter is the above mentioned matrix produced from the map.

For example, for the given rasterized map, the code below should return True since the destination is reachable:

```python
map_matrix = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
];

route_exists(0, 0, 2, 2, map_matrix)
```

```python
def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    pass

if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];

    print(route_exists(0, 0, 2, 2, map_matrix))
```
