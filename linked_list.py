class Node: 
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None

    def to_list(self):
        arr =[]

        if self.head is None:
            return None    
    
        node = self.head
        while node.next_node is not None:
            arr.append(node.data)
            node = node.next_node

        return arr

    def get_user_by_id(self, user_id):
        node = self.head

        while node.next_node is not None:
            if int(user_id) == node.data["id"]:
                return node.data
            node = node.next_node

        return None

    def print_ll(self):
        ll_string = ""
        node = self.head

        if node is None: 
            print(None)
        
        while node: 
            ll_string += f"{node.data} -> "
            node = node.next_node  

        ll_string += " None"
        print(ll_string)

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        
        new_node = Node(data=data, next_node=self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if not self.head:
            self.insert_beginning(data)

        if self.last_node is None: 
            temp = self.head

            while temp.next_node:
                temp = temp.next_node

            new_node = Node(data, temp)
            temp.next_node = new_node
            self.last_node = new_node
        
        else: 
            self.last_node.next_node = Node(data, None)
            self.last_node = self.last_node.next_node
        
        