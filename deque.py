from collections import deque

dq = deque(range(10), maxlen=11)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(3)
print(dq)
dq.appendleft(-1)
print(dq)
# will not work as we are using int in this one
# dq.appendleft("a"))
# print(dq)
# dq.appendleft(1.5))
# print(dq)
dq.append(11)
print(dq)
dq.extend([3,2,66])
print(dq)
dq.extendleft((22,33,44))
print(dq)

dq2 = deque(("a","b","c"), maxlen=4)
print(dq2)

#::todo
# This provides the synchronized (i.e., thread-safe) classes SimpleQueue, Queue,
# LifoQueue, and PriorityQueue. These can be used for safe communication
# between threads. All except SimpleQueue can be bounded by providing a max
# size argument greater than 0 to the constructor. However, they don’t discard
# items to make room as deque does. Instead, when the queue is full, the insertion
# of a new item blocks—i.e., it waits until some other thread makes room by taking
# an item from the queue, which is useful to throttle the number of live threads.
# multiprocessing
# Implements its own unbounded SimpleQueue and bounded Queue, very similar
# to those in the queue package, but designed for interprocess communication. A
# specialized multiprocessing.JoinableQueue is provided for task management.
# asyncio
# Provides Queue, LifoQueue, PriorityQueue, and JoinableQueue with APIs
# inspired by the classes in the queue and multiprocessing modules, but adapted
# for managing tasks in asynchronous programming.
# heapq
# In contrast to the previous three modules, heapq does not implement a queue
# class, but provides functions like heappush and heappop that let you use a muta‐
# ble sequence as a heap queue or priority queue.