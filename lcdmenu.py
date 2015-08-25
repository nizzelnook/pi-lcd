# uses menu.py to make a menu for the pi's lcd

from menu import Menu
import Adafruit_CharLCD as LCD
import time

# some constants
DEBOUNCE_TIME = .075

# initialize lcd
lcd = LCD.Adafruit_CharLCDPlate()

# create list of buttons
'''
buttons = {'l': LCD.LEFT, 'r': LCD.RIGHT, 'u': LCD.UP, 'd': LCD.DOWN,
           's': LCD.SELECT}
'''
# buttons = (LCD.LEFT, LCD.RIGHT, LCD.UP, LCD.DOWN, LCD.SELECT)

# create menus
row1 = [['1', 'text1'], ['2', 'text2'], ['3', 'text3'], ['4', 'exit']]
row1a = [['1a', 'text1a'], ['1b', 'text1b'], ['1c', 'text1c']]
row2a = [['2a', 'text2a'], ['2b', 'text2b']]
row3a = [['3a', 'text3a']]
row1aa = [['1aa', 'text1aa'], ['1ab', 'text1ab']]
row1ba = [['1ba', 'text1ba'], ['1bb', 'text1bb']]

m = Menu()
# add menus to m
m.add_right_list(row1)
m.add_right_list(row1a, up='1')
m.add_right_list(row2a, up='2')
m.add_right_list(row3a, up='3')
m.add_right_list(row1aa, up='1a')
m.add_right_list(row1ba, up='1b')

# turn lcd on and clear, set message to current item
lcd.clear()
lcd.set_color(1, 0, 0)
lcd.message(m.current_item.get_text())

run = True
while run:
    if lcd.is_pressed(LCD.LEFT):
        lcd.clear()
        m.move_left()
        lcd.message(m.current_item.get_text())
    elif lcd.is_pressed(LCD.RIGHT):
        lcd.clear()
        m.move_right()
        lcd.message(m.current_item.get_text())
    elif lcd.is_pressed(LCD.UP):
        lcd.clear()
        m.move_up()
        lcd.message(m.current_item.get_text())
    elif lcd.is_pressed(LCD.DOWN):
        lcd.clear()
        m.move_down()
        lcd.message(m.current_item.get_text())
    elif lcd.is_pressed(LCD.SELECT):
        if m.current_item.get_text() == 'exit':
            run = False
    time.sleep(DEBOUNCE_TIME)

# turn display off
lcd.clear()
lcd.set_color(0, 0, 0)
