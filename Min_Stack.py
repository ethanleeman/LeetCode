class Node(object):
    def __init__(self):
        self.next = None
        self.value = None

class MinStack(object):


    def __init__(self):
        """
        initialize your data structure here.
        """
        self.top_node = None
        self.d = {}

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        new_node = Node()
        new_node.value = x
        new_node.next = self.top_node
        self.top_node = new_node

        if (x in self.d.keys()):
            self.d[x] += 1
        else:
            self.d[x] = 1

    def pop(self):
        """
        :rtype: None
        """
        return_node = self.top_node
        return_value = return_node.value
        self.top_node = return_node.next
        return_node.next = None
        if (self.d[return_value] == 1):
            del self.d[return_value]
        else:
            self.d[return_value] -= 1

        return return_value

    def top(self):
        """
        :rtype: int
        """
        n = self.top_node
        v = n.value
        return v

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.d.keys())
        
