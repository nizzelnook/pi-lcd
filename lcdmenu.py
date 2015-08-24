# a simple lcd menu system


class menuItem(object):
    """ docstring
    missing action functionality
    """
    def __init__(self, name, text=None, left=None, right=None, up=None,
                 down=None, action=None):
        self.name = name
        self.text = text
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.action = action

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_up(self):
        return self.up

    def get_down(self):
        return self.down

    def set_left(self, newleft):
        self.left = newleft

    def set_right(self, newright):
        self.right = newright

    def set_up(self, newup):
        self.up = newup

    def set_down(self, newdown):
        self.down = newdown

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

    def set_text(self, newtext):
        self.text = newtext


class lcdMenu(object):

    def __init__(self, itemname=None, itemtext=None):
        self.items = dict()
        if itemname is not None:
            self.items[itemname] = menuItem(itemname, itemtext)
            self.current_item = self.items[itemname]

    def add_item(self, name, text=None, left=None, right=None,
                 up=None, down=None):
        """
        adds a new item to the menu
        """
        self.items[name] = menuItem(name, text, left, right, up, down)

    def create_left(self, name, leftname, text=None, up=None):
        """
        creates a new item to the left of item with name=name
        setes the right item to the new item
        if up is None then the up value for the right item is used
        """
        r_item = self.items[name]
        self.items[leftname] = menuItem(leftname, text, right=r_item, up=up)
        r_item.set_left(self.items[leftname])
        if up is None:
            self.items[leftname].set_up(r_item.get_up())

    def link_items(self, aname, bname, dir='right', copy_up=True):
        """
        links two items by ensuring that the two point to eachother in the
            direction specified
        direction specifies bname's relation to aname
        copy_up will assign aname's up value to bname
        """
        aitem = self.items[aname]
        bitem = self.items[bname]
        if dir == 'right' or dir == 'r':
            aitem.set_right(bitem)
            bitem.set_left(aitem)
            if copy_up:
                bitem.set_up(aitem.get_up())

        if dir == 'left' or dir == 'l':
            aitem.set_left(bitem)
            bitem.set_right(aitem)
            if copy_up:
                bitem.set_up(aitem.get_up())

        if dir == 'up' or dir == 'u':
            aitem.set_up(bitem)
            bitem.set_down(aitem)

        if dir == 'down' or dir == 'd':
            aitem.set_down(bitem)
            bitem.set_up(aitem)

    def create_right(self, lname, rname, text=None, up=None):
        """
        creates a new item to the right of item with name=lname
        sets the left item of rname to lname and visa versa
        """
        l_item = self.items[lname]
        self.items[rname] = menuItem(rname, text, left=l_item, up=up)
        l_item.set_right(self.items[rname])
        if up is None:
            self.items[rname].set_up(l_item.get_up())

    def add_up(self, uname, dname):
        """
        adds an existing item to another existing item's up
        """
        self.items[dname].set_up(self.items[uname])

    def add_down(self, dname, uname, text=None):
        """ adds a new item to an existing item's down
        """
        self.items[dname] = menuItem(dname, text, up=self.items[uname])
        self.items[uname].set_down(self.items[dname])

    def add_right_list(self, items, up=None, loop=False):
        """
        adds the 2d tuple of ((name, text), (name, text)) pairs to the menu
            where the order of the tuple is preserved in the menu
        the first entry will be the leftmost, snd will therefore be the down
            item if an up item is given
        the loop flag links the leftmost (first) and rightmost (last) items such
            that the menu forms a loop
        """
        # assert info not empty
        # create the items
        for item in items:
            for name, text in item:
                self.items[name] = menuItem(name, text)

    '''
    def add_up_right(self, name, uname, traverse=True):
        """
        traverses to the leftmost entry and moves right adding the leftmost
            item to the up item's down attribute and adding the up item to all
            other items' up attribute
        works the fastest when the leftmost item is passed
        the traverse flag stops the fuction from traversing the linked list if
            the list is a loop
    '''
