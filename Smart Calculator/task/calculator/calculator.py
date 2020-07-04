from string import ascii_letters
from string import digits
from collections import deque


class Calculator:

    operators_precedence_map = {'(': 7,
                                ')': 6,
                                '^': 5,
                                '*': 4,
                                '/': 3,
                                '+': 2,
                                '-': 1}

    def __init__(self):
        self.store = {}
        self.postfix_stack = deque()
        self.check_brace_stack = deque()

    def display_help(self):
        print('The program can calculate all possible addition and subtraction')

    def determine_symbol(self, symbol):
        if '+' in symbol:
            return '+'
        if '-' in symbol:
            return '-' if len(symbol) % 2 == 1 else '+'

    def extract_info_equals(self, string):
        key, value = [x.strip() for x in string.split('=', maxsplit=1)]
        return key, value

    def check_variable_names(self, name, position):
        for character in name:
            if character in digits:
                if position == 'before':
                    print('Invalid identifier')
                    return False
                if position == 'after':
                    print('Invalid assignment')
                    return False
        return True

    def check_value(self, value):
        try:
            return int(value)
        except ValueError:
            if self.check_variable_names(value, 'after'):
                value = self.store.get(value)
                if value is None:
                    print('Unknown variable')
                    return None
                return value

    def update_store(self, string):
        variable, value = self.extract_info_equals(string)
        if self.check_variable_names(variable, 'before'):
            value = self.check_value(value)
            if value is not None:
                self.store[variable] = value

    def fetch_store(self, key):
        return self.store.get(key)

    def add_to_stack(self, char, compare_list):
        if len(self.postfix_stack) > 0 and self.postfix_stack[-1] in compare_list:
            self.postfix_stack.append(self.postfix_stack.pop() + char)
        else:
            self.postfix_stack.append(char)

    def evaluate_expression(self, exp_string):
        self.postfix_stack.clear()
        for character in exp_string:
            if character in digits:
                self.add_to_stack(character, digits)
            elif character in ascii_letters:
                self.add_to_stack(character, ascii_letters)
            elif character in self.operators_precedence_map:
                self.add_to_stack(character, self.operators_precedence_map)

        # Calculate the expression
        try:
            for i, variable in enumerate(self.postfix_stack):
                if all(True if operator not in variable else False for operator in self.operators_precedence_map):
                    self.postfix_stack[i] = str(self.check_value(variable))
                if variable.startswith('/') and len(variable) > 1:
                    print('Invalid expression')
                    break
            print(int(eval("".join(self.postfix_stack))))
        except SyntaxError:
            print('Invalid expression')

    def display_variable_value(self, string):
        if self.check_variable_names(string, 'before'):
            value = self.fetch_store(string)
            if value is None:
                print('Unknown variable')
            else:
                print(value)

    def perform_calculation(self, string):
        if '=' in string:
            self.update_store(string)
        elif all(True if operator not in string else False for operator in self.operators_precedence_map):
            self.display_variable_value(string)
        else:
            self.evaluate_expression(string)

    def determine_action(self, string):
        if string.startswith('/'):
            if string == '/exit':
                print('Bye!')
                exit(0)
            elif string == '/help':
                self.display_help()
            else:  # for any other command, display unknown command
                print('Unknown command')
        elif string != '':   # check for empty string
            self.perform_calculation(string)

    def run(self, string):
        self.determine_action(string)


calc = Calculator()
while True:
    calc.run(input())
