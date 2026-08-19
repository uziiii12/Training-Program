class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        head=Node(10)
        second=Node(20)
        third=Node(30)
        forth=Node(40)
        head.next=second
        second.next=third
        third.next=forth
