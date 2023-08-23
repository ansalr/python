arr = [7,0,4,0,0,7,0]
package = []
for i in arr:
    
    if i != 0:
        package.insert(0,i)
        print(package,sep="\n")

    else:
        
        package.append(i)
        print(package)
        


