class Variables:
    __stored_variables = {}

    @staticmethod
    def add_or_update(variable_name: str, value):
        """adds a variable to the variables table or update it if it already exist"""
        Variables.__stored_variables[variable_name] = value

    @staticmethod
    def get_value(variablename: str):
        """returns the value of the varible from the varibles table"""
        return Variables.__stored_variables.get(variablename)
