
# Based on: PySide examples/itemviews/simpletreemodel
# See: http://harmattan-dev.nokia.com/docs/library/html/qt4/itemviews-simpletreemodel.html

# Disabling the need for docstrings, all methods are tiny.
# pylint: disable=C0111

import logging
logger = logging.getLogger(__name__)

# Maximum number of characters used in the __str__ method to represent the underlying object
MAX_OBJ_STR_LEN = 50

class TreeItem(object):
    """ Tree node class that can be used to build trees of objects.
    """
    def __init__(self, obj, name, obj_path, is_attribute, parent=None):
        self.parent_item = parent
        self.obj = obj
        self.obj_name = str(name)
        self.obj_path = str(obj_path)
        self.is_attribute = is_attribute
        self.child_items = []
        self.has_children = True
        self.children_fetched = False


    def __str__(self):
        n_children = len(self.child_items)
        if n_children == 0:
            s = repr(self.obj)
            if len(s) > MAX_OBJ_STR_LEN:
                s = s[:MAX_OBJ_STR_LEN] + '...'
            
            return "<TreeItem(0x{:x}): {} = {}>" \
                .format(id(self.obj), self.obj_path, s)
        else:
            return "<TreeItem(0x{:x}): {} ({:d} children)>" \
                .format(id(self.obj), self.obj_path, len(self.child_items))


    def __repr__(self):
        n_children = len(self.child_items)
        return "<TreeItem(0x{:x}): {} ({:d} children)>" \
            .format(id(self.obj), self.obj_path, n_children)
            
    
    def append_child(self, item):
        item.parent_item = self
        self.child_items.append(item)

    def insert_children(self, idx, items):
        self.child_items[idx:idx] = items
        for item in items:
            item.parent_item = self

    def child(self, row):
        return self.child_items[row]

    def child_count(self):
        return len(self.child_items)

    def parent(self):
        return self.parent_item

    def row(self):
        if self.parent_item:
            return self.parent_item.child_items.index(self)
        else:
            return 0

    def pretty_print(self, indent=0):
        if 0:
            print(indent * "    " + str(self))
        else:
            logger.debug(indent * "    " + str(self))
        for child_item in self.child_items:
            child_item.pretty_print(indent + 1)
            
        
        
