fun = "1111111111111111"
length = len(fun)
if length == 8:
    arg = int(length ** 0.5) + 1
else:
    arg = int(length ** 0.5)
print(length)
print(arg)
bin_fun = []

for i in range(length):
    bin_fun.append(bin(i)[2:].zfill(int(arg)))

for i in range(len(bin_fun)):
    for j in range(len(bin_fun[i])):
        print(*bin_fun[i][j])
