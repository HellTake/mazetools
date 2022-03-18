# map='*******+********* ******    ****   ******* **F******    **************'
# goal='F'
# home='+'
class breaker:
    def __init__(self,map,width,height,home,goal):
        self.map={}
        for x in range(height):
            self.map[x]=map[x*width:(x+1)*width]
        self.home=home
        self.goal=goal
        self.width=width
        self.height=height
    def DFS(self,up,down,left,right):
        find=[]
        over=[]
        route=[]
        flag=0
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == home:
                    flag=1
                    start=(x,y)
                    find.append(start)
                    print('start position x:'+str(x)+'  y:'+str(y))
                    
                    break
            if flag == 1:
                break
        if flag == 0:
            print('can\'t find start position!')
        
        while(find!=[]):
            flag=0
            now=find[-1]
            x=now[0]
            y=now[1]
            if self.map[y][x] == self.goal:
                print('get goal!')
                break
            over.append(find.pop())
            if y-1>0:
                if self.map[y-1][x] == ' ' or self.map[y-1][x] == self.goal:
                    if (x,y-1) not in find and (x,y-1) not in over:
                        find.append((x,y-1))
                        route.append(up)
                        print('up')
                        flag=1
            if y+1>0:
                if self.map[y+1][x] == ' ' or self.map[y+1][x] == self.goal:
                    if (x,y+1) not in find and (x,y+1) not in over:
                        find.append((x,y+1))
                        route.append(down)
                        print('down')
                        flag=1
            if x+1>0:
                if self.map[y][x+1] == ' ' or self.map[y][x+1] == self.goal:
                    if (x+1,y) not in find and (x+1,y) not in over:
                        find.append((x+1,y))
                        route.append(right)
                        print('right')
                        flag=1
            if x-1>0:
                if self.map[y][x-1] == ' ' or self.map[y][x-1] == self.goal:
                    if (x-1,y-1) not in find and (x-1,y) not in over:
                        find.append((x-1,y))
                        route.append(left)
                        print('left')
                        flag=1
            if flag == 0:
                route=[]
        if route == []:
            print('cant\' find the right way!')
        print('route:',end='')
        for i in route:
            print(i,end='')
            
            

if __name__ == '__main__':
    # map='*******+********* ******    ****   ******* **F******    **************'
    # width=10
    # height=7
    # home='+'
    # goal='F'
    map=input('input map:')
    width=input('input width:')
    height=input('input height')
    home=input('input home')
    goal=input('input goal')
    b=breaker(map,width,height,home,goal)
    b.DFS('w','s','a','d')