def relax(w, u, v, shortest, pred):
    """
    :param w: Веса графа
    :param u: Вершина 1
    :param v: Вершина 2
    :param shortest: Массив минимальных расстояний до точки
    :param pred: Массив по которому можно восстановить кратчайший путь
    :return: Функция уменьшает значения для вершин, если нашелся такой путь, который короче чем был до этого
    """
    # Если путь новой вершины короче, чем тот который был сохранен ранее, тогда
    # меняем значения
    if shortest[u] + w[(u, v)] < shortest[v]:
        shortest[v] = shortest[u] + w[(u, v)]
        pred[v] = u


def dijkstra(g, w, n, s):
    shortest = [float('inf')] * (n + 1)
    shortest[s] = 0  # Расстояние от начальной вершины = 0 тк мы уже достигли ее
    pred = [None] * (n + 1)  # Массив, в котором хранятся пути для того, чтобы обратно воссоздать маршрут

    q = set(range(1, n+1))

    while len(q) > 0:
        min_u = next(iter(q))
        for u in q:
            if shortest[u] < shortest[min_u]:
                min_u = u

        q.discard(min_u)

        for v in g.get(min_u, []):
            relax(w, min_u, v, shortest, pred)

    return shortest, pred


if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [3],
        3: [4, 5, 1]
    }

    weights = {
        (1, 2): 4,
        (1, 3): 6,
        (2, 3): 1,
        (3, 4): 2,
        (3, 5): 3,
        (3, 1): 1
    }
    print(dijkstra(graph, weights, 5, 3))