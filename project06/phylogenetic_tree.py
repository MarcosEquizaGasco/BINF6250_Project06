class Tree:
    """
    Class tree acts as a lookup table for Node objects

    Attributes:
        - nodes (dict): A dictionary of {name: Node} objects
    Methods:
        - add_node: Adds Node object to tree using the name as key and Node Object as value
        - convert_to_newick: TBD
    """
    def __init__(self, seq_ids):
      self.nodes = {}
      for seq_id in seq_ids:
          self.add_node(seq_id, [])

    def add_node(self, name, children):
      self.nodes[name] = Node(name, children)

    def convert_to_newick(self):
      pass


class Node:
    """
    Class Node represents all nodes in a phylogenetic tree

    Attributes:
    - name (str): Name of node
    - children (dict): Dictionary of {child_name: branch_length}, built from input list of tuples [(child_name, branch_length)]
    - parent: parent node, None if not yet assigned

    """
    def __init__(self, name, children):
        self.name = name
        self.children = {}
        for seq_id, branch_length in children:
             self.children[seq_id] = branch_length

    def add_parent(self, parent):
        self.parent = parent