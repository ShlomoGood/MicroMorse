from microbit import *

#these variables describe the images to be displayed on the microbit's builtin 5x5 led grid
# 0 means led off  and 9 means led at full brightness, can vary brightness using numbers between 0-9
#e.g. "over" appears as [*   *]
#                       [ * * ]
#                       [  *  ]
#                       [ * * ]
#                       [*   *]
over = Image("90009:09090:00900:09090:90009")
dot = Image("00000:00000:00900:00000:00000")
dash = Image("00000:00000:09990:00000:00000")

#Can be used to make the puzzle slightly more complicated.
#Replace all instances of "dot" and "dash" in the code with "on"
#Users need to pay attention to length of time when the grid is illuminated to determine difference between dot (1 unit) and dash (3 units).
on = Image("99999:99999:99999:99999:99999") 

#Set the time unit used for dot, dash, and pauses.
time = 120 #speed of about 10 words per minute (wpm), calculation is time = 1200/wpm

CHAR = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  '.':'.-.-.-',  ',':'--..--',
        '?':'..--..',  '/':'--..-.',  '@':'.--.-.',
        ':':'---...'
        }

while True:
    msg = "https://github.com/ShlomoGood"

    for char in msg:
        letter = CHAR.get(char.upper())
	for bit in letter:
	   if bit==".":
               display.show(dot)
               sleep(time)
           if bit=="-":
               display.show(dash)
               sleep(time * 3)
           display.clear()
           sleep(time * 3)
    display.show(over)
    sleep(time * 7)
