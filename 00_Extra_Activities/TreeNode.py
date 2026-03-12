class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
# YOU CAN TEST THE CLASS LIKE THIS:
# node1 = TreeNode("R")
# print(node1.value)   # "R"
# print(node1.left)    # None
# print(node1.right)   # None

# node2 = TreeNode("A")
# print(node2.value)   # "A"

class BinaryTree:
    # add 
    def __init__(self, root_value):
        self.root = TreeNode(root_value)   # Kökü oluştur
    
    # ---   ADD  ---
    def insert_left(self, current_node, new_value):
        new_node = TreeNode(new_value)          # Yeni düğüm oluştur
        if current_node.left is None:           # Sol boşsa
            current_node.left = new_node        #   direkt yerleştir    
        else:                                   # Sol doluysa
            new_node.left = current_node.left   #   eskiyi kurtar
            current_node.left = new_node        #   yeniyi yerleştir
    
    def insert_right(self, current_node, new_value):
        new_node = TreeNode(new_value)
        if current_node.right is None:
            current_node.right = new_node
        else:
            new_node.right = current_node.right
            current_node.right = new_node
    
    # --- Travel ---
    def pre_order_traversal(self, start_node, visit_list):
        if start_node is None:                  # Durdurma noktası
            return
        visit_list.append(start_node.value)     # ÖNCE kaydet
        self.pre_order_traversal(start_node.left, visit_list)   # Sol
        self.pre_order_traversal(start_node.right, visit_list)  # Sağ
    
    def in_order_traversal(self, start_node, visit_list):
        if start_node is None:
            return
        self.in_order_traversal(start_node.left, visit_list)    # Sol
        visit_list.append(start_node.value)     # ORTADA kaydet
        self.in_order_traversal(start_node.right, visit_list)   # Sağ
    
    def post_order_traversal(self, start_node, visit_list):
        if start_node is None:
            return
        self.post_order_traversal(start_node.left, visit_list)  # Sol
        self.post_order_traversal(start_node.right, visit_list) # Sağ
        visit_list.append(start_node.value)     # EN SON kaydet


# PARÇA 3: Ağacı inşa et ve test et
bt = BinaryTree('R')

bt.insert_left(bt.root, 'A')
bt.insert_right(bt.root, 'B')

nodeA = bt.root.left
nodeB = bt.root.right

bt.insert_left(nodeA, 'C')
bt.insert_right(nodeA, 'D')
bt.insert_left(nodeB, 'E')
bt.insert_right(nodeB, 'F')

nodeF = nodeB.right
bt.insert_left(nodeF, 'G')

pre = []
bt.pre_order_traversal(bt.root, pre)
print("Pre-order: ", pre)     # [R, A, C, D, B, E, F, G]

ino = []
bt.in_order_traversal(bt.root, ino)
print("In-order:  ", ino)     # [C, A, D, R, E, B, G, F]

post = []
bt.post_order_traversal(bt.root, post)
print("Post-order:", post)    # [C, D, A, E, G, F, B, R]


# ADIM 1: TreeNode yaz (5 satır)
#   class TreeNode:
#       def __init__(self, value):
#           self.value = value
#           self.left = None
#           self.right = None

# ADIM 2: BinaryTree yaz
#   class BinaryTree:
#       def __init__(self, root_value):
#           self.root = TreeNode(root_value)

# ADIM 3: insert_left yaz
#   Yeni düğüm oluştur
#   Sol boşsa → yerleştir
#   Sol doluysa → eskiyi kurtar, yeniyi yerleştir

# ADIM 4: Traversal yaz (3 satırlık iş)
#   None mı → return
#   3 işlem yap: kaydet + sol git + sağ git
#   Bu 3 işlemin SIRASI traversal türünü belirler:
#     Pre:  kaydet, sol, sağ
#     In:   sol, kaydet, sağ
#     Post: sol, sağ, kaydet