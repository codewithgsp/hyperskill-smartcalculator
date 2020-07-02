from string import digits


class Calculator:

    def __init__(self):
        self.store = {}

    def display_help(self):
        print('The program can calculate all possible addition and subtraction')

    def determine_symbol(self, symbol):
        if '+' in symbol:
            return '+'
        if '-' in symbol:
            return '-' if len(symbol) % 2 == 1 else '+'

    def extract_info_equals(self, string):
        return [x.strip() for x in string.split('=', maxsplit=1)]

    def check_variable_names(self, name):
        for character in name:
            if character in digits:
                return False
        return True

    def check_value(self, value):
        try:
            return int(value)
        except ValueError:
            if self.check_variable_names(value):
                return self.store.get(value)
            else:
                return 'Invalid assignment'

    def update_store(self, key, value):
        self.store[key] = value

    def fetch_store(self, key):
        return self.store.get(key)

    def evaluate_expression(self, exp_list):
        final_exp_list = []
        for i, exp in enumerate(exp_list):
            if i % 2 == 0:
                final_exp_list.append(str(self.check_value(exp)))
            else:
                final_exp_list.append(exp)
        print(eval(" ".join(final_exp_list)))

    def perform_calculation(self, string):
        if '=' in string:
            split_equals_list = self.extract_info_equals(string)
            if self.check_variable_names(split_equals_list[0]):
                variable = split_equals_list[0]
                value = self.check_value(split_equals_list[1])
                if value is None:
                    print('Unknown variable')
                elif value == 'Invalid assignment':
                    print('Invalid assignment')
                else:
                    self.update_store(variable, value)
            else:
                print('Invalid identifier')
        elif '+' in string or '-' in string:
            self.evaluate_expression(string.split())
        else:
            split_equals_list = self.extract_info_equals(string)
            if self.check_variable_names(split_equals_list[0]):
                variable = split_equals_list[0]
                value = self.fetch_store(variable)
                if value is None:
                    print('Unknown variable')
                else:
                    print(value)
            else:
                print('Invalid identifier')

    def fetch_input(self, string):
        if string == '/exit':
            print('Bye!')
            exit(0)
        elif string == '/help':
            self.display_help()
        elif string == '':
            pass
        elif string.startswith('/') and string[1:5] not in ('exit', 'help'):
            print('Unknown command')
        else:
            self.perform_calculation(string)

    def run(self, string):
        self.fetch_input(string)


calc = Calculator()
while True:
    calc.run(input())
