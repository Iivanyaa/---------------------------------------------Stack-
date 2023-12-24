class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items ==     []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def is_balanced(self, input_string):
        stack = []
        opening_brackets = ['(', '[', '{']
        closing_brackets = [')', ']', '}']
        
        for char in input_string:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if not stack:
                    print("Несбалансированно")
                    return False
                if opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                    print("Несбалансированно")
                    return False
        print("Сбалансированно")
        return len(stack) == 0


print('Введите строку со скобками')
TestStack = Stack()
input_string = input()
TestStack.is_balanced(input_string)