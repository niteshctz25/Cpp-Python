def createStack():
    stack = []
    return stack

def is_empty(stack):
    return len(stack) == 0

def push(stack,data):
    stack.append(data)
    print("Pushed item: " + data)

def pop(stack):
    if (is_empty(stack)):
        return "Stack is empty"
    return stack.pop()

stack = createStack()
push(stack, str(1))
push(stack, str(2))
print("popped item: " + pop(stack))
print("popped item: " + pop(stack))
print("popped item: " + pop(stack))


    