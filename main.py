from class_ import Stack

def balance(data):
    stack = Stack()
    open_parenthesis = ('(', '[', '{')
    close_parenthesis = (')', ']', '}')
    key_dict = dict(zip(close_parenthesis, open_parenthesis))

    for d in data:
        if d in open_parenthesis:
            stack.push(d)
        elif d in close_parenthesis:
            if key_dict.get(d) == stack.peek():
                stack.pop()
            else:
                return 'Несбалансированно'
        else:
            return 'Несбалансированно'
    if not stack.is_empty():
        return 'Несбалансированно'
    return 'Сбалансированно'

