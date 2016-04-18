a=open('a.txt', 'r+')
b=open('b.txt', 'r+')

aa=a.read()
bb=b.read()

i=0
while 1:
  if aa[i] != bb[i]:
    print aa[i], bb[i],
    asdsad=raw_input('')
  i += 1
