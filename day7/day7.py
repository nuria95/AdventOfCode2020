
import numpy as np
import re

all_bags = []
def update_all_bags(obj):
    all_bags.append(obj)

def go_to_bag(name_bag):
    for bag in all_bags:
        if bag.name == name_bag:
            return bag
    return None

class Node():
    def __init__(self, name, parent=None):
        self.name = name
        self.tree = {}
        if parent is None:
            self.direct_parents = []
        else:
            self.direct_parents = [parent]
        update_all_bags(self)
        
    def add_children(self, children):
        for child in children:
            num, name = child.split(' ', maxsplit=1)
            self.tree[name] = int(num)
            child_bag = go_to_bag(name)
            if child_bag is None:
                child_bag = Node(name, parent = self)
            
            if self.name not in [parent.name for parent in child_bag.direct_parents]:
                    child_bag.direct_parents.append(self)
  
    def get_children(self, number_items=1):
        num_children = 0
        # print(self.tree)
        for name, num in self.tree.items():
            num_children = num_children + (num*number_items)
            num_children +=go_to_bag(name).get_children(number_items=num*number_items)
        return num_children
      
    def get_parents(self):
        p = []
        p=p+[parent.name for parent in self.direct_parents]
        for parent in self.direct_parents:
            p=p + go_to_bag(parent.name).get_parents()
        return p
    
    @property
    def num_parents(self):
        # Do set because there are repeated elements
        return len(set(self.get_parents()))
        

data = np.loadtxt('input', dtype='str', delimiter = '\n')
# data = ['faded purple bags contain 1 shiny maroon bag.']
def prepare_input(data_sample):
      
    a = re.split(' bags contain | bag[.]| bags, | bag, | bags[.]', data_sample)
   
    return a[0], a[1:-1] # last one is a '.'

print('Creating tree of bags...')
for data_sample in data:
    
    parent_name, child_name = prepare_input(data_sample)
    
    bag = go_to_bag(parent_name)
    if bag is None:
        bag = Node(name=parent_name)
    if 'no other' in child_name:
        continue
    bag.add_children(child_name)

my_bag_name = 'shiny gold'
print(f'Going to my bag {my_bag_name} on tree')
node = go_to_bag(name_bag=my_bag_name)
# print('Num parents my bag',node.num_parents)
print('Num children my bag', node.get_children())


