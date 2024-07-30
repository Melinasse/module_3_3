# Пункт №1
def print_params(a=1, b='str', c=True):
    print(a, b, c)


print_params(11)
print_params(False, 1.5, (1, 2, 3))
print_params(b=25)
print_params(c=[1, 2, 3])
print_params()

# Пункт №2
values_list = [77, 3.75, True]
values_dict = {'a': 2, 'b': 'str2', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# Пункт №3
values_list_2 = [17.31, (33, True, 'str3')]
print_params(*values_list_2, 42)
