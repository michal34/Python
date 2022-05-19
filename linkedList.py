from __future__ import annotations
from typing import Any

class ListNode:
    def _init_(self, value: Any=None, next: ListNode=None):
        self.value: Any = value
        self.next: LinkedList = next
        
        
class LinkedList:
    def _init_(self):
        
        self.head = None
        self.tail = None        
        
    def append(self, value):
        
        el = ListNode(value)
        if self.head:
            self.tail.next = el
            self.tail = self.tail.next
            
        else:
            self.head = el
            self.tail = self.head
        
    def get(self, n):
        
        head2 = self.head
        
        for i in range(n):
            head2 = head2.next
            
        return head2.value
            
    def pop(self, n):
        
        if n == 0:
            self.head = self.head.next
        else:
            left = self.head
            right = self.head
            for i in range(n-1):
                left = left.next
            if left.next.next:
                left.next = right.value
            else:
                left.next = None
                self.tail = left
        
    def insert(self, n, value):
        pass
    
    
    def remove(self, value):
        pass