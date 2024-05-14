# def permute(string,pocket = '',perm = []):
#     if len(string)== 0:
        
#         perm.append(pocket)
#     else:
#         for i in range(len(string)):
#             letter = string[i]
#             front = string[0:i]
#             back = string[i+1:]
#             together = front+back
#             app = permute(together,letter+pocket)
#     return perm
            


# a = permute('ansal')
# print(*a)

s = ['a','j','b']
print(set(s))
