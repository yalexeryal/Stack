from validator import is_valid


# Пример сбалансированных последовательностей скобок:
balanced_code1 = '(((([{}]))))'
balanced_code2 = '[([])((([[[]]])))]{()}'
balanced_code3 = '{{[()]}}'

#  Несбалансированные последовательности:
unbalanced_code1 = '}{}'
unbalanced_code2 = '{{[(])]}}'
unbalanced_code3 = '[[{())}]'

if __name__ == '__main__':
    # print(check_string(input('Введите строку')))
    print(is_valid(balanced_code1))
    print(is_valid(balanced_code2))
    print(is_valid(balanced_code3))
    print(is_valid(unbalanced_code1))
    print(is_valid(unbalanced_code2))
    print(is_valid(unbalanced_code3))
