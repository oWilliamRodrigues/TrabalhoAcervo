class ListNode:
  def __init__(self, data):
      self.data = data
      self.prevNode = None
      self.nextNode = None

class DoublyLinkedListIterator:
  def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0
      self.iterator = None

  def addNode(self, data):
      new_node = ListNode(data)
      if self.head is None:
          self.head = new_node
          self.tail = new_node
          self.iterator = new_node
      else:
          new_node.prevNode = self.tail
          self.tail.nextNode = new_node
          self.tail = new_node
          self.iterator = new_node
      self.size += 1

  def insNode(self, data, position):
      if position <= 0:
          self.addNode(data)
      elif position >= self.size:
          self.addNode(data)
      else:
          new_node = ListNode(data)
          current_node = self.head
          for _ in range(1, position):
              current_node = current_node.nextNode
          new_node.prevNode = current_node.prevNode
          new_node.nextNode = current_node
          current_node.prevNode.nextNode = new_node
          current_node.prevNode = new_node
          self.size += 1
          self.iterator = new_node

  def elimNode(self):
      if self.head is not None:
          if self.head.prevNode is None:
              self.head = self.head.nextNode
              if self.head is not None:
                  self.head.prevNode = None
              self.iterator = self.head
          else:
              self.head.prevNode.nextNode = self.head.nextNode
              self.head.nextNode.prevNode = self.head.prevNode
              self.head = self.head.nextNode
              self.iterator = self.head
          self.size -= 1

  def first_Node(self):
      return self.head

  def last_Node(self):
      return self.tail

  def nextNode(self):
      if self.iterator is not None and self.iterator.nextNode is not None:
          self.iterator = self.iterator.nextNode
          return self.iterator.data
      else:
          return None

  def antNode(self):
      if self.iterator is not None and self.iterator.prevNode is not None:
          self.iterator = self.iterator.prevNode
          return self.iterator.data
      else:
          return None

  def posNode(self, position):
      if position <= 0:
          self.iterator = self.first_Node()
      elif position >= self.size:
          self.iterator = self.last_Node()
      else:
          current_node = self.head
          for _ in range(1, position):
              current_node = current_node.nextNode
          self.iterator = current_node
          return self.iterator.data

  def undefinedIterator(self):
      return self.iterator is None