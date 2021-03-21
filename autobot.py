import pyautogui
import time

# For meeting ID
meet_id = '2337926896'
pyautogui.press('esc',interval=0.1)

time.sleep(0.2)

# This will search for zoom and open the zoom
pyautogui.press('win',interval=0.1)
pyautogui.write('zoom')
pyautogui.press('enter',interval=0.5)

time.sleep(10)

#working fine till here
print('you are here')


# This will verify the join buttom

# x,y = pyautogui.locateOnScreen('JoinAMeeting.png')
# pyautogui.click(x,y)

pyautogui.press('enter',interval=1)
pyautogui.write(meet_id)
pyautogui.press('enter',interval=1)

pyautogui.click(772,445)
pyautogui.press('enter',interval=1)
print('Clicked Join a Meeting Button')

pyautogui.click(948,417)
pyautogui.press('enter',interval=1)
print('Clikced Drop Down to choose the previously saved file')

pyautogui.click(810,464)
pyautogui.press('enter',interval=1)
print('To choose the availabe option')

pyautogui.click(830,606)
pyautogui.press('enter',interval=1)
print('For Joingin the meeting')

pyautogui.press('enter',interval=1)



# For the password section
# Uncomment only if there is password for the meeting
password = '8My5KX'

time.sleep(3)
pyautogui.press('enter',interval=1)
pyautogui.write(password)
pyautogui.press('enter',interval = 1)

pyautogui.click(884,668)
pyautogui.press('enter',interval=1)
print('For Joingin the meeting with video on')


# For recording the meeting using Windows Game Bar
time.sleep(5)


# opening up  windows game bar  overlay
pyautogui.hotkey('win','g')
time.sleep(1)

# commencing screen recording
pyautogui.hotkey('win','alt','r')
time.sleep(1)

# Closing windows game bar overlay
pyautogui.hotkey('win','g')

# recording time amount
# time must be in second; Example:5min = 5*60 = 300sec
time.sleep(300)

# ending screen recording
pyautogui.hotkey('win','alt','r')
time.sleep(2)
## By default, screen captures are sent to a folder called captures in "videos" in "this PC"

# closing zoom
pyautogui.hotkey('alt','f4')
time.sleep(0.5)
# pyautogui.hotkey('alt','f4')
