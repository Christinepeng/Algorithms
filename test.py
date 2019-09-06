from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")           # Terry arrives
print(queue)
queue.append("Graham")          # Graham arrives
print(queue)
queue.popleft()                 # The first to arrive now leaves
# 'Eric'
print(queue)
queue.popleft()                 # The second to arrive now leaves
# 'John'
print(queue)
# queue
# print(queue)# Remaining queue in order of arrival
# print(dequeue)
deque(['Michael', 'Terry', 'Graham'])
# print(dequeue)