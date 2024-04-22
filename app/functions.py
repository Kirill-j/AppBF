import random
import numpy as np


# Выводит сообщение об ошибке ввода
def error_value(label_for_input):
    label_for_input.setText("Invalid value!\nPlease re-enter the value.")


# Добавляет пробел после каждых n символов строки
def spaces(stroka, n):
    for i in range(0, len(stroka) + (len(stroka) // n), n + 1):
        stroka = (stroka[:i] + ' ' + stroka[i:])
    return stroka


# Проверка валидности вводимого вектора функции
def is_valid(stroka: str):
    l = len(stroka)
    if stroka.count('0') + stroka.count('1') == l and (l & (l - 1) == 0) and l != 0:
        return True
    return False


# Вычисляет остаточную от вектор-функции
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


# Вычисляет оригинальный вектор на основе остаточных от него
def original_function(vector_null, vector_unit, arg):
    func_vec = []
    l_vector_null = list(vector_null)
    l_vector_unit = list(vector_unit)
    new_vector_null = np.array_split(l_vector_null, (2 ** arg) // 2)
    new_vector_unit = np.array_split(l_vector_unit, (2 ** arg) // 2)
    for i in range(2 ** arg):
        if i % 2 == 0:
            func_vec.extend(new_vector_null[i // 2])
        else:
            func_vec.extend(new_vector_unit[i // 2])
    return ''.join(func_vec)


def func_of_2_arg():
    bin_func = {}
    bin_name = ["Нулевая", "Конъюнкция", "Коимпликация", "Переменная 1", "Обратная коимпликация", "Переменная 2",
                "Сложение", "Дизъюнкция", "Стрелка", "Эквивалентность", "Отрицание", "Обратная импликация",
                "Отрицание", "Импликация", "Штрих", "Единичная"]
    for i in range(16):
        bin_func[bin_name[i]] = bin(i)[2:].zfill(4)
    return bin_func


def func_of_3_arg():
    n = random.randint(0, 256)
    return bin(n)[2:].zfill(8)


def dnf(bin_func):
    # Предполагая, что bin_func представляет собой список двоичных строк, представляющих таблицы истинности
    dnf_terms = []
    for i, binary_string in enumerate(bin_func):
        if binary_string == '1':
            # Преобразуем индекс 'i' в его двоичное представление
            binary_index = bin(i)[2:]
            # Добавьте ведущие нули, чтобы они соответствовали длине двоичных строк в таблице истинности.
            binary_index = binary_index.zfill(len(bin_func[0]))
            # Преобразование двоичного индекса в термины DNF
            dnf_terms.append("(" + "*".join([f"~x{j}" if bit == '1' else
                                             f"x{j}" for j, bit in enumerate(binary_index)])
                             + ")")
    # Объедините термины DNF с оператором OR
    return " + ".join(dnf_terms)


def cnf(bin_func):
    cnf_terms = []
    for i, binary_string in enumerate(bin_func):
        if binary_string == '0':
            # Преобразуйте индекс «i» в его двоичное представление.
            binary_index = bin(i)[2:]
            # Добавьте ведущие нули, чтобы они соответствовали длине двоичных строк в таблице истинности.
            binary_index = binary_index.zfill(len(bin_func[0]))
            # Преобразование двоичного индекса в термины CNF
            cnf_terms.append("(" + "+".join([f"~x{j}" if bit == '0' else
                                             f"x{j}" for j, bit in enumerate(binary_index)]) + ")")
    # Объедините термины CNF с оператором AND
    return " * ".join(cnf_terms)


def pdnf(bin_func):
    # Если все биты равны 1, функция тождественно истинна
    if '1' not in bin_func:
        return "PDNF does not exist"
    pdnf_list = []
    # Преобразование булевой функции в список
    bin_func_list = list(bin_func)
    # Определение числа переменных
    if len(bin_func) == 8:
        num_vars = int(len(bin_func) ** 0.5) + 1
    else:
        num_vars = int(len(bin_func) ** 0.5)
    # Проход по всем возможным наборам переменных
    for i in range(2 ** num_vars):
        # Преобразование индекса в двоичное число
        bin_index = format(i, '0' + str(num_vars) + 'b')
        # Проверка условия соответствия булевой функции значению 1
        if bin_func_list[i] == '1':
            literals = []
            # Построение дизъюнкции
            for j in range(num_vars):
                if bin_index[j] == '0':
                    literals.append('~x' + str(j + 1))
                else:
                    literals.append('x' + str(j + 1))
            pdnf_list.append("(" + " & ".join(literals) + ")")
    # Объединение всех дизъюнкций
    pdnf_expr = ""
    for i, pdnf_term in enumerate(pdnf_list):
        pdnf_expr = pdnf_expr + pdnf_term + " | "
        if (i + 1) % 4 == 0 and i != len(pdnf_list) - 1:
            pdnf_expr += "\n"
    return pdnf_expr[:-3]


def pcnf(bin_func):
    # Если все биты равны 0, функция тождественно ложна
    if '0' not in bin_func:
        return "PCNF does not exist"

    pcnf_list = []
    # Преобразование булевой функции в список
    bin_func_list = list(bin_func)
    # Определение числа переменных
    if len(bin_func) == 8:
        num_vars = int(len(bin_func) ** 0.5) + 1
    else:
        num_vars = int(len(bin_func) ** 0.5)

    # Проход по всем возможным наборам переменных
    for i in range(2 ** num_vars):
        # Преобразование индекса в двоичное число
        bin_index = format(i, '0' + str(num_vars) + 'b')
        # Проверка условия соответствия булевой функции значению 0
        if bin_func_list[i] == '0':
            literals = []
            # Построение конъюнкции
            for j in range(num_vars):
                if bin_index[j] == '0':
                    literals.append('x' + str(j + 1))
                else:
                    literals.append('~x' + str(j + 1))
            pcnf_list.append("(" + " & ".join(literals) + ")")

    # Объединение всех конъюнкций с переходом на новую строку после каждых 4
    pcnf_expr = ""
    for i, pcnf_term in enumerate(pcnf_list):
        pcnf_expr += pcnf_term + " | "
        if (i + 1) % 4 == 0 and i != len(pcnf_list) - 1:
            pcnf_expr += "\n"

    return pcnf_expr[:-3]
