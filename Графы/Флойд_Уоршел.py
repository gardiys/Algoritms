def floyd_warshall(g, n):
    shortest = [[float('inf') for _ in range(n)] for _ in range(n)]
    pred = [[None for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            shortest[u][v] = g[u][v]
            if g[u][v] != float("inf"):
                pred[u][v] = u

    for x in range(n):
        for u in range(n):
            for v in range(n):
                if shortest[u][v] > shortest[u][x] + shortest[x][v]:
                    shortest[u][v] = shortest[u][x] + shortest[x][v]
                    pred[u][v] = pred[x][v]

    return shortest, pred


if __name__ == "__main__":
    graph = [
        [0, 3, 8, float("inf")],
        [float("inf"), 0, float('inf'), 1],
        [float("inf"), 4, 0, float('inf')],
        [2, float('inf'), -5, 0]
    ]
    n = 4
    print(floyd_warshall(graph, n))

