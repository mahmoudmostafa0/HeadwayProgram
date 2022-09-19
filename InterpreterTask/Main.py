from datetime import datetime

from Compiler.Interpreter import Interpreter
from Compiler.Lexer import Lexer
from Compiler.Tables.Variables import Variables
from Compiler.Parser import Parser
from Input.CSVReader import CSVReader
from Output.MySqlDataSink import MySqlDataSink


def main():
    data_sink = MySqlDataSink("localhost", "root", "root", "task1")
    reader = CSVReader("input.txt")
    with open("equation.config", 'r') as f:
        equation = f.read()
    lexer = Lexer(equation)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    while not reader.is_data_finished():
        message = reader.get_next()
        Variables.add_or_update("ATTR", message.value)
        result = interpreter.interpret()
        interpreter.reset()  ##reset intercepter to be able to add another input
        message.timestamp = str(datetime.now())
        message.value = result
        data_sink.add_new_entry(message)
    data_sink.close()


if __name__ == '__main__':
    main()
