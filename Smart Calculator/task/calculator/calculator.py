

class Calculator:

    def __init__(self, input_calc):
        self.input_calc = input_calc

    def display_help(self):
        print('The program calculates the sum and subtraction of numbers')

    def determine_sign(self, symbol):
        if '+' in symbol:
            return '+'
        return '-' if len(symbol) % 2 == 1 else '+'

    def fetch_input(self, string):
        if string == '/exit':
            print('Bye!')
            exit(0)
        elif string == '/help':
            self.display_help()
        elif string == '':
            pass
        else:  # do real stuff
            list_of_input = string.split()
            list_of_input = [x if i % 2 == 0 else self.determine_sign(x) for i, x in enumerate(list_of_input)]
            print(sum(map(int, [list_of_input[0]] +
                          [list_of_input[i] + list_of_input[i + 1] for i in range(1, len(list_of_input), 2)])))

    def run(self):
        self.fetch_input(self.input_calc)


while True:
    calc = Calculator(input())
    calc.run()
