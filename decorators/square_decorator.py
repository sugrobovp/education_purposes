def square_decorator(func):
    def wrapper(a: list):
        square_list = [x**2 for x in a]
        return square_list
    return wrapper


@square_decorator
def example(numbers: list):
    return numbers
