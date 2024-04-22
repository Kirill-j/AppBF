import numpy as np  

def residual_function(vector, sig, arg):
    l_vector = list(str(vector))
    new_vector = np.array_split(l_vector, 2 ** arg)
    res_func = []
    if sig == 0:
        for i in range(2 ** arg):
            if i % 2 == 0:
                res_func.extend(new_vector[i])
    else:
        for i in range(2 ** arg):
            if i % 2 != 0:
                res_func.extend(new_vector[i])
    return ''.join(res_func)

# Вычисляет существенные и фиктивные переменные
def significant_or_dummy_variable(vector):
    zero_res_func = residual_function(vector, 0, 3)
    single_res_func = residual_function(vector, 1, 3)
    lst = [[zero_res_func], [single_res_func]]
    print(zero_res_func)
    print(single_res_func)
    fict = []
    sush = []
    for i in range(len(zero_res_func)):
        if zero_res_func[i] == single_res_func[i]:
            fict.append(i + 1)
        else:
            sush.append(i + 1)
    return fict, sush

print(*significant_or_dummy_variable("11101011"))
