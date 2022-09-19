import re
import pickle


class Functions:
    @staticmethod
    def isfunction(name):
        return hasattr(Functions, name)

    @staticmethod
    def callfunction(name, parameters):
        func = getattr(Functions, name)
        return func(*parameters)

    # you can add functions as much as you want and it will be found dynamicly (CASE SENSITIVE)
    @staticmethod
    def Regex(value, expression):
        if re.search(expression, value) is None:
            return False
        return True

    @staticmethod
    def Model(value: str, model_type, file_name):
        model = pickle.load(open(file_name, 'rb'))
        x = value.split("#")
        return model.predict(x)
