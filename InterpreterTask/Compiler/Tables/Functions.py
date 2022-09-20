import re
import pickle


class Functions:
    """
    class that contains all the functions that will be executed in the interpreter.
    you can add functions and they will be found (CASE SENSITIVE)
    """

    @staticmethod
    def isfunction(name) -> bool:
        """
        checks if the functions exists in the functions class
        Args:
            name: name of the function to check

        Returns: True if the function exists false otherwise

        """
        return hasattr(Functions, name)

    @staticmethod
    def callfunction(name, parameters):
        """
        call a function dynamicly from the functions
        Args:
            name: name of the function to be called
            parameters: parameters of the function to be called

        """
        func = getattr(Functions, name)
        return func(*parameters)

    #
    @staticmethod
    def Regex(value, expression) -> bool:
        """
        match regeular expression with the value
        Args:
            value: value to be matched
            expression: regular expression to be matched

        Returns: true if the regular expression is matches false otherwise

        """
        if re.search(expression, value) is None:
            return False
        return True

    @staticmethod
    def Model(value: str, model_type:str, file_name):
        """
        loads a liner model from file and classify the value into +ve or -ve
        Args:
            value: value to be classified
            model_type: model type SVM/Perceptron
            file_name: name of the file to load the model from

        Returns: +ve or -ve based on the classification

        """
        with open(file_name, 'rb') as file:
            model = pickle.load(file)

        features = value.split("#")
        return model.predict(features)
