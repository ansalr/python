"https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true"


n = 5
width = 9
j = 1
for i in range(1,n+1):
    p_h = "H"*j
    print(p_h.center(width," "))
    width-+1
    j+=2


for i in range(0,n):

    level_b1 = ("H"*n).center(width," ")

    print(level_b1,)

for i in range(0,3):
    level_c = n*6                # level_c_width = level_c
    count_c = level_c - 4        # level_c_h_count = count_c
    level_c1 = (("H"*count_c).center(level_c," "))
    print(level_c1)

for i in range(0,n):

    level_b1 = ("H"*n).center(width," ")

    print(level_b1,)
    







    """
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
"""