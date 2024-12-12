import lab
import time


def track_time(func):
    """
    A decorator that tracks the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Time taken by {func.__name__}: {execution_time:.6f} seconds")
        return result
    return wrapper


filename = input('Input filaname to read: ')
start = 0
incidence_matrix = lab.read_incidence_matrix(filename)
adjacency_matrix = lab.read_adjacency_matrix(filename)
adjacency_dict = lab.read_adjacency_dict(filename)

# print(incidence_matrix)
# print(adjacency_matrix)
# print(adjacency_dict)

time1 = track_time(
    lab.iterative_adjacency_dict_dfs)
time1(adjacency_dict, start)

time2 = track_time(
    lab.iterative_adjacency_matrix_dfs)
time2(adjacency_matrix, start)

time3 = track_time(
    lab.recursive_adjacency_dict_dfs)
time3(adjacency_dict, start)

time4 = track_time(
    lab.recursive_adjacency_matrix_dfs)
time4(adjacency_matrix, start)

time5 = track_time(
    lab.iterative_adjacency_dict_bfs)
time5(adjacency_dict, start)

time6 = track_time(
    lab.iterative_adjacency_matrix_bfs)
time6(adjacency_matrix, start)
