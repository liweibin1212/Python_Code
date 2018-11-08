#! python3
# bulletPointAdd.py to add a bullet point for each line
import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)