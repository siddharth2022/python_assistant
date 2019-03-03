
### ------------------------------MOUSE--------------------------
>>> pyautogui.moveTo(100, 200)   # moves mouse to X of 100, Y of 200.
>>> pyautogui.moveRel(0, 50)     # move the mouse down 50 pixels.
>>> pyautogui.moveRel(-30, 0)     # move the mouse left 30 pixels.
>>> pyautogui.moveRel(-30, None)  # move the mouse left 30 pixels.
>>> pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
>>> pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
>>> pyautogui.dragRel(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button
>>> pyautogui.click()  # click the mouse
>>> pyautogui.click(x=100, y=200)  # move to 100, 200, then click the left mouse button.
>>> pyautogui.click(button='right')  # right-click the mouse
>>> pyautogui.click(clicks=2)  # double-click the left mouse button
>>> pyautogui.click(clicks=2, interval=0.25)  # double-click the left mouse button, but with a quarter second pause in between clicks
>>> pyautogui.click(button='right', clicks=3, interval=0.25)  ## triple-click the right mouse button with a quarter second pause in between clicks
>>> pyautogui.doubleClick()  # perform a left-button double click
>>> pyautogui.mouseDown(); pyautogui.mouseUp()  # does the same thing as a left-button mouse click
>>> pyautogui.mouseDown(button='right')  # press the right button down
>>> pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.
>>> pyautogui.scroll(10)   # scroll up 10 "clicks"
>>> pyautogui.scroll(-10)  # scroll down 10 "clicks"
>>> pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"
>>> pyautogui.hscroll(10)   # scroll right 10 "clicks"
>>> pyautogui.hscroll(-10)   # scroll left 10 "clicks"
The scroll() function is a wrapper for vscroll(), which performs vertical scrolling.
>>> pyautogui.typewrite('Hello world!')                 # prints out "Hello world!" instantly
>>> pyautogui.typewrite('Hello world!', interval=0.25)  # prints out "Hello world!" with a quarter second delay after each character

###---------------------------HOLD--------------------------
>>> pyautogui.keyDown('shift')  # hold down the shift key
>>> pyautogui.press('left')     # press the left arrow key
>>> pyautogui.press('left')     # press the left arrow key
>>> pyautogui.press('left')     # press the left arrow key
>>> pyautogui.keyUp('shift')    # release the shift key

###---------------------------better to use for hold--------
>>> pyautogui.hotkey('ctrl', 'shift', 'esc')

###------------------------------valid options------------
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

#####-------------------some basic interrupt guis
Message Box Functions
PyAutoGUI makes use of the message box functions in PyMsgBox to provide a cross-platform, pure Python way to display JavaScript-style message boxes. There are four message box functions provided:

The alert() Function
>>> alert(text='', title='', button='OK')
Displays a simple message box with text and a single OK button. Returns the text of the button clicked on.

The confirm() Function
>>> confirm(text='', title='', buttons=['OK', 'Cancel'])
Displays a message box with OK and Cancel buttons. Number and text of buttons can be customized. Returns the text of the button clicked on.

The prompt() Function
>>> prompt(text='', title='' , default='')
Displays a message box with text input, and OK & Cancel buttons. Returns the text entered, or None if Cancel was clicked.

The password() Function
>>> password(text='', title='', default='', mask='*')
Displays a message box with text input, and OK & Cancel buttons. Typed characters appear as *. Returns the text entered, or None if Cancel was clicked.

###-------------------------screenshot----------
>>> import pyautogui
>>> im1 = pyautogui.screenshot()
>>> im2 = pyautogui.screenshot('my_screenshot.png')


>>> im = pyautogui.screenshot(region=(0,0, 300, 400))#regional gui


##--------------------------locate by image
http://pyautogui.readthedocs.io/en/latest/screenshot.html

