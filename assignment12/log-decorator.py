import logging

# Task 1 - Logger Decorator Setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# Declare a decorator called logger_decorator. This should log the name of the called function (func.__name__), the input parameters of that were passed, and the value the function returns, to a file ./decorator.log. 
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        pos_args = list(args) if args else "none"
        kw_args = dict(kwargs) if kwargs else "none"
        
        log_message = f"function: {func.__name__} positional parameters: {pos_args} keyword parameters: {kw_args} return: {result}"
        logger.log(logging.INFO, log_message)
        
        return result
    return wrapper

# Function 1: Declare a function that takes no parameters and returns nothing. Maybe it just prints "Hello, World!". Decorate this function with your decorator.
@logger_decorator
def hello_world():
    print("Hello, World!")
    return None

# Function 2: Declare a function that takes a variable number of positional arguments and returns True. Decorate this function with your decorator.
@logger_decorator
def var_pos_args(*args):
    return True

# Function 3: Declare a function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator. Decorate this function with your decorator.
@logger_decorator
def var_kw_args(**kwargs):
    return logger_decorator

# Within the mainline code, call each of these three functions, passing parameters for the functions that take positional or keyword arguments. Run the program, and verify that the log file contains the information you want.
if __name__ == "__main__":
    hello_world()
    var_pos_args(1, 2, 3, "test")
    var_kw_args(name="Jason", age=71, city="Boston")