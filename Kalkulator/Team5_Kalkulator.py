from abc import ABC

class ExitLoop(Exception):
    pass

class Singleton(type):  # Singleton, so no new instance if the variable is called for the operations
    _instances = {}     # maybe other, simpler Singleton version can be used, I only managed with this

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls) \
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class Calculator(metaclass=Singleton):      # main class, this has to be initialized to run the calculations

    def __init__(self):
        self.current_first_number = None
        self.current_second_number = None
        self.current_result = None
        self.current_operand = None
        self.allowed_operands_list = []
        self.fact = OperationFactory()      # initializes Factory so that the operations get initialized

    def calculate(self):
        for key in OperationFactory.dict_operations.keys():     # compile a list of allowed operands to print at
            self.allowed_operands_list.extend(list(key))        # start and also for error message

        if not self.current_result:         # at start to print the instructions and allowed operands
            self.initialize()

        try:
            while True:                         # loop until terminated by user
                self.get_number()  # read in first number
                if self.current_result:
                    self.fact.call_operation()
                    self.current_second_number = self.current_result

                self.get_operand()              # read in operand
                self.fact.call_operation()

                if self.current_operand:
                    self.get_number()
                    self.fact.call_operation()
                    self.current_second_number = self.current_result
                    self.get_operand()
                    self.fact.call_operation()


        except ExitLoop:
            print("Bye :)")
            pass


    def initialize(self):                   # at start to print the instructions and allowed operands
        print(f'Wilkommen im Kalkulator!\nZahlen und Operanden können nacheinander eingegeben werden'
              f'\nErlaubte Operanden (ohne Klammern):\n')
        for key in OperationFactory.dict_operations.keys():
            print(key)
        print(f'\nFür Abbruch jederzeit E eingeben\n')


    def get_number(self):                   # method to read in number, check correct number format
        self.current_first_number = self.current_second_number
        check = False
        while not check:                         # loop until correct number format or terminated by user
            current_input = input('Zahl eingeben:\n')
            if current_input == 'E':
                raise ExitLoop

            else:
                try:
                    self.current_second_number = float(current_input)
                    self.current_result = self.current_second_number
                    check = True
                except ValueError:
                    print('Zahl darf int oder float sein')              # incorrect format, ask for new input


    def get_operand(self):                  # method to read in operand, check if allowed operand
        check = False
        while not check:                         # loop until allowed operand input or terminated by user
            self.current_operand = input('Operand eingeben:\n')
            check = True
            if self.current_operand == 'E':
                raise ExitLoop

            elif self.current_operand not in self.allowed_operands_list:    # check operand if allowed
                print(f'Erlaubte Operanden:\n')
                for key in OperationFactory.dict_operations.keys():         # print out allowed operands
                    print(key)



class Operation(ABC):                   # abstract class to make sure operation is implemented
    def do_operation(self):             # eventual new operation must be added here as subclass
        pass


class Addition(Operation):
    def do_operation(self):
        Calculator().current_result = Calculator().current_first_number + Calculator().current_second_number


class Subtraktion(Operation):
    def do_operation(self):
        Calculator().current_result = Calculator().current_first_number - Calculator().current_second_number


class Multiplikation(Operation):
    def do_operation(self):
        Calculator().current_result = Calculator().current_first_number * Calculator().current_second_number


class Dividieren(Operation):
    def do_operation(self):
        Calculator().current_result = Calculator().current_first_number / Calculator().current_second_number


class Ergebnis(Operation):
    def do_operation(self):
        print(f'Ergebnis:\n{Calculator().current_result}')
        Calculator().current_result = 0
        Calculator().current_operand = None


class OperationFactory:     # called as Calculator is initialized, this class will initialize and execute the ops
    # initialized = False     # to make sure initialized only once
    # operations = {}         # dictionary to store and call initialized operations

    dict_operations = {('+', 'add', 'plus'): Addition(),            # allowed operands and the respective operations
                       ('-', 'sub', 'minus'): Subtraktion(),        # eventual new operations and operands have to be
                       ('*', 'mal'): Multiplikation(),              # added here
                       ('/', 'div'): Dividieren(),
                       ('=', 'ergebnis'): Ergebnis()}

    def __init__(self):
        for i in self.dict_operations.values():
            i

    # to initialize operations
        # if not self.initialized:
        #     self.initialized = True
        #     for value in self.dict_operations.values():
        #         operation_name = value                          # this is used later to call the ops
        #         operation_instance = eval(value)()              # ops initialized
        #         self.operations[value] = operation_instance     # the initialized ops added to a dict

    def call_operation(self):                                   # execute op based on the last input operand
        for k, v in self.dict_operations.items():
            if Calculator().current_operand in k:
                return v.do_operation()


if __name__ == '__main__':
    a = Calculator()
    a.calculate()