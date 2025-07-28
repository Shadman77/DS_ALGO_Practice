def create_adjacency_matrix(size):
    return [[0]*size for _ in range(size)]

def set_adjacency_matrix_undirectional(node_a, node_b, adjacency_matrix):
    adjacency_matrix[node_a-1][node_b-1] = 1
    adjacency_matrix[node_b-1][node_a-1] = 1

def get_adjacent_nodes(node, adjacency_matrix):
    adjacent_nodes = list()
    for i in range(len(adjacency_matrix[node-1])):
        if adjacency_matrix[node-1][i] == 1:
            adjacent_nodes.append(i+1)
    return adjacent_nodes

def bfs(start, adjacency_matrix):
    queue = list()
    visited = list()

    queue.append(start)
    while(len(queue) > 0):
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            adjacent_nodes = get_adjacent_nodes(node, adjacency_matrix)
            for adjacent_node in adjacent_nodes:
                if adjacent_node not in visited:
                    queue.append(adjacent_node)
        
    print(visited)

if __name__ == "__main__":
    inp = input()
    num_of_nodes, lines = list(map(int, inp.split(" ")))
    
    adjacency_matrix = create_adjacency_matrix(num_of_nodes)
    # print(adjacency_matrix)

    for _ in range(lines):
        inp = input()
        node_from, node_to = list(map(int, inp.split(" ")))
        set_adjacency_matrix_undirectional(node_from, node_to, adjacency_matrix)
    
    # print(adjacency_matrix)

    bfs(1, adjacency_matrix)