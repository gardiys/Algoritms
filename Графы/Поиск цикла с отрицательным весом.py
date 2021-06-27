from Белман_Форд import belman_ford


def find_negative_weight_cycle(g, w, n, shortest, pred):
    # Обходим все ребра
    for u in range(1, n):
        for v in g.get(u, []):
            if shortest[u] + w[(u, v)] < shortest[v]:
                # Если мы попали в тело этого if, тогда мы точно знаем, что
                # цикл с отрицательными весами уже есть

                # находим этот цикл
                visited = [False] * (n + 1)
                x = v
                # восстанавливаем цикл
                while x is not None and not visited[x]:
                    visited[x] = True
                    x = pred[x]
                # Собираем вершины цикла
                v = pred[x]
                cycle = [x]
                while v != x:
                    cycle.append(v)
                    v = pred[v]
                return cycle[::-1]
    return []


if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [3],
        3: [4, 5, 1]
    }

    weights = {
        (1, 2): -4,
        (1, 3): 6,
        (2, 3): -1,
        (3, 4): 2,
        (3, 5): -3,
        (3, 1): 1
    }
    shortest, pred = belman_ford(graph, weights, 5, 1)
    print(find_negative_weight_cycle(graph, weights, 5, shortest, pred))
