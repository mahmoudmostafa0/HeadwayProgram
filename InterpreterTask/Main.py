from datetime import datetime
from Compiler.interpreter import Interpreter
from Compiler.lexer import Lexer
from Compiler.Tables.Variables import Variables
from Compiler.parser import Parser
from Input.csv_reader import CSVReader
from Output.mysql_data_sink import MySqlDataSink


def main():
    """
    main function
    """
    data_sink = MySqlDataSink("localhost", "root", "root", "task1")
    reader = CSVReader("input.txt")
    with open("equation.config", 'r') as file:
        equation = file.read()
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
