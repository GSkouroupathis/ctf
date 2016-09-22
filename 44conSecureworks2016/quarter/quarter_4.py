import re

with open('quarter_4.txt', 'r+') as f:
   enc = f.read()

while True:
   allre = re.findall(r'%..', enc)
   dec = ''
   for onere in allre:
      dec += onere[1:].decode("hex")
   print dec
   enc = dec
   foobar = raw_input()

