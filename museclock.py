import math
import time
from datetime import datetime
from tkinter import *
from baseConverter import numToBase

# window
root = Tk()
root.title('Seximal Clock')
root.resizable(FALSE, FALSE)

# window size
x = 150		# Center Point x
y = 150		# Center Point
root.geometry('{}x{}'.format(x * 2, y * 2))

# clock variables
length = 100	            # stick Length
buffer = 10                 # circle buffer
rotation = math.radians(90) # rotate clock so 0 is at the bottom

# canvas and background
canvas = Canvas(root, bg='#444444')
canvas.pack(expand='yes', fill='both')

# clock face
def create_circle(x, y, r, width, outline, fill):
    canvas.create_oval(x - r, y - r, x + r, y + r, width = width, outline = outline, fill = fill)
create_circle(x, y, length + buffer, width = 3, outline = '#111111', fill = '#333333')

# hands
sticks=[]
sticks.append(canvas.create_line(x, y, x, y, width = 1, fill = '#666666')) # ticks
sticks.append(canvas.create_line(x, y, x, y, width = 2, fill = '#888888')) # lulls
sticks.append(canvas.create_line(x, y, x, y, width = 4, fill = '#AAAAAA')) # short lapses
sticks.append(canvas.create_line(x, y, x, y, width = 6, fill = '#CCCCCC')) # long lapses

# notches
for i in range(36):
    line_buffer = 0
    medium_buffer = 10
    long_buffer = 20
    if i % 6 == 0:
        line_buffer = long_buffer
    elif i % 3 == 0:
        line_buffer = medium_buffer

    canvas.create_line(
        (length + buffer) * math.cos(math.radians(i * 10) + rotation) + x,
        (length + buffer) * math.sin(math.radians(i * 10) + rotation) + y,
        (length - line_buffer) * math.cos(math.radians(i * 10) + rotation) + x,
        (length - line_buffer) * math.sin(math.radians(i * 10) + rotation) + y,
        width = 2
    )

# digital clock text
text = StringVar()
label = Label(canvas, font='Courier', textvariable=text, anchor=W, width=11)
label.pack(side=BOTTOM, anchor=SE);

# update the time, then update the clock
def update_clock():
    now = time.time() # does not account for timezone?
    now -= 18000  # subtracts (and therefor, gives) timezone EST
    now -= 1640995200  # subtracts all time from before jan 1 2022 UTC

    now /= 1.851851851 # convert to misalian moments
    #now /= 0.66
    #now  /= 0.01

    now = int(now * 216) # round to seximal equivelent of microseconds or whatever 0.01 is
    now = numToBase(now, 6) # convert to a seximal string
    now = str(int(float(now)))
    now = now[::-1] # reverse string so that the smallest units are first, so indexing the precise digits is easier
    now = list(now)

    instants = now[0]
    snaps = now[1]
    ticks = '{}{}'.format(now[3], now[2])
    lulls = '{}{}'.format(now[5], now[4])
    short_lapses = now[6]
    long_lapses = now[7]
    
    timeString = '{}{}:{}:{}.{}{}'.format(long_lapses, short_lapses, lulls, ticks, snaps, instants)
    text.set(timeString)

    now = (ticks, lulls, short_lapses, long_lapses)
    for n, i in enumerate(now):
        cr = canvas.coords(sticks[n])[0:2]
        if (n < 2):
            cr.append((length - n * 14) * math.cos(math.radians(int(i, 6) * 10) + rotation) + x)
            cr.append((length - n * 14) * math.sin(math.radians(int(i, 6) * 10) + rotation) + y)
        else:
            cr.append((length - n * 14) * math.cos(math.radians(int(i, 6) * 10 * 6) + rotation) + x)
            cr.append((length - n * 20) * math.sin(math.radians(int(i, 6) * 10 * 6) + rotation) + y)
        canvas.coords(sticks[n], tuple(cr))


while True:
    root.update()
    root.update_idletasks()
    update_clock()
