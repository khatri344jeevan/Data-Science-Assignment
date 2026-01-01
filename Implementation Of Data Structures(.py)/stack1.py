from collections import deque
stack = deque()
stack.append("a")
stack.append("b")
stack.append("c")
stack.append("r")
stack.append("e")

print("Elements popped")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("Stack:",list(stack))