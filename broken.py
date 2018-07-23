from itertools import *

f = open('broken', "rb")
brokena = f.read(1453)
f.seek(2260)
brokenb = f.read()

def readfrag(name):
  with open(name, 'rb') as f:
    frag = f.read()
  return(frag)

#def printFrag(frag):
  #print('/x' + '/x'.join(hex(ord(x))[2:] for x in frag))

def writeBin(order, index):
  f = open('bin/' + str(index), 'wb')
  f.write(brokena + order[0] + order[1] + order[2] + order[3] + order[4] + order[5] + order[6] + order[7] + brokenb)
  f.close()

def main():
  frag1 = readfrag('fragment_1.dat')
  frag2 = readfrag('fragment_2.dat')
  frag3 = readfrag('fragment_3.dat')
  frag4 = readfrag('fragment_4.dat')
  frag5 = readfrag('fragment_5.dat')
  frag6 = readfrag('fragment_6.dat')
  frag7 = readfrag('fragment_7.dat')
  frag8 = readfrag('fragment_8.dat')

  dump = list(permutations([frag1, frag2, frag3, frag4, frag5, frag6, frag7, frag8]))

  for index,line in enumerate(dump):
    writeBin(line, index)

if __name__ == '__main__':
  main()
