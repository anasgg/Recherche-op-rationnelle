import numpy as np

# Matrice de distances
distances = [
    [0, 3.6, 5.1, 10, 15.3, 20, 16, 14.2, 23, 26.4],
    [3.6, 0, 3.6, 6.4, 12.1, 18.1, 13.2, 10.6, 19.7, 23],
    [5.1, 3.6, 0, 7.1, 10.6, 15, 15.8, 10.8, 18.4, 21.9],
    [10, 6.4, 7.1, 0, 7, 15.7, 10, 4.2, 13.9, 17],
    [15.3, 12.1, 10.6, 7, 0, 9.9, 15.3, 5, 7.3, 11.3],
    [20, 18.1, 15, 15.7, 9.9, 0, 25, 14.9, 12, 15],
    [16, 13.2, 15.8, 10, 15.3, 25, 0, 10.3, 19.2, 21],
    [14.2, 10.6, 10.8, 4.2, 5, 14.9, 10.3, 0, 10.2, 13],
    [23, 19.7, 18.4, 13.9, 7.3, 12, 19.2, 10.2, 0, 3.6],
    [26.4, 23, 21.9, 17, 11.3, 15, 21, 13, 3.6, 0]
]

def calculate_distance(path):
    distance = 0
    for i in range(len(path) - 1):
        distance += distances[path[i]][path[i + 1]]
    distance += distances[path[-1]][path[0]]  # Retour au point de départ
    return distance

def descente_gradient_from_starting_point(starting_point, n_iterations, learning_rate):
    path = np.roll(np.arange(len(distances)), -starting_point)
    distance = calculate_distance(path)
    print("Chemin initial:", path, "Distance:", distance)

    for i in range(n_iterations):
        improved = False
        for j in range(1, len(path)-1):
            if distances[path[0]][path[j]] + distances[path[j+1]][path[-1]] > distances[path[0]][path[j+1]] + distances[path[j]][path[-1]]:
                new_path = np.copy(path)
                new_path[j], new_path[j+1] = new_path[j+1], new_path[j]
                new_distance = calculate_distance(new_path)
                if new_distance < distance:
                    path = np.copy(new_path)
                    distance = new_distance
                    print("Nouveau chemin:", path, "Distance:", distance)
                    improved = True
                    break
        if not improved:
            break
    return path, distance

n_iterations = 1000
learning_rate = 0.01
starting_point = 0
optimal_path, optimal_distance = descente_gradient_from_starting_point(starting_point, n_iterations, learning_rate)
print("Chemin optimal trouvé:", optimal_path)
print("Distance minimale trouvée:", optimal_distance)
