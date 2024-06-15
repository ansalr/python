"""Generate a dictionary which key as odd number of chararter and value as
even number of the chararter from the input. If user enter number or space
in between skip and consider"""

inp_list=['one','two','three','four','five','six','seven','eight','nine','ten']
inp_list=list(map(str,input().split()))
new_d={}
for i in range(0,int(len(inp_list)/2),2):
    new_d[inp_list[i]]=inp_list[i+1]
    
print(new_d)