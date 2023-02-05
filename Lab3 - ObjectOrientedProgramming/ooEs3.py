import re

regex_aritmetical_operands_pattern = re.compile("\\d+")
regex_boolean_operands_pattern = re.compile("T|F")
regex_aritmetical_operators_pattern = re.compile("[+\\-*/]")
regex_boolean_operators_pattern = re.compile("or|and|not")
class PolishCalculator:
    def __init__(self):
        self._stack = list()

    def __str__(self): pass

    def eval(self, str):
        splitted = str.split()
        if not regex_boolean_operands_pattern.fullmatch(splitted[0]).__eq__(None):
            regex_operands = regex_boolean_operands_pattern
            regex_operators = regex_boolean_operators_pattern
            self._stack.append(splitted[0])
        elif not regex_aritmetical_operands_pattern.fullmatch(splitted[0]).__eq__(None):
            regex_operands = regex_aritmetical_operands_pattern
            regex_operators = regex_aritmetical_operators_pattern
            self._stack.append(splitted[0])
        else:
            raise ValueError

        #for i in range(1, len(splitted)):
         #   if

