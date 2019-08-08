class SingleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """将新的值附加到链表尾部。"""
        newnode = SingleLinkedListNode(obj, None, self.end)
        if self.end is not None:
            self.end.next = newnode
        else:
            self.begin = newnode
        self.end = newnode

    def pop(self):
        """移除最后一个元素并返回它。"""
        if self.begin is None:  # zero element
            return None

        lastnode = self.end
        node = self.begin

        if node.next is None:  # 1 element
            self.begin = None
            self.end = None
            return lastnode.value

        while node.next != lastnode:
            node = node.next
        node.next = None
        self.end = node
        return lastnode.value

    def shift(self, obj):
        """将新的值附加到链表头部。"""
        newnode = SingleLinkedListNode(obj, self.begin, None)
        if newnode.next is None:  # 1 element
            self.end = newnode
        self.begin = newnode

    def unshift(self):
        """移除第一个元素并返回它。"""
        if self.begin is None:
            return None
        firstnode = self.begin
        self.begin = firstnode.next
        return firstnode.value

    def remove(self, obj):
        """寻找匹配的元素并从中移除。"""
        if self.begin is None:  # 0 element
            return None
        if self.begin == self.end:  # 1 element
            if self.begin.value == obj:
                self.begin = None
                self.end = None
                return 0
            return None

        node = self.begin
        prevnode = None
        i = 0
        while node is not None:
            if node.value == obj:
                if self.begin == node:
                    self.begin = node.next
                    return 0
                if self.end == node:
                    self.end = prevnode
                    prevnode.next = None
                    return i
                prevnode.next = node.next
                return i
            prevnode = node
            if node.next is None:
                return None
            node = node.next
            i = i+1

    def first(self):
        """返回第一个元素的*引用*，不要移除。"""
        if self.begin is None:
            return None
        return self.begin.value

    def last(self):
        """返回最后一个元素的*引用*，不要移除。"""
        if self.end is None:
            return None
        return self.end.value

    def count(self):
        """计算链表中的元素数量。"""
        node = self.begin
        i = 0
        if node is None:
            return 0
        while node is not None:
            node = node.next
            i = i+1
        return i

    def get(self, index):
        """获取下标处的值。"""
        if self.begin is None:
            return None
        i = 0
        node = self.begin
        while i < index:
            node = node.next
            i = i+1
            if node is None:
                return None
        return node.value

    def dump(self, mark):
        """转储链表内容的调试函数。"""
        print(mark, end=' ')
        if self.begin is None:
            print('Empty')
            return
        node = self.begin
        while node.next is not None:
            print(node.value, end=' ')
            node = node.next
        print(node.value)
