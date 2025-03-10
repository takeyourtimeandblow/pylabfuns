def are_ids_same(id_func1, id_func2):
    if id_func1 == id_func2:
        return "same"
    return "not same"


valuable: int = 12 # int неизменяемый тип данных, поэтому при любых операциях будет создаваться новый объект
id0 = id(valuable)
addition: int = 1

valuable = valuable + addition # создаёт новый объект
id1 = id(valuable)
print(f'{are_ids_same(id0, id1)}: {id0} {id1}') # id разные
id0 = id1
valuable += addition # создаёт новый объект
id1 = id(valuable)
print(f'{are_ids_same(id0, id1)}: {id0} {id1}') # id разные

valuable1 = list([1, 2, 3])
"""
list изменяемый тип данных,
поэтому при += новый объект создаваться не будет
однако при присваивании (=) будет создаваться новый объект в любом случае
"""
id0 = id(valuable1)
addition1 = list([4, 5, 6])

valuable1 = valuable1 + addition1 # создаёт новый объект
id1 = id(valuable1)
print(f'{are_ids_same(id0, id1)}: {id0} {id1}') # id разные
id0 = id1
valuable1 += addition1 # изменяет объект, не меняя его id
id1 = id(valuable1)
print(f'{are_ids_same(id0, id1)}: {id0} {id1}') # id одинаковые

