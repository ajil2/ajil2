import random  # Санамсаргүй тоо үүсгэх модуль
from collections import deque  # Дараалал хэрэгжүүлэх модуль
import time  # Цаг хугацаа хэмжих модуль

VERTICES = 500  # Графын оройн тоо

# Графт хоёр оройн хооронд зах байгаа эсэхийг шалгах функц
def has_edge(edge_array, source, target):
    for edge in edge_array:  # Бүх захыг шалгана
        if (edge[0] == source and edge[1] == target) or (edge[0] == target and edge[1] == source):  # Эсрэг чиглэлтэй захыг мөн шалгана
            return True  # Зах байвал үнэн утга буцаана
    return False  # Зах байхгүй бол худал утга буцаана

# хайлт (BFS Дараалсан оройн хайлт) алгоритм
def bfs(edge_array, start):
    visited = [False] * VERTICES  # Орой тус бүрийн visited төлөвийг хадгалах жагсаалт
    queue = deque([start])  # BFS-ийн дарааллыг эхлүүлнэ
    visited[start] = True  # Эхлэх оройг visit гэж тэмдэглэнэ

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

# (DFS Гүн замын хайлт) алгоритм
def dfs(edge_array, current, visited):
    visited[current] = True  # Одоогийн оройг visited гэж тэмдэглэнэ
    for edge in edge_array:  # Бүх захыг шалгана
        neighbor = -1  # Хөрш орой хадгалах хувьсагч
        if edge[0] == current:  # Одоогийн оройтой холбогдсон зах байвал
            neighbor = edge[1]
        elif edge[1] == current:
            neighbor = edge[0]
        
        if neighbor != -1 and not visited[neighbor]:  # Хөрш орой visited биш бол
            dfs(edge_array, neighbor, visited)

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
        degree = random.randint(1, 10)  # Орой тус бүрийн холболтын тоог санамсаргүйгээр үүсгэнэ
        for _ in range(degree):  # Холболтуудыг үүсгэнэ
            neighbor = random.randint(0, VERTICES - 1)  # Санамсаргүй хөрш орой сонгоно
            if i != neighbor and not has_edge(edge_array, i, neighbor):  # Өөртэйгөө холбогдохгүй ба давхардсан зах үүсгэхгүй
                edge_array.append([i, neighbor])  # Шинэ зах нэмнэ
    print("Массивт жагсаалт:") 
    print_edge_array(edge_array)

    print("\nЦагын хэмжилтүүд:")  
    print(f"Дараалсан оройн хайлтын хугацаа): {measure_bfs(edge_array)}")
    print(f"Гүн замын хайлтын хугацаа: {measure_dfs(edge_array)}") 
