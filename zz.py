import random  # Санамсаргүй тоо үүсгэх модуль
from collections import deque  # Дараалал хэрэгжүүлэх модуль
import time  # Цаг хугацаа хэмжих модуль

VERTICES = 500  # Графын оргилуудын тоо

# Графт хоёр оргилын хооронд зах байгаа эсэхийг шалгах функц
def has_edge(edge_array, source, target):
    for edge in edge_array:  # Бүх захыг шалгана
        if (edge[0] == source and edge[1] == target) or (edge[0] == target and edge[1] == source):  # Эсрэг чиглэлтэй захыг мөн шалгана
            return True  # Зах байвал үнэн утга буцаана
    return False  # Зах байхгүй бол худал утга буцаана

# Өргөн хайлт (BFS) алгоритм
def bfs(edge_array, start):
    visited = [False] * VERTICES  # Орой тус бүрийн айлчлагдсан төлөвийг хадгалах жагсаалт
    queue = deque([start])  # BFS-ийн дарааллыг эхлүүлнэ
    visited[start] = True  # Эхлэх оройг айлчилсан гэж тэмдэглэнэ

    while queue:  # Дараалал хоосон биш бол
        current = queue.popleft()  # Дарааллын эхний элементийг авна
        for edge in edge_array:  # Бүх захыг шалгана
            neighbor = -1  # Хөрш орой хадгалах хувьсагч
            if edge[0] == current:  # Одоогийн оройтой холбогдсон зах байвал
                neighbor = edge[1]
            elif edge[1] == current:
                neighbor = edge[0]
            
            if neighbor != -1 and not visited[neighbor]:  # Хөрш оройг айлчлаагүй бол
                queue.append(neighbor)  # Хөрш оройг дараалалд нэмнэ
                visited[neighbor] = True  # Айлчлагдсан гэж тэмдэглэнэ

# BFS-ийн хугацааг хэмжих функц
def measure_bfs(edge_array):
    start_time = time.perf_counter_ns()  # Алгоритмын эхлэх хугацааг хэмжинэ
    bfs(edge_array, 0)  # BFS алгоритмыг гүйцэтгэнэ
    return time.perf_counter_ns() - start_time  # Үргэлжлэх хугацааг буцаана

# Гүнзгий хайлт (DFS) алгоритм
def dfs(edge_array, current, visited):
    visited[current] = True  # Одоогийн оройг айлчилсан гэж тэмдэглэнэ
    for edge in edge_array:  # Бүх захыг шалгана
        neighbor = -1  # Хөрш орой хадгалах хувьсагч
        if edge[0] == current:  # Одоогийн оройтой холбогдсон зах байвал
            neighbor = edge[1]
        elif edge[1] == current:
            neighbor = edge[0]
        
        if neighbor != -1 and not visited[neighbor]:  # Хөрш оройг айлчлаагүй бол
            dfs(edge_array, neighbor, visited)  # Гүнзгий хайлтаар хөрш оройг айлчилна

# DFS-ийн хугацааг хэмжих функц
def measure_dfs(edge_array):
    start_time = time.perf_counter_ns()  # Алгоритмын эхлэх хугацааг хэмжинэ
    dfs(edge_array, 0, [False] * VERTICES)  # DFS алгоритмыг гүйцэтгэнэ
    return time.perf_counter_ns() - start_time  # Үргэлжлэх хугацааг буцаана

# Захуудыг хэвлэх функц
def print_edge_array(edge_array):
    for edge in edge_array:  # Бүх захыг шалгана
        print(f"{edge[0]} - {edge[1]}")  # Захыг хэвлэнэ

# Гол програм
if __name__ == "__main__":
    # Захуудын жагсаалтыг үүсгэх
    edge_array = []

    # Графыг санамсаргүй байдлаар үүсгэх
    for i in range(VERTICES):  # Бүх оргилуудад зориулж
        degree = random.randint(1, 10)  # Оргил тус бүрийн холболтын тоог санамсаргүйгээр үүсгэнэ
        for _ in range(degree):  # Холболтуудыг үүсгэнэ
            neighbor = random.randint(0, VERTICES - 1)  # Санамсаргүй хөрш орой сонгоно
            if i != neighbor and not has_edge(edge_array, i, neighbor):  # Өөртэйгөө холбогдохгүй ба давхардсан зах үүсгэхгүй
                edge_array.append([i, neighbor])  # Шинэ зах нэмнэ

    # Графын бүтэцийг харах
    print("Edge Array List:")  # Захуудын жагсаалтыг хэвлэнэ
    print_edge_array(edge_array)

    # BFS ба DFS-ийн хугацааны хэмжилт
    print("\nTime Measurements:")  # Хугацааны хэмжилтүүдийг хэвлэнэ
    print(f"BFS time measurement (Edge Array): {measure_bfs(edge_array)}")  # BFS хугацаа
    print(f"DFS time measurement (Edge Array): {measure_dfs(edge_array)}")  # DFS хугацаа
