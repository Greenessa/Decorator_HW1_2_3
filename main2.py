import os
from functools import wraps

def logger(path):

    def __logger(old_function):
        import datetime
        @wraps(old_function)
        def new_function(*args, **kwargs):
            dt = datetime.datetime.now()
            return_name_func = old_function.__name__
            return_value = old_function(*args, **kwargs)
            b = str(args) + str(kwargs)

            with open(path, "a", encoding="utf-8") as f:
                f.write(f'{dt} \n')
            with open(path, "a", encoding="utf-8") as f:
                f.write(f'{return_value} \n')
                f.write(f'Имя функции {return_name_func} \n')
                f.write(f'Передаваемые функции аргументы: {b} \n')
            return return_value
        return new_function

    return __logger

# @logger(path="main2.log")
# def sum1(a,b):
#     s = a+b
#     return s
# summa = sum1(3,2)

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path, encoding="utf-8") as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()