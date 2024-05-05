import math
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
    len_s = len(stroka)
    if stroka.count('0') + stroka.count('1') == len_s and (len_s & (len_s - 1) == 0) and len_s != 0:
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
    len_func = len(bin_func)
    if bin_func.count('1') == 0:
        return 'Для тождественного нуля не существует СДНФ'
    number_args = int(math.log2(len_func))
    args = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']
    terms = []

    for i in range(len_func):
        if bin_func[i] == '1':
            term = ''
            for j in range(number_args):
                if i // (len_func // 2 ** (j + 1)) % 2 == 0:
                    x = '!' + args[j]
                else:
                    x = '' + args[j]
                term += x + '*'
            terms.append(term)
            terms[len(terms) - 1] = terms[len(terms) - 1][:-1]

    PDNF = ''
    for i in range(len(terms)):
        PDNF += '(' + terms[i] + ')' + '+'
    PDNF = PDNF[:-1]
    return PDNF


def pcnf(bin_func):
    len_func = len(bin_func)
    if bin_func.count('0') == 0:
        return 'Для тождественной единицы не существует СКНФ'
    number_args = int(math.log2(len_func))
    args = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']
    terms = []

    for i in range(len_func):
        if bin_func[i] == '0':
            term = ''
            for j in range(number_args):
                if i // (len_func // 2 ** (j + 1)) % 2 == 0:
                    x = '' + args[j]
                else:
                    x = '!' + args[j]
                term += x + '+'
            terms.append(term)
            terms[len(terms) - 1] = terms[len(terms) - 1][:-1]

    PСNF = ''
    for i in range(len(terms)):
        PСNF += '(' + terms[i] + ')' + '*'
    PСNF = PСNF[:-1]
    return PСNF


def create_truth_table_for_vector(func):
    truth_table = {}
    number_args = int(math.log2(len(func)))
    for i in range(2 ** number_args):
        truth_table[bin(i)[2:].zfill(number_args)] = func[i]
    return truth_table


# Возвращает полином жигалкина от вектора-функции
def get_polinom_jigalkina(func):
    args = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', ]
    len_func = len(func)
    count_args = int(math.log2(len_func))
    polinom = ''
    for i in range(len_func):
        bin_i = bin(i)[2:].zfill(count_args)
        x = 0
        for j in range(i + 1):
            bin_j = bin(j)[2:].zfill(count_args)
            check = True
            for k in range(count_args):
                if bin_i[k] != '1' and bin_j[k] == '1':
                    check = False
            if check:
                x = x ^ int(func[j])
        if x == 1:
            if bin_i.count('1') == 0:
                polinom += '1xor'
            else:
                arg = ''
                for z in range(count_args):
                    if bin_i[z] == '1':
                        arg += args[z]
                polinom += arg + 'xor'
    return polinom[:-3]


def is_save_null(func):
    if func[0] == '0':
        return True
    return False


def is_save_one(func):
    if func[len(func) - 1] == '1':
        return True
    return False


def is_monotonous(func):
    number_args = int(math.log2(len(func)))
    truth_table = create_truth_table_for_vector(func)
    for i in range(2 ** number_args):
        bin_i = bin(i)[2:].zfill(number_args)
        for j in range(i + 1, 2 ** number_args):
            bin_j = bin(j)[2:].zfill(number_args)
            check = True
            for k in range(number_args):
                if bin_i[k] == '1' and bin_j[k] == '0':
                    check = False
            if check:
                if truth_table[bin_i] > truth_table[bin_j]:
                    return False
    return True


def is_linear(func):
    polinom_jig = get_polinom_jigalkina(func)
    print(polinom_jig)
    polinom_jig = polinom_jig.split('xor')
    for elem in polinom_jig:
        if len(elem) > 2:
            return False
    return True


def is_selfdual(func):
    for i in range(len(func) // 2):
        if func[i] == func[len(func) - i - 1]:
            return False
    return True
