# https://www.acmicpc.net/problem/5397
# 알고보니 연결리스트가 아니라 스택으로 푸는거였던거임;

class Node(object):

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail
        self.cursor = 0

    def traverse(self):
        res = []
        curr = self.head
        while curr.next:
            curr = curr.next
            res.append(curr.data)
        return res

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            raise IndexError
        curr = self.head
        i = 0
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next == None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):

        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        curr = prev.next
        if curr == None:
            raise IndexError
        prev.next = curr.next
        self.nodeCount -= 1
        return curr

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    def moveCursor(self, lr):
        if lr == +1:
            self.cursor = self.cursor + 1 if self.cursor < self.nodeCount else self.cursor
        elif lr == -1:
            self.cursor = self.cursor - 1 if self.cursor > 0 else 0
        else:
            raise ValueError

    def backspace(self):
        if self.cursor > 0:
            self.popAt(self.cursor)
            self.cursor -= 1

    def charIn(self, charactor):
        self.insertAt(self.cursor + 1, Node(charactor))
        self.cursor += 1


# ll = LinkedList()
# ll.charIn('a')
# ll.moveCursor(-1)
# ll.moveCursor(1)
# # print(ll.nodeCount)
# # print(ll.cursor)
# print(ll.traverse(), ll.nodeCount)

N = int(input())
for _ in range(N):
    keyLog = input()
    passwordLL = LinkedList()
    for c in keyLog:
        # print('charactor:' + c)
        if c == '<':
            passwordLL.moveCursor(-1)
        elif c == '>':
            passwordLL.moveCursor(+1)
        elif c == '-':
            passwordLL.backspace()
        else:
            passwordLL.charIn(c)
        # print('paswordLL:', passwordLL.traverse())
        # print('cursor:' + str(passwordLL.cursor))
        # print('------------------------------')
    print(''.join(passwordLL.traverse()))
