class Year:
    
    def __init__(self) -> None:
        self.nd = {}
        
    def calc(self,l):
        for i in l:
            k = 18
            m = 1
            d = int(str(i)[2:])
            c = int(str(i)[:2])
            # F = k+ [(13*(m-1))/5] +D+ [D/4] +[C/4]-2*C
            f = k+int((13*(m-1))/5) + d + int(d/4) +int(c/4)-int(2*c)
            day = int(f%7)
            
            if day == 5:
                if i%4 ==0:
                    day=['thu','fri','sat','sun','mon','tue','wed',]
                    h=((i//4)+i+1+0)%7
                    self.nd[day[h]]=i
                else:
                    day=['fri','sat','sun','mon','tue','wed','thu']
                    h=((i//4)+i+1+0)%7
                    self.nd[day[h]]=i

        print(self.nd)
years = [1981,1979,1998,2002,2012]
o1=Year()
o1.calc(years)