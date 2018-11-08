#! python3
import pyperclip
spam = ' hot dog '
print(spam.strip().center(20,'*'))
print(spam.lstrip().center(20,'*'))
print(spam.rstrip().center(20,'*'))

bacon = 'SpamSpamSpamBaconspamEggsSpamSpam'
print(bacon.strip('Spam'))
print(bacon.strip('apmS'))
#pyperclip.copy("hello python")
print(pyperclip.paste())