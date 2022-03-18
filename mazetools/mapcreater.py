from collections import Counter
import turtle as t
class maze:
    def __init__(self,map):
        self.map=map
        self.create={}

    def set_element(self):
        dict=Counter(self.map).most_common()
        num=0
        for i in dict:
            if num <4:
                if num == 0:
                    self.wall=i[0]
                elif num == 1:
                    self.roud=i[0]
                elif num == 2:
                    self.goal=i[0]
                elif num == 3:
                    self.home=i[0]
                num+=1
        maze.set_boundary()
        maze.createmap()

    def change_wall(self):
            tem=self.roud
            self.roud=self.wall
            self.wall=tem
    
    def change_goal(self):
        tem=self.home
        self.home=self.goal
        self.goal=tem

    def change_xy(self):
        tem=self.width
        self.height=self.width
        self.width=tem

    def show_element(self):
        print('wall:'+self.wall)
        print('roud:'+self.roud)
        print('home:'+self.home)
        print('goal:'+self.goal)
        print('width:'+str(self.width))
        print('height:'+str(self.height))

    def set_boundary(self):
        l=len(self.map)
        cmult=[l/i for i in range(5,l-4)]
        dict=[i for i in range(5,l-4)]
        cmult1=list(set(cmult)&set(dict))
        xy=[]
        for x in cmult1:
            if (int(l/x),x) not in xy:
                xy.append((x,int(l/x)))
            else:
                break
        rang=len(xy)
        print('choice width and height:')
        for i in range(rang):
            print(str(i+1)+'.x:'+str(xy[i][0])+'    y:'+str(xy[i][1]))
        p=int(input('num:'))
        if p<=rang+1:
            self.width=xy[p-1][0]
            self.height=xy[p-1][1]
        else:
            print('no this choice')
    
    def createmap(self):
        for x in range(self.height):
                self.create[x]=self.map[x*self.width:(x+1)*self.width]

    def draw(self):
        x=-319
        y=267
        k=x
        l=y
        rank=30
        t.speed(100)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x+rank*(self.width),y)
        t.goto(x+rank*(self.width),y-rank*(self.height))
        t.goto(x,y-rank*(self.height))
        t.goto(x,y)
        
        l-=rank
        for i in range(0,self.height):
            t.goto(k,l-i*rank)
            for j in range(0,self.width):
                t.pendown()
                now=self.create[i][j]
                if(i+1<=self.height-1):
                    next=self.create[i+1][j]
                else:
                    next=now
                if now == self.roud and next != self.wall:
                    t.penup()
                if now == self.goal:
                    t.write('goal')
                    if now == self.goal and next != self.wall:
                        t.penup()
                if now == self.home:
                    t.write('home')
                    if now == self.home and next != self.wall:
                        t.penup()
                x+=rank
                t.goto(x,l-i*rank)
            x=k
            t.penup()
        l+=rank
        k+=rank
        for i in range(self.width):
            t.goto(k+i*rank,l)
            for j in range(0,self.height):
                t.pendown()
                now=self.create[j][i]
                if(i+1<=self.width-1):
                    next=self.create[j][i+1]
                else:
                    next=now
                if now == self.roud and next != self.wall:
                    t.penup()
                if now == self.goal and next != self.wall:
                    t.penup()
                if now == self.home and next != self.wall:
                    t.penup()
                y-=rank
                t.goto(k+i*rank,y)
            y=l
            t.penup()
        t.done()
    
    

if __name__=='__main__':
    # map='*******+********* ******    ****   ******* **F******    **************'
    map=input('please input maze_string:')
    maze=maze(map)
    maze.set_element()
    c=''
    while(c!='5'):
        print('     mapcraft       ')
        c=input(
        
'''1.exchange goal and home
2.exchange wall and road
3.show map's message
4.craft the map
5.exit\n'''
        )
        if c == '1' :
            maze.change_goal()
        elif c == '2' :
            maze.change_wall()
        elif c == '3' :
            maze.show_element()
        elif c == '4' :
            maze.draw()
        else:
            print('erro!')