arr = [7,0,4,0,0,7,0]
package = []
for i in arr:
    print(i)
    if i != 0:
        package.insert(0,i)
        print(package,sep="\n")

    else:
        print(i)
        package.append(i)
        print(package)
        


