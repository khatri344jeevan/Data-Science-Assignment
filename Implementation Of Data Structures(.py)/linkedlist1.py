from collections import deque
linked_list = deque()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

print("Linked List:",list(linked_list))
linked_list.appendleft(5)
print("After inserting at beginning:",list(linked_list))
linked_list.pop()
linked_list.popleft()
print("After removals:",list(linked_list))