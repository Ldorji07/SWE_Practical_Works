def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:  
            b, a = stack.pop(), stack.pop()
            result = eval(f"{a} {token} {b}")
            stack.append(result)
    return stack.pop()

print(evaluate_postfix("3 4 + 2 * 7 /"))  

class QueueWithTwoStacks:
    def __init__(self):
        self.stack1, self.stack2 = [], []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

queue = QueueWithTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  

def task_scheduler(tasks):
    queue = tasks[:]
    while queue:
        print(f"Processing task: {queue.pop(0)}")

task_scheduler(["Task 1", "Task 2", "Task 3"])

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack, output = [], []
    
    for token in expression.split():
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:
            while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)

    output.extend(reversed(stack))
    return ' '.join(output)

print(infix_to_postfix("A + B * C"))  
