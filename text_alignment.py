"https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true"


def text_align(n):

    w = n+(n-1)

    part_a(n,w)
    part_b(n,w)
    mid(n)
    part_b(n,w)
    end_h(n,w)




def part_a(n,width):

   
    j = 1
    for i in range(1,n+1):
        p_h = "H"*j
        
        print(p_h.center(width," "))
        width-+1
        j+=2

def part_b(n,width):

    for i in range(0,n):

        level_b1 = ("H"*n).rjust(width-2," ")
        level_bc = level_b1.ljust(19,' ')
    
        print(level_bc,level_b1)      

def mid(n):

    for i in range(0,3):

        level_c = (n*6)-3                # level_c_width = level_c
        count_c = level_c - 2            # level_c_h_count = count_c
        level_c1 = (("H"*count_c).rjust(level_c," "))
        print(level_c1)

def end_h(n,width):
    j = 9
    for i in range(1,n+1):
        p_h = "H"*j
        print(' '*((4*n)-1),p_h.center(width," "))
        width-+1
        j-=2

text_align(5)





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