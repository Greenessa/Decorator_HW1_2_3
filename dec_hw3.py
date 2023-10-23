from main2 import logger



@logger(path="log_4.log")
def flat_list_gen(some_list):
    list_new = []
    for l in some_list:
        if isinstance(l, list):
            yield from flat_list_gen(l)
        else:
            yield l
list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
sp=flat_list_gen(list_of_lists_1)