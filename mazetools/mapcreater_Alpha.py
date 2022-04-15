from collections import Counter
import turtle as t
class maze:
    def __init__(self,map):
        self.ware=''
        self.round=''
        self.goal=''
        self.home=''
        self.map=map
        self.create={}
        self.arg=[]
    def create_block(self,x,y,color):
        t.up()
        t.goto(x*10,y*10)
        t.setheading(90)
        t.color(color)
        t.down()
        t.begin_fill()
        for _ in range(4):
            t.forward(20)
            t.right(90)
        t.end_fill()
        
    def choice(self,gh,c,b):
        #choice goal
        a=1
        for i in gh:
            print(str(a)+'.'+i+'   ',end='')
            a+=1
        choice=int(input('\nchoice a '+b+':'))
        if choice>len(gh):
            print('not right number!')
            exit(0)
        goal=gh[choice-1]
        gh.pop(choice-1)
        #choice home
        a=1
        for i in gh:
            print(str(a)+'.'+i+'   ',end='')
            a+=1
        choice=int(input('\nchoice a '+c+':'))
        if choice>len(gh):
            print('not right number!')
            exit(0)
        home=gh[choice-1]
        return (home,goal)
    
    def set_element(self):
        dict=Counter(self.map)
        tmp=dict.most_common()
        tmps=[]
        for i in tmp:
            tmps.append(i[0])
        
        #goal and home
        gh=[]
        ghl=[]
        for i in tmps:
            if(dict[i]==1):
                gh.append(i)
        if len(gh)<2:
                print("can't find goal or home")
                exit(0)
        for i in gh:
            ghl.append(i)
        t=self.choice(gh,'home','goal')
        self.home=t[0]
        self.goal=t[1]
        #round and wall
        if self.wall=='':
            tmps=list(set(tmps)-set(ghl))
            t=self.choice(tmps,'round','wall')
            self.round=t[0]
            self.wall=t[1]
            
        t=('#',' ')
        self.arg=list(set(tmps)-set(t))
              
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
        print('roud:'+self.round)
        print('home:'+self.home)
        print('goal:'+self.goal)
        print('orther:'+str(self.arg))
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
            exit(0)
    
    def createmap(self):
        for x in range(self.height):
                self.create[x]=self.map[x*self.width:(x+1)*self.width]

    def create_bround(self,x,y):
        for i in range(self.width+2):
            self.create_block(x+i*2,y,'white')
            self.create_block(x+i*2,y-(self.height+1)*2,'white')
        for i in range(self.height+2):
            self.create_block(x,y-i*2,'white')
            self.create_block(x+(self.width+1)*2,y-i*2,'white')
            
    def draw(self):
        parten={}
        for i in range(len(self.arg)):
            parten[i]=self.arg[i]
        print(len(self.arg))
        
        
        home=(-22,18)
        x=home[0]
        y=home[1]
        t.speed(1000)
        t.colormode(255)
        self.create_bround(x-2,y+2)
        for i in range(len(self.create)):
            for j in self.create[i]:
                #color
                for i in range(len(self.arg)):
                    if parten[i]==j:
                        color=10+i*20
                        self.create_block(x,y,(color,color,color))
                        break
                if j==self.wall:
                    self.create_block(x,y,'brown')
                if j==self.goal:
                    self.create_block(x,y,'pink')
                if j==self.home:
                    self.create_block(x,y,'purple')
                x+=2
            x=home[0]
            y-=2
        t.up()
        t.goto((home[0]+(self.width)*2+4)*10,(home[1]-10)*10)
        t.down()
        t.write('Pick is home，and purple is goal!')
        t.done()
    

if __name__=='__main__':
    choice=input('1.hex  2.string')
    if choice == '1':
        string=input('please input maze_hex:')
        # string='11223344556677'
        # string='0000000023000000000000002323232300000023230000004F4F00000000000000000000000000004F4F0050500000000000004C004F4F004F4F0050500000000000004C004F4F004F4F00500000000000004C4C004F4F00000000500000000000000000004F4F00000000500000000023000000000000000000000000000000000000000000000000000000230000000000000000004D4D4D00000023000000000000000000004D4D4D00000000454500000030004D004D004D0000000045000000000000000000000000000000454554545449004D004D004D00000000450000540049004D004D004D00000000450000540049004D004D004D210000004545'
        map=''
        d={}
        tmp=['%','&','*','@','~','!','/','=','[',']']
        num=0
        tmps=[]
        for i in range(0,len(string)-1,2):
            h=string[i]+string[i+1]
            tmps.append(h)
        w=Counter(tmps).most_common(2)
        ti=[]
        for i in w:
            ti.append(i[0])
        d[w[0][0]]=' '
        d[w[1][0]]='#'
        wall='#'
        round=' '
        for i in tmps:
            if not d.get(i):
                d[i]=tmp[num]
                num+=1
                if num >10:
                    print(d)
                    print('out of range')
            map+=d.get(i)
    else:
        # map='*******+********* ******    ****   ******* **F******    **************'
        map=input('please input maze_string:')
    maze=maze(map)
    if choice=='1':
        maze.wall=wall
        maze.round=round
    
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