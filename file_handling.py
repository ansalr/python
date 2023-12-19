"""
with open('python.txt','r') as f:
    print(f.read())


with open('python1.txt','w') as f:
    f.write('Test\n')
    f.write('Test1\n')
    f.write('Test2')

copy from onefile to another
with open('python.txt','r') as f:
    with open('python1.txt','w') as w:
        for line in f:
            w.write(line)
with open('img.jpg','rb') as f:
    with open('image1.jpg','wb') as w:
        for line in f:
            w.write(line)          
    """

with open('python.txt','r') as f:
    with open('python1.txt','a') as w:
        for line in f:
            w.write(line)
        w.write('\n')