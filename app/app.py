from PySide6.QtWidgets import QTabWidget
from design import Ui_Widget

import functions
import random


class Application(QTabWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tabBar().setDocumentMode(True)

        self.buttons_connections()
        self.answer = "Answer: "
        self.right_button = None

    def buttons_connections(self):
        self.button_enter_1.clicked.connect(self.exercise_1)
        self.button_enter_2.clicked.connect(self.exercise_2)
        self.button_enter_3.clicked.connect(self.exercise_3)
        self.button_start_4.clicked.connect(self.exercise_4)
        self.button_start_5.clicked.connect(self.exercise_5)
        self.button_enter_5.clicked.connect(self.exercise_5_check)
        self.button_start_6.clicked.connect(self.exercise_6)
        self.button_start_7.clicked.connect(self.exercise_7)
        self.button_enter_8.clicked.connect(self.exercise_8)
        self.button_enter_9.clicked.connect(self.exercise_9)

    def exercise_1(self):
        n = self.input_text_1.text()
        if n.isnumeric():
            n = int(n)
            n = functions.spaces(functions.get_func(n), n - 2)
            self.answer_1.setText(self.answer + n)
        else:
            functions.error_value(self.answer_1)

    def exercise_2(self):
        func_vector = self.input_text_2_1.text()
        sigma = self.input_text_2_2.text()
        arg_number = self.input_text_2_3.text()
        if functions.is_valid(func_vector) and (sigma == '0' or sigma == '1') and arg_number.isnumeric():
            func_vector = int(func_vector)
            sigma = int(sigma)
            arg_number = int(arg_number)
            res_func = functions.residual_function(func_vector, sigma, arg_number)
            res_func = functions.spaces(res_func, arg_number - 1)
            self.answer_2.setText(self.answer + res_func)
        else:
            functions.error_value(self.answer_2)

    def exercise_3(self):
        residual_vector_null = self.input_text_3_1.text()
        residual_vector_unit = self.input_text_3_2.text()
        arg_number = self.input_text_3_3.text()
        if functions.is_valid(residual_vector_null) & functions.is_valid(residual_vector_unit) & arg_number.isnumeric():
            arg_number = int(arg_number)
            orig_func = functions.original_function(residual_vector_null, residual_vector_unit, arg_number)
            orig_func = functions.spaces(orig_func, arg_number)
            self.answer_3.setText(self.answer + orig_func)
        else:
            functions.error_value(self.answer_3)

    def exercise_4(self):
        self.answer_4.clear()
        buttons = [self.btn_ans_4_1, self.btn_ans_4_2, self.btn_ans_4_3, self.btn_ans_4_4,
                   self.btn_ans_4_5, self.btn_ans_4_6, self.btn_ans_4_7, self.btn_ans_4_8,
                   self.btn_ans_4_9, self.btn_ans_4_10, self.btn_ans_4_11, self.btn_ans_4_12,
                   self.btn_ans_4_13, self.btn_ans_4_14, self.btn_ans_4_15, self.btn_ans_4_16]
        for button in buttons:
            button.setText('')
        dict_func = {}
        name_func = ["Нулевая", "Конъюнкция", "Коимпликация", "Переменная 1", "Обратная коимпликация", "Переменная 2",
                     "Сложение", "Дизъюнкция", "Стрелка", "Эквивалентность", "Отрицание 2 Переменной",
                     "Обратная импликация", "Отрицание 1 Переменной", "Импликация",
                     "Штрих", "Единичная"]
        for i in range(16):
            dict_func[name_func[i]] = bin(i)[2:].zfill(4)
        random_key = random.choice(list(dict_func.keys()))
        self.label_function_4.setText(dict_func[random_key])
        dict_func.pop(random_key)
        self.right_button = random.choice(buttons)
        self.right_button.setText(random_key)

        for button in buttons:
            if button != self.right_button:
                random_keys = random.choice(list(dict_func.keys()))
                dict_func.pop(random_keys)
                button.setText(random_keys)
            button.clicked.connect(lambda _, func=button: self.check_answer_4(func))

    def check_answer_4(self, func):
        if self.right_button == func:
            self.answer_4.setText("Right!")
        else:
            self.answer_4.setText("Wrong!")

    def exercise_5(self):
        self.answer_5.clear()
        self.answer_5.setText(self.answer)
        for radio_buttons in (self.radio_button_5_x_fict, self.radio_button_5_x_su,
                              self.radio_button_5_y_fict, self.radio_button_5_y_su,
                              self.radio_button_5_z_fict, self.radio_button_5_z_su):
            radio_buttons.setAutoExclusive(False)
            radio_buttons.setChecked(False)
            radio_buttons.setAutoExclusive(True)
        self.label_5_func.setText(functions.spaces(functions.get_func(3)))
        self.answer_5.clear()

    def exercise_5_check(self):
        if self.label_5_func.text() == 'Вектор':
            return self.answer_5.setText("Вы не нажали старт")
        if not ((self.radio_button_5_x_su.isChecked() or self.radio_button_5_x_fict.isChecked()) and (
                self.radio_button_5_y_su.isChecked() or self.radio_button_5_y_fict.isChecked()) and (
                        self.radio_button_5_z_su.isChecked() or self.radio_button_5_z_fict.isChecked())):
            return self.answer_5.setText("Выберите каждую переменную")

        func = self.label_5_func.text().replace(' ', '')
        x = functions.check_fict_of_significant(func, 1)
        y = functions.check_fict_of_significant(func, 2)
        z = functions.check_fict_of_significant(func, 3)

        if (self.radio_button_5_x_fict.isChecked() and x == 0 or self.radio_button_5_x_su.isChecked() and x == 1) and (
                self.radio_button_5_y_fict.isChecked() and y == 0 or self.radio_button_5_y_su.isChecked() and y == 1) and (
                self.radio_button_5_z_fict.isChecked() and z == 0 or self.radio_button_5_z_su.isChecked() and z == 1):
            return self.answer_5.setText("Right !")
        else:
            return self.answer_5.setText("Wrong")

    def exercise_6(self):
        bin_func = str(functions.get_func(3))
        self.label_function_6.setText(bin_func)
        print(functions.dnf(bin_func))

        def on_button_click(user_input):
            user_input = str(user_input)
            ans = functions.dnf(bin_func)
            self.check_answer_6(user_input, ans, self.answer)

        self.button_enter_6.clicked.connect(lambda: on_button_click(self.input_text_6.text()))

    def check_answer_6(self, user_dnf, ans, answer):
        self.answer_6.clear()
        print(user_dnf)
        print(ans)
        if user_dnf == ans:
            self.answer_6.setText(answer + "Right!")
        else:
            self.answer_6.setText(answer + "Wrong!")

    def exercise_7(self):
        bin_func = str(functions.get_func(3))
        self.label_function_7.setText(bin_func)
        print(functions.cnf(bin_func))

        def on_button_click(user_input):
            user_input = str(user_input)
            ans = functions.cnf(bin_func)
            self.check_answer_7(user_input, ans, self.answer)

        self.button_enter_7.clicked.connect(lambda: on_button_click(self.input_text_7.text()))

    def check_answer_7(self, user_cnf, ans, answer):
        self.answer_7.clear()
        print(user_cnf)
        print(ans)
        if user_cnf == ans:
            self.answer_7.setText(answer + "Right!")
        else:
            self.answer_7.setText(answer + "Wrong!")

    def exercise_8(self):
        self.answer_8.clear()
        bin_func = self.input_text_8.text()
        if bin_func.isnumeric() and bin_func != '0' and bin_func != '1' and (
                len(bin_func) & (len(bin_func) - 1)) == 0:
            self.answer_8.setText("PDNF: " + functions.pdnf(bin_func))
        else:
            functions.error_value(self.answer_8)

    def exercise_9(self):
        self.answer_9.clear()
        bin_func = self.input_text_9.text()
        if bin_func.isnumeric() and bin_func != '0' and bin_func != '1' and (
                len(bin_func) & (len(bin_func) - 1)) == 0:
            self.answer_9.setText("PCNF: " + functions.pcnf(bin_func))
        else:
            functions.error_value(self.answer_9)
