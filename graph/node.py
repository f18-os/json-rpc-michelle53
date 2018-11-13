class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

# create a list of nodes(trees)
def list_creation( new_object, list=[] ): # assume list is emtpy if nothing is given
    children = []  # list of strings
    for child in new_object.children: # get string names of children
        children.append( str( child.name ) )
    dictionary = {'name':new_object.name, 'children':children, 'val':new_object.val }
    list.append( dictionary )
    for child in new_object.children: # recursively add each child
        list = list_creation( child, list)
    return list
# get the node based on name
def get_node( name_of_node, list):
    for node in list:
        if node.name == name_of_node:
            return node
    return []
# transforms list to a tree 
def back_to_tree( name_of_node='root', list=[] ):
    node_n = get_node( name_of_node, list)
    if node_n != []: # if node is not empty
        children = []
        for n_node in node_n['children']:
            if n_node.name not in children:
                children.append( n_node.name )
                continue
            children.append( back_to_tree(n_node, list) )
    else:
        return []
    c_node = node( name_of_node, children )
    c_node.val = node_n['val']
    return c_node

    



