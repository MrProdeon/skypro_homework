import os
from collections.abc import Callable
from functools import wraps
from typing import Any


def log(filename: str | None = None) -> Callable:
    """
    Декоратор, который логирует информацию о выполнении функции.
    Если функция выполнена успешно - отдаст сообщение об успехе с именем функции и результатом.
    В случае исключения - отдаст имя функции, ошибку и входные параметры.
    По умолчанию отдает в консоль, но можно необязательным параметром в декоратор передать имя файла, в который
    будут записаны финальные данные.
    """
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                message = f"Успех! Имя функции : {func_name}\nРезультат : {result}"
            except Exception as e:
                arguments = args, kwargs
                error = e
                message = f"Исключение!\nИмя функции : {func_name}\nОшибка : {error}\nВходные параметры : {arguments}"
                result = None
            if filename:
                name_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", filename)
                with open(name_file, "a", encoding="UTF-8") as file:
                    file.write(message + "\n")
            else:
                print(message)
            return result

        return inner

    return wrapper
