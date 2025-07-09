class Node:
    def __init__(self,data=0):
        if data ==0 :
            data=int(input("enter the data of the node"))
        self.left=None
        self.right=None
        self.data=data

class BST:
    def __init__(self):
        self.root=None
    
        print("an empty tree is created")

    def add_Node(self,key):
        new_node=Node(key)
        if self.root is None:
            self.root=new_node
            return
        current=self.root
        while True:
            if current.data <key:
                if current.right is None:
                    current.right=new_node
                    break
               

                current=current.right
            else:
                if current.data >key:
                    if current.left is None:
                        current.left=new_node
                        break
                    
                    current=current.left
    def inorder(self,current):
        if current is None:
            return
        self.inorder(current.left)
        print(current.data,end=' ')
        self.inorder(current.right)

    def preorder(self,current):
        if current is None:
            return
        print(current.data,end=' ')
        self.preorder(current.left)
        self.preorder(current.right)
    
    def postorder(self,current):
        if current is None:
            return
        self.postorder(current.left)
        self.postorder(current.right)
        print(current.data,end=' ')

    def search(self,key):
    
        current= self.root
        while current:
            if key==current.data:
                print(f"value {key} is found")
                return True
            else:
                if key<current.data:
                    current=current.left
                   
                else:
                    current=current.right
        print(f"value {key} not found")
        return False 

    #def delete (self,key):
        #current = self.root
        #if current is None:
         #   return

class Menu:
    def __init__(self):
        self.choice=0
        self.bst=BST()

    def is_empty(self):
        if self.bst.root is None:
            print("tree is empty")
            return True
        return False
    
    def menu(self):
        match self.choice:
            case 1:
                key = int(input("Enter value to insert: "))
                self.bst.add_Node(key)
            case 2:
                if self.is_empty():
                    return
                self.bst.inorder(self.bst.root)
            case 3:
                if self.is_empty():
                    return
                self.bst.preorder(self.bst.root)
            case 4:
                if self.is_empty():
                    return
                self.bst.postorder(self.bst.root)
            case 5:
                if self.is_empty():
                    return
                key=int(input("enter the element to be searched:"))
                found=self.bst.search(key)
                if found:
                    print(f"value {key} is found")
                else:
                    print(f"value {key} is not found")
           # case 6:
            #    if self.is_empty(bst):
             #       return
              #  delete=int(input("enter the element to e deleted:"))
               # bst.delete(bst.root,bst.data)
            case 7:
                print("exiting program")
                exit()

            case _:
                print("invalid choice")
    def start_app(self):
        
        while True:
            print("1:Instert 2:inorder 3:preorder 4:postorder 5:search 6:delete 7:exit")
            self.choice=int(input("enter your choice:"))
            self.menu()
            

menu=Menu()
menu.start_app()

                


    
    

            