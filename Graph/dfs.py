def create_adjacency_matrix(size):
    return [[0]*size for _ in range(size)]

if __name__ == "__main__":
    inp = input()
    num_of_nodes, lines = list(map(int, inp.split(" ")))
    print(type(num_of_nodes), type(lines))

    for _ in range(lines):
        inp = input()
        num_of_nodes, lines = list(map(int, inp.split(" ")))
        print(type(num_of_nodes), type(lines))