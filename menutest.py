# for testing the menu

from lcdmenu import lcdMenu

m = lcdMenu()
row1 = [['1', 'item1'], ['2', 'item2'], ['3', 'item3'], ['4', 'item4']]
row1a = (('1a', 'item1a'), ('1b', 'item1b'))
row2a = (('2a', 'item2a'), ('2b', 'item2b'))
row3a = (('3a', 'item3a'))

m.add_right_list(row1)
m.add_right_list(row1a, up='1')
m.add_right_list(row2a, up='2')
m.add_item('3a', 'item3a')
m.link_items('3a', '3', 'up')

# navigation of menu
sel = '-1'
while sel != 'exit':
    print(m.get_text())
    sel = input('Choice: ')
    if sel == 'w':
        m.move_up()
    elif sel == 's':
        m.move_down()
    elif sel == 'a':
        m.move_left()
    elif sel == 'd':
        m.move_right()
