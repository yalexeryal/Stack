from class_stack import Stack

def is_valid(lines):
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    open_par = Stack()

    if len(lines) % 2 > 0:
        return 'Несбалансированно'

    for i, char in enumerate(lines):
        if char in opening:
            open_par.push(char)
        elif char in closing:
            if open_par.is_empty():
                return 'Несбалансированно'
            elif opening.index(open_par.peek()) != closing.index(char):
                return 'Несбалансированно'
            else:
                open_par.pop()
                if open_par.is_empty() and i == len(lines)-1:
                    return 'Сбалансированно'



if __name__ == '__main__':
    print(is_valid(input('Введите строку')))