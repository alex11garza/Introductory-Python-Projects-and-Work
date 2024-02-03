#  File: Josephus.py
#  Student Name: Saurelle Ngaintse Jiotsa
#  Student UT EID: SN26524
#  Partner Name: Alex Garza
#  Partner UT EID: ang3489

import sys

# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data):
        new_node=Link(data)
        if self.is_empty():
            self.first=new_node
            self.last=new_node
            self.last.next=self.first
        else:
            self.last.next=new_node
            self.last=new_node
            new_node.next=self.first

    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        if self.is_empty():
            return None
        else:
            current_node=self.first
            while current_node.next!=self.first:
              if current_node.data==data:
                return current_node
              else:
                current_node=current_node.next
            if current_node.data==data:
              return current_node
            else:
              return None
      
    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):
        if (self.is_empty() or self.find(data) is None):
          return None
        else:          
          if self.first==self.last:
              self.first=None
              return self.first
          else:
              current_node=self.first
              del_node=self.find(data)
              while current_node!=del_node:
                  previous_node=current_node
                  current_node=current_node.next
              if current_node==self.first:
                  self.first=self.first.next
                  self.last.next=self.first
              elif current_node==self.last:
                  previous_node.next=self.first
                  self.last=previous_node
              else:
                  previous_node.next=previous_node.next.next
          return current_node   
  
    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):
        if self.is_empty() or self.find(start) is None:
          return None
        elif self.first==self.last:
            return self.first.data, self.last
        else:         
          temp4=self.first
          while temp4.data!=start:
              prev_node=temp4              
              temp4=temp4.next  
          current_node1=temp4
        if step==1:      
            if current_node1==self.first:
                  self.first=self.first.next
                  self.last.next=self.first
            elif current_node1==self.last:
                prev_node.next=self.first
                self.last=prev_node
            else:
                prev_node.next=prev_node.next.next  
            return current_node1.data, current_node1.next
        elif step>1:
            for i in range(1,step-1):
                current_node1=current_node1.next
            if current_node1.next==self.first:
                temp4=current_node1.next
                current_node1.next=self.first.next
                self.first=self.first.next
                return temp4.data, self.first
            elif current_node1.next==self.last:
                temp5=current_node1.next
                current_node1.next=self.first
                self.last=current_node1
                return temp5.data, self.last.next
            else:              
                temp=current_node1.next
                current_node1.next=current_node1.next.next
                return temp.data, temp.next
        else:
          return None

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        if self.is_empty():
            return '[]'
        else:
            string='['
            current_node=self.first
            while current_node!=self.last:
                string=string+str(current_node.data)+ ', '
                current_node=current_node.next
            string=string+str(current_node.data)+']'
            return string

# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):
    cir_list=CircularList()
    for k in range (1,num_soldiers+1):
        cir_list.insert(k)
    return cir_list

# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    my_list=create_circular_list(num_soldiers)
    #print(my_list)
    current_start_pos=my_list.find(start_data)
    while (my_list.first!=my_list.last): 
        deleted_node,next_current_start_pos=my_list.delete_after(current_start_pos.data,step_count)
        print(deleted_node)
        current_start_pos=next_current_start_pos
    print(current_start_pos)


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()
