#декоратор, который записывает в файл 'main.log' дату и время вызова функции,
#имя функции, аргументы, с которыми вызвалась функция, и возвращаемое значение

import os

def logger(old_function):
    import datetime

    def new_function(*args, **kwargs):
        dt = datetime.datetime.now()
        return_name_func = old_function.__name__
        return_value = old_function(*args, **kwargs)
        b = args
        с = kwargs

        with open("main.log", "a", encoding="utf-8") as f:
            f.write(f'{dt} \n')
        with open("main.log", "a", encoding="utf-8") as f:
            f.write(f'{return_value} \n')
            f.write(f'Имя функции {return_name_func} \n')
            f.write(f'Передаваемые функции аргументы args: {b} \n')
            f.write(f'Передаваемые функции аргументы kwargs: {с} \n')
        return return_value
    return new_function

# @logger
# def sum1(a,b):
#     s = a+b
#     return s
# summa = sum1(3,2)


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path, encoding="utf-8") as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()


