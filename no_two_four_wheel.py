def automobile(v,w):
  if (w&1)==1 or w<2 or v>=w:
    return ("INVALID INPUT")
else:
    x = ((4*v)-w)//2
    return ("TW={} FW={}".format(x,v-x))

v = int(input())
w = int(input())
output = automobile(v,w):
