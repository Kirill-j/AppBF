import random

def get_func(n):
    k = 2 ** (2 ** n) - 1
    randon_int = random.randint(0, k)
    return bin(randon_int)[2:].zfill(2 ** n)

def create_truth_table(x):
    arg_name = []
    num_vars = int(len(get_func(3)) ** 0.5) + 1
    for i in range(num_vars):
        arg_name.append("x" + str(i + 1))
    print(*arg_name)

    arg = [[0]] * len(x)
    for i in range(len(x)):
        arg[i] = [0] * num_vars

    for i in range(len(arg)):
        for j in range(len(arg[i])):
            print(arg[i][j], end = '  ')
        print()

n = "11001100"
create_truth_table(n)
