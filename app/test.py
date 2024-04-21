# def create_truth_table(x):
#     truth_table = {}
#     for i in range(int(len(x) ** 0.5) + 1):
#         for j in range(len(x)):
#             truth_table[j] = i
#     print(truth_table)
#
#
# n = "11000011"
# create_truth_table(n)


def create_truth_table(x):
    arg = []
    if len(x) == 8:
        num_vars = int(len(x) ** 0.5) + 1
    else:
        num_vars = int(len(x) ** 0.5)
    for i in range(num_vars):
        arg.append("x" + str(i + 1))
    print(*arg)



n = "1100110011001100"
create_truth_table(n)
