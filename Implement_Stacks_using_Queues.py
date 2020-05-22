from collections import deque

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_1 = deque()
        self.queue_2 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if (len(self.queue_1) == 0):
            self.queue_2.append(x)
        else:
            self.queue_1.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """

        if (len(self.queue_1) == 0):
            while(len(self.queue_2) > 1):
                val = self.queue_2.popleft()
                self.queue_1.append(val)
            return self.queue_2.popleft()
        else:
            while(len(self.queue_1) > 1):
                val = self.queue_1.popleft()
                self.queue_2.append(val)
            return self.queue_1.popleft()
        throw("Stack Underflow")

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        val = self.pop()
        self.push(val)
        return val

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue_1) + len(self.queue_2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
