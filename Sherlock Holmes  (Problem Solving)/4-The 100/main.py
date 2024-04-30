def read_matrix(filename):
    with open(filename, "r") as file:
        return [[int(char) for char in line.strip()] for line in file]

def dijkstra(matrix):
    n = len(matrix)
    distances = [[float('inf')] * n for _ in range(n)]
    distances[0][0] = matrix[0][0]
    visited = set()
    directions = [(1, 0), (0, 1)]
    while True:
        min_dist = float('inf')
        min_node = None
        for i in range(n):
            for j in range(n):
                if (i, j) not in visited and distances[i][j] < min_dist:
                    min_dist = distances[i][j]
                    min_node = (i, j)
        
        if min_node == (n-1, n-1):
            break
        
        visited.add(min_node)
        x, y = min_node
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_dist = distances[x][y] + matrix[nx][ny]
                if new_dist < distances[nx][ny]:
                    distances[nx][ny] = new_dist

    return distances[n-1][n-1]

def main():
    matrix = read_matrix("input.txt")
    print(dijkstra(matrix))

if __name__ == "__main__":
    main()
