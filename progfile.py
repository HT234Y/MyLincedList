      
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def push(self, value):
        previousHead = self.head
        newElement = Element(value, previousHead)
        if self.head == None:
            self.tail = newElement
        
        self.head = newElement
        self.len += 1

    def pushBack(self, value):
        newTail = Element(preLastElement.next)
        currentTail = self.head
        currentTail.next = newTail
        self.tail = newTail
        self.len += 1

    def last(self):
        currentLast = self.head
        
        while currentLast.next != None:
            currentLast = currentLast.next

        return currentLast

    def lengthSlow(self):
        current = self.head
        len = 0

        while current.next != None:
            current = current.next
            len += 1

        return len

    def length(self):
        return self.len

    def elementAt(self, position):
        currentPosition = 0
        current = self.head
        
        while current.next != None and position > currentPosition:
            current = current.next
            currentPosition += 1

        return current

    def deleteAt(self):
        pass

    def max(self):
        current = self.head
        currentPosition = 0

        maxElement = current
        maxCurrentPosition = currentPosition

        while current.next != None:
            current = current.next
            currentPosition += 1

            if current.value > maxElement.value : 
                maxElement = current
                maxCurrentPosition = currentPosition

        return maxElement            


class Element:

    def __init__(self, value, nextElement):
        self.value = value
        self.next = nextElement

    
# TODO: push back


lis = MyLinkedList()
lis.push(10)
lis.push(111)
lis.push(11)
lis.push(7)

#print(lis.length())
print(lis.max().value)
#print(lis.elementAt(1).value)

insertHere = lis.head.next.next

three = Element(3, insertHere.next)
insertHere.next = three

#print(lis.head.next.next.value)
#print(lis.head.next.next.next.value)

#list.pushBack(9)
#print(list.last().value) #should be 9

#print(list.last().value)
