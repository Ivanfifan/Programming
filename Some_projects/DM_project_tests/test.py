import random
from collections import deque


# === 1. Функція генерації ОРІЄНТОВАНОГО графу G(n, p) у вигляді списку суміжності ===
def generate_erdos_renyi_digraph(n, p):
    """
    Генерує орієнтований граф G(n, p) у вигляді списку суміжності.
    """
    graph = {i: [] for i in range(n)}
    nodes = list(range(n))

    for i in nodes:
        for j in nodes:
            # Створюємо орієнтоване ребро i -> j з імовірністю p (включно з i=j)
            if i != j and random.random() <= p:
                graph[i].append(j)

    return graph


# === 2. Функції для обчислення Матриці Досяжності за допомогою BFS ===

def bfs(graph, start_node):
    """Обхід у ширину (BFS) для пошуку досяжних вершин."""
    queue = deque([start_node])
    visited = {start_node}

    while queue:
        current_node = queue.popleft()

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


def build_reachability_matrix(graph, n):
    """Побудова матриці досяжності, використовуючи BFS для кожного вузла."""

    M = [[0] * n for _ in range(n)]

    for i in range(n):  # i - стартова вершина (рядок матриці)

        # Запуск BFS
        reached_nodes = bfs(graph, i)

        # Заповнення i-го рядка
        for j in range(n):  # j - цільова вершина (стовпець матриці)
            if j in reached_nodes:
                M[i][j] = 1

    return M


def print_matrix(matrix, n):
    """Виводить матрицю."""
    print("   ", ' '.join(map(str, range(n))))  # Заголовок стовпців
    print("---", "---" * n)
    for i, row in enumerate(matrix):
        print(f"{i} |", ' '.join(map(str, row)))


# =======================================================
# --- ЗАПУСК КОДУ ---
# =======================================================

N_VERTICES = 7  # Кількість вершин
P_PROBABILITY = 0.25  # Ймовірність ребра 25%

# 1. Генерація графа Ердеша-Реньї
graph_er = generate_erdos_renyi_digraph(N_VERTICES, P_PROBABILITY)

print(f"Модель Ердеша-Реньї G(n={N_VERTICES}, p={P_PROBABILITY})")
print("\nЗгенерований список суміжності (орієнтований):")
for node, neighbors in graph_er.items():
    print(f"Вершина {node}: {neighbors}")

# 2. Побудова матриці досяжності
reachability_matrix = build_reachability_matrix(graph_er, N_VERTICES)

print("\nМатриця досяжності (обчислена за допомогою BFS):")
print_matrix(reachability_matrix, N_VERTICES)