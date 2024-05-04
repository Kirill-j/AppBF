import random
import numpy as np


# Выводит сообщение об ошибке ввода
def error_value(label_for_input):
    label_for_input.setText('Неверное значение!\nПожалуйста, введите значение заново')


# Возвращает булеву вектор-функцию от n аргументов
def get_func(n):
    k = 2 ** (2 ** n) - 1
    randon_int = random.randint(0, k)
    return bin(randon_int)[2:].zfill(2 ** n)


# Ставит пробелы по n-му аргументу
def spaces(stroka, n=1):
    if n < 0:
        n = 0
    step = len(stroka) // 2 ** n
    position = step
    steps = 2 ** n - 1
    for i in range(0, steps):
        stroka = (stroka[:position] + ' ' + stroka[position:])
        position += step + 1
    return stroka


# Проверка валидности вводимого вектора функции
def is_valid(stroka: str):
    les_s = len(stroka)
    if stroka.count('0') + stroka.count('1') == les_s and (les_s & (les_s - 1) == 0) and les_s != 0:
        return True
    return False


# Возвращает таблицу истинности для формулы в виде вектора
def create_truth_table(formula):
    formula = formula.replace('!x', '(x^1)')
    formula = formula.replace('!y', '(y^1)')
    formula = formula.replace('!z', '(z^1)')
    formula = formula.replace('+', ' or ')
    formula = formula.replace('*', ' and ')
    tr_table = ''
    for x in range(2):
        for y in range(2):
            for z in range(2):
                tr_table += str(eval(formula))
    return tr_table


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


# Возвращает 1, если переменная существенная и 0 если фиктивная
def check_fict_of_significant(func, arg_num):
    x_0 = residual_function(func, 0, arg_num)
    x_1 = residual_function(func, 1, arg_num)
    return 0 if x_0 == x_1 else 1


# Проверяет корректность формулы ДНФ или КНФ
def formula_validity(formula):
    if (formula.count('(') + formula.count(')') + formula.count('x') + formula.count('y') + formula.count('z') +
            formula.count('+') + formula.count('*') + formula.count('!') + formula.count(' ') != len(formula) or
            formula.count('(') != formula.count(')')):
        return 'Некорректная формула'

    dnf = True
    cnf = True

    if (formula.count('x') + formula.count('y') + formula.count('z')) == 1:
        return 'DNF and CNF'
    if (formula.count('+') + formula.count('*')) == 1:
        return 'DNF and CNF'
    if formula.count('(') == 0:
        return 'DNF'

    bracket_is_open = True if formula[0] == '(' else False
    for i in range(1, len(formula)):
        current_el = formula[i]
        prev_el = formula[i - 1]

        if prev_el == '(' and current_el != '!' and current_el != 'x' and current_el != 'y' and current_el != 'z':
            dnf, cnf = (False, False)

        if prev_el == '!' and current_el != 'x' and current_el != 'y' and current_el != 'z':
            dnf, cnf = (False, False)

        if prev_el == '*' or prev_el == '+':
            if (current_el != '!' and
                    current_el != 'x' and current_el != 'y' and current_el != 'z' and current_el != '('):
                dnf, cnf = (False, False)
            if current_el == '(':
                bracket_is_open = True

        if prev_el == ')':
            if current_el == '*':
                dnf = False
            elif current_el == '+':
                cnf = False
            else:
                dnf, cnf = (False, False)

        if prev_el == 'x' or prev_el == 'y' or prev_el == 'z':
            if current_el == ')':
                bracket_is_open = False
            elif current_el == '*':
                if bracket_is_open:
                    cnf = False
                else:
                    dnf = False
            elif current_el == '+':
                if bracket_is_open:
                    dnf = False
                else:
                    cnf = False
            else:
                dnf, cnf = (False, False)
    if dnf and cnf:
        return 'DNF and CNF'
    elif dnf:
        return 'DNF'
    elif cnf:
        return 'CNF'
    else:
        return 'Некорректная формула'


# Проверяет, является ли формула ДНФ функции
def is_dnf(formula, func):
    formula_type = formula_validity(formula)
    if formula_type == 'DNF' or formula_type == 'DNF and CNF':
        true_table = create_truth_table(formula)

        formula = formula.replace('!', '')
        formula = formula.replace('(', '')
        formula = formula.replace(')', '')

        # Проверка того, что каждый литерал встречается не более 1-го раза в каждом терме
        terms = formula.split('+')
        for term in terms:
            for literal in term:
                if literal != '+' and literal != '*' and term.count(literal) > 1:
                    return 'Литерал ' + literal + ' встречается более 1го раза в одном из термов'

        if true_table != func:
            return 'Таблица истинности вашей формулы не совпадает с вектором\n' + true_table + ' != ' + func
        return 'Right'
    if formula_type == 'CNF':
        return 'Формула является КНФ, но не ДНФ'
    return formula_type


# Проверяет, является ли формула КНФ функции
def is_cnf(formula, func):
    formula_type = formula_validity(formula)
    if formula_type == 'CNF' or formula_type == 'DNF and CNF':
        true_table = create_truth_table(formula)

        formula = formula.replace('!', '')
        formula = formula.replace('(', '')
        formula = formula.replace(')', '')

        # Проверка того, что каждый литерал встречается не более 1-го раза в каждом терме
        terms = formula.split('*')
        for term in terms:
            for literal in term:
                if literal != '+' and literal != '*' and term.count(literal) > 1:
                    return 'Литерал ' + literal + ' встречается более 1го раза в одном из термов'

        if true_table != func:
            return 'Таблица истинности вашей формулы не совпадает с вектором\n' + true_table + ' != ' + func
        return 'Right'
    if formula_type == 'DNF':
        return 'Формула является ДНФ, но не КНФ'
    return formula_type


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
