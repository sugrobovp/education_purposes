def call_decorator(func):
    """ Декоратор, который будет логировать все вызовы функции и выводить информацию о них в консоль. """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} была вызвана с args: {args} и kwargs: {kwargs}')
        return result

    return wrapper


@call_decorator
def square_func(x, y):
    return x * y

