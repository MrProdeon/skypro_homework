from functools import wraps
import os


def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                message = f'Успех! Имя функции : {func_name}\nРезультат : {result}'
            except Exception as e:
                arguments = args, kwargs
                error = e
                message = f'Исключение!\nИмя функции : {func_name}\nОшибка : {error}\nВходные параметры : {arguments}'
                result = None
            if filename:
                name_file = os.path.join(os.path.dirname(os.path.dirname(__file__)),'data', filename)
                with open(name_file, 'a', encoding='UTF-8') as file:
                    file.write(message + '\n')
            else:
                print(message)
            return result




        return inner
    return wrapper