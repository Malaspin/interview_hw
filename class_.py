class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not self.stack
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        try:
            result = self.stack.pop()
            return result
        except IndexError:
            return None

    def peek(self):
        try:
            result = self.stack[-1]
            return result
        except IndexError:
            return None

    def size(self):
        len_stack = len(self.stack)
        return len_stack
    
        

    
    