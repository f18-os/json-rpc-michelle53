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
    name = new_object.name # shohuld be a name string\
    children = []  # list of strings
    for child in new_object.children: # get string names of children
        children.append( str( child.name ) )
    val = new_object.val # should be an int val
    dictionary = {'name':name, 'children':children, 'val':val }
    list.append( dictionary )
    # recursively add each child
    for child in new_object.children:
        list = list_creation( child, list)

    return list