class Stack:
    def __init__(self):
        self.line = input(str("Введите строку: \n"))
        self.stack = []
        self.flag = True

    def is_empty(self):
        if not self.stack:
            return True

    def push(self, element):
        return self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def analyze(self):
        for el in self.line:
            if el in "({[":
                self.push(el)
            elif el in ")}]":
                if self.size() == 0:
                    self.flag = False
                    break

                stack_el = self.pop()
                if stack_el == "(" and el == ")":
                    continue
                if stack_el == "[" and el == "]":
                    continue
                if stack_el == "{" and el == "}":
                    continue

                self.flag = False
                break

        if self.flag and self.is_empty():
            print("Сбалансировано")
        else:
            print("Несбалансированно")


line = Stack()
line.analyze()
