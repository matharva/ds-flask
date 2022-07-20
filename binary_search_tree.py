from turtle import left, right
from typing_extensions import dataclass_transform


class Node: 
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None 

    def _insert_recursive(self, data, node):
        if data["id"] < node.data["id"]:
            if node.left is None: 
                # self._insert_recursive(data, node.left)
                node.left = Node(data)
            else: 
                self._insert_recursive(data, node.left)

        if data["id"] > node.data["id"]:
            if node.right is None: 
                node.right = Node(data)
            else: 
                self._insert_recursive(data, node.right)

        else: 
            return 

    def _search_recursive(self, blog_post_id, node):
        if node.data["id"] == blog_post_id:
            return node.data    
        
        if node.data["id"] > blog_post_id and node.left is not None:
            if blog_post_id == node.left.data["id"]:
                return node.left.data 
            
            return self._search_recursive(blog_post_id, node.left)

        if node.data["id"] < blog_post_id and node.right is not None:
            if blog_post_id == node.right.data["id"]:
                return node.right.data
            return self._search_recursive(blog_post_id, node.right)

        return None


    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)

        if self.root is None: 
            return False
        
        return self._search_recursive(blog_post_id, self.root)

    def insert(self, data):
        if self.root is None: 
            self.root = Node(data)
        else: 
            self._insert_recursive(data, self.root)