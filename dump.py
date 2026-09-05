'''
printing

print match "r1" □ 
match "r0" ■ 
match text1 "r" 
match text2 "final" 
match text3 "cell " 
match text4 " " 
match text5 "x" 
match text6 "s" 
match text7 "y" 
match text8 "" 
match subound int word slice line find add "bound" "up" -1 -1 0 
match sdbound int word slice line find add "bound" "down" -1 -1 0 
match slbound int word slice line find add "bound" "left" -2 -1 0 
match srbound int word slice line find add "bound" "right" -1 -1 0 
match "s2" "text8"
match "s1" "add parse add text1 string amount find add text2 add text3 add string x add text4 string y match text5 add x 1 parse parse add text6 string amount without x srbound" 
match "s0" "add newlineee match text5 slbound match text7 add y 1 parse parse add text6 string add 2 break invert amount without y sdbound" 
match "total" pack line find add "final" "cell"
match y add -1 subound 
match x add -1 slbound parse s1
'''



def grr():
    """
    import typing
lines=[]

x=100
def ack():
    global x
    x-=10
    return x


class Line:

    def construct(self):

        self.blocks=[]
        self.words=[]
        first=0
        second=0
        self.code=self.code
        while first<len(self.code):
            string=False
            while second<len(self.code):

                if self.code[second]=='"':
                    if string:
                        string=False
                        self.blocks.append((first+1,second+1))
                        self.words.append(self.code[first+1:second+1])
                        second+=1
                        first=second
                    else:
                        string=True

                elif self.code[second]==' ':
                    if string==False:
                        first
                        self.blocks.append((first+1,second))
                        self.words.append(self.code[first+1:second])
                        first=second
                    else:
                        pass
                second+=1
            first+=1
        self.blocks.pop(0)
        self.words.pop(0)
                    
    def __init__(self,code):
        self.to_delete=[]
        self.to_put={}
        self.code=" "+code
        self.construct()

    def __str__(self):
        return self.code
    
    def slice(self,a,b):
        a=Address(self,a,b)
        return a

    def apply(self):
        c=list(self.code)
        for f in self.to_delete:
             f)
        for f in self.to_delete:
            c[f[0]:f[1]]=['']*(f[1]-f[0])
        for key in self.to_put.keys():
            c[key]+=self.to_put[key]

        self.code=''.join(c)
        self.to_put={}
        self.to_delete=[]
        self.construct()
         self.code)
        return self.code
    
class Address:
    def __init__(self,line,a,b):
        if b==-1:
            b=len(line.code)
        self.line=line
        self.start=a
        self.end=b
        self.code=line.code[a:b]
    def __str__(self):
        return self.code

    def __len__(self):
        return len(self.code)

    def __eq__(self,a):
        if isinstance(a,Address):
            return self.line==a.line and self.start==a.start and self.end==a.end
        
        return False






def test(a:str)->str:
    return a+1


types = {
    "address":type(Address(Line(""),0,0)),
    "line":type(Line("")),
}

class Scanner():
    index=0
    start=0
    end=0
    iterations=3
    line=None
    parsebuffer=[]
    newline=True
    matches={}
    def put():
        pass

    def Go(self):
        running=False
        for line in lines:
            self.index=0
            self.line=line
            while self.index<len(line.words):
                if line.words[self.index]=="put":
                     "eyyyy im puttin ere")
                    running=True
                    self.index+=1
                    first=self.parse()
                     first)
                     "go forth")
                    second=self.parse()
                     second)
                     "the chud")
                    lines
                    for adr in first:
                         adr)
                         adr.line)
                        for fillerer in second:
                            fillerer=str(fillerer)
                            if adr.start in adr.line.to_put.keys():
                                if fillerer+adr.line.to_put[adr.start]==line.to_put[adr.start]+fillerer:
                                    line.to_put[adr.start]+=fillerer
                                else:
                                    raise Exception("string collision!")
                            else:
                                adr.line.to_put[adr.start]=fillerer

                elif line.words[self.index]=="new":
                    
                    running=True
                    self.index+=1
                    self.to_add+=self.parse()

                elif line.words[self.index]=="delete":
                     "empty it")
                    running=True
                    self.index+=1
                    z=self.parse()
                    for Z in z:
                         Z)
                         Z.line)
                        Z.line.to_delete.append((Z.start,Z.end))
                elif line.words[self.index]=="print":
                     "beep boop")
                    running=True
                    self.index+=1
                     *map(str,self.parse()))
                self.index+=1
        for line in lines:
            line.apply()
        if self.iterations>0:
            self.iterations-=1

            self.Go()

                

    def step(self):
        s=self

    def recurseparse(self,params,expression,index,args):
        final=[]
         index)
         args)
        for filler in params[index]:
            if (1+index)<len(params):
                 args)
                 "hi")
                a=self.recurseparse(params,expression,index+1,args+[filler])
                final+=a
            else:
                final+= [expression(*(args+[filler]))]
         final)
        return final

                


    def parse(self):


        s=self
        word=""
        if self.parsebuffer!=[]:
            word=self.parsebuffer.pop(0)
        else:
            word=s.line.words[s.index]
            s.index+=1

        if word in self.Words.keys():
            word=self.Words[word]
            if word[0]==0:
                return word[1]()
            else:
                params=[]
                for filler in range(word[0]):
                    params.append(self.parse())
                self.recurseparse(self,params,word[1],0,[])
                

        if word[0]=='"':
            return [word[1:-1]]
        if word.isdigit() or (word[0]=="-" and word[1:].isdigit()):
            return [int(word)]
        if word in self.matches:
            return self.matches[word]
        return [str(word)]


    def Find(self,s,exclude=False):
        full=[]
         s)
        for real in s:
            for l in lines:
                x=0
                c=l.code
                a=c.find(real,x)
                x=a+1
                while a!=-1:
                    z=l.slice(a,a+len(real))
                     l)
                     z.line)
                     l.code)
                     z.line.code)
                     "FOUND!")
                    
                    full.append(z)
                    a=c.find(real,x)
                    x=a+1
         full)
        return full

    def wmatch(self):
        a=self.parse()
        b=self.parse()
        data1=a[1]
        data2=a[1]
        a=a[0]
        b=b[0]

    def wslice(self):
        Adr=self.parse()
        Start=self.parse()
        End=self.parse()
        Scale=self.parse()
        asdf=0
        for adr in Adr:
            for start in Start:
                for end in End:
                    for scale in Scale:
                        asdf+=1
                        if end<0:
                            end+=1+len(adr)
                        if type(adr)==type(""):
                            a=adr[start-scale:end+scale]
                            
                            yield adr[start-scale:end+scale]
                        else:
                             )
                            a=adr.line.slice(adr.start+start-scale,adr.start+end+scale)
                            b=adr.line.slice(adr.start+start-scale,adr.start+end+scale)
                            adr.start
                            adr.end
                            yield adr.line.slice(adr.start+start-scale,adr.start+end+scale)        
    def wword(self):
        final=[]
        adr=self.parse()
        for x in adr:
            needf=True
            search=0
            while search<len(x.line.blocks):
                if needs:
                    nstart=x.line.blocks[search][0]
                if neede:
                    nend=x.line.blocks[search][1]
                if x.start>=nstart:

                    needs=False
                if x.end<=x.line.blocks[search][1] and neede:

                    neede=False
                if not(needf) and not(neede):
                    final.append(self.line.slice(nstart,nend))

                
                search+=1
            final.append(self.line.slice(nstart,nend))
        return final 

    def wadd(self):
        final=[]
        a=self.parse()
        b=self.parse()
        data1=a[1]
        data2=a[1]
        a=a[0]
        b=b[0]
        if data1.get("matches")!=None:
            pass

        for num1 in a:
            for num2 in b:
                final.append(num1+num2)
        return

    def wwithout(self):
        a=self.parse()
        b=self.parse()
        data1=a[1]
        data2=a[1]
        a=a[0]
        b=b[0]

    def wword(self):
        a=self.parse()
        b=self.parse()
        data1=a[1]
        data2=a[1]
        a=a[0]
        b=b[0]


    def wamount(self):
        a=self.parse()
        b=self.parse()
        data1=a[1]
        data2=a[1]
        a=a[0]
        b=b[0]


    def wstart(self):
        a=self.parse()
        b=self.parse()
        data1=a[1]
        data2=a[1]
        a=a[0]
        b=b[0]


    def wend(self):
        a=self.parse()
        b=self.parse()
        data1=a[1]
        data2=a[1]
        a=a[0]
        b=b[0]


    def wint(self):
        a=self.parse()
        b=self.parse()
        data1=a[1]
        data2=a[1]
        a=a[0]
        b=b[0]


    def wstring(self):
        a=self.parse()
        b=self.parse()
        data1=a[1]
        data2=a[1]
        a=a[0]
        b=b[0]


    def __init__(self):
        self.Words={
            "add":(2,lambda a,b:a+b),
            "here":(0,lambda:[self.line.slice(self.start,self.end)]),
            "this":lambda:(0,[self.line.slice(0,-1)]),
            "find":lambda:(1,lambda x:self.Find(x)),
        #    "shift":lambda:[a:=[self.parse(),self.parse(),self.parse()],a[0].line.slice(a[0].start+y,a[0].start+z) for x in a[0] for y in a[1] for z in a[2]][1],
            "slice":lambda:[*self.slice()],
            "parse":lambda:1,                                                                                                                                                                                                                                                                #this will cause a bug that will cause unparsed words to carry over and be run after the run ends, such as in the case of parse "find str hi parse" though i cant image it actually causing problems if you write code as intended. ill pretend its an awesome emergent property of my awesome code ah fuck but this would mean different orderings of sets would behave differently why cant i ever have fun do i just leave it in anyway
            "without":lambda:(a:=[self.parse(),self.parse()]) and [x for x in a[0] if not(x in a[1])],
            "and":lambda:self.parse()+self.parse(),
            "word":lambda:[self.word()],
            "amount":lambda:[len(self.parse())],
            "start":lambda:[x.start for x in self.parse()[0]],
            "end":lambda:[x.end for x in self.parse()[0]],
            "int":lambda:[int(x) for x in self.parse()[0]],
            "string":lambda:[str(x) for x in self.parse()[0]],
            
#            "":lambda,

        }
         self.recurseparse([["a","b"],["c","d"],["e","f"]],lambda x,y,z:x+y+z,0,[]))

'''
"command match m (word input) word m"
"m=[a,b,c]"
"command -> match ->*
#    def at(self):
 #       a=self.parse()
        
'put match m word find "s" add str m "us" '

#parse |"find str amon", "find str gus"|

'''
scanner=Scanner()


thecode='''
mark print 0
put slice find add "ma" "rk" 5 0 0 
delete slice find add "ma" "rk" 13 -1 8
'''
lines=thecode.split("\n")
lines=[Line(x+" ") for x in lines]

 lines)
#scanner.Go()
def matchh():
    x=0
    while x<10:
        yield x
        x+=1
    

for z in matchh():
     z)
    """

'''
bound updating

new add "bound" add "left " match "current" word slice line find add "bound" "left " -1 -1 0 string add int current add -1 amount without string word slice find add "final" "cell" 11 11 0 string current

boundleft -30
'''

'''
printing

print match "r1" □ 
match "r0" ■ 
match text1 "r" 
match text2 "final" 
match text3 "cell " 
match text4 " " 
match text5 "x" 
match text6 "s" 
match text7 "y" 
match text8 "" 
match subound int word slice line find add "bound" "up" -1 -1 0 
match sdbound int word slice line find add "bound" "down" -1 -1 0 
match slbound int word slice line find add "bound" "left" -2 -1 0 
match srbound int word slice line find add "bound" "right" -1 -1 0 
match "s2" "text8"
match "s1" "add parse add text1 string amount find add text2 add text3 add string x add text4 string y match text5 add x 1 parse parse add text6 string amount without x srbound" 
match "s0" "add newlineee match text5 slbound match text7 add y 1 parse parse add text6 string add 2 break invert amount without y sdbound" 
match "total" pack line find add "final" "cell"
match y add -1 subound 
match x add -1 slbound parse s1
'''




'''

finalcell 0 0 finalcell 0 1 finalcell 0 2 finalcell 0 3 finalcell 0 4


boundleft -30
boundright 30
boundup -1
bounddown 1

new add "bound" "left" match current word slice line find add "bound" "left " -1 -1 0 string add int current add -1 amount without string find add "final" "cell" string current

new match dir and "left " "up " match thestr add "bound" dir add thestr match "current" word slice line find thestr -2 -1 0 add add int current -1 amount without find add "final" "cell"
new match dir and "right " "down " match thestr add "bound" dr add thestr match "current" word slice line find thestr -2 -1 0 add int current invert add -1 amount without find add "final" "cell"

delete line find add "bound" and and and "left" "right" "up" "down"

new match enum find add "final" "cell" match "eX" word slice enum 10 10 0 match eY slice eX 2 0 2 match "eX" int eX and add add add add "live" "cell " eX " " eY match y and and -1 0 1 match x and and -1 0 1 add add add add "around" "cell " ex " " ey 

delete line find add "final" "cell"

new match total pack find add "around" "cell" match Ltotal pack find add "live" "cell" match "r0" pack and 3 4 match "r1" pack 3 match "s0" "without 0 0" match "text" add "final" "cell " match "s1" "add add final cell " match "s1" "add add text num" match enum flatten unpack total parse add "s" amount without unpack parse add "r" string amount without unpack Ltotal add add add "live" "cell " slice enum 10 -1 0 amount without without enum total total

print match "r1" □ match "r0" ■ match text1 "r" match text2 "final" match text3 "cell " match text4 " " match text5 "x" match text6 "s" match text7 "y" match text8 "" match subound int word slice find add "bound" "up" -2 -1 0 match sdbound int word slice find add "bound" "down" -2 -1 0 match slbound int word slice find add "bound" "left" -2 -1 0 match srbound int word slice find add "bound" "right" -2 -1 0 match "s2" "text8" match "s1" "add parse add text1 string amount without unpack total find add text2 add text3 add x add text4 add y match text5 x+1 parse add text6 string  amount without add x add 1 srbound" match "s0" "add \n match x slbound match text7 add y 1 parse add text6 string add 1  amount without y without y add 1 sdbound" match "total" pack find add "final" "cell" match y add -1 subound match x add -1 slbound parse s1

'''


'''

updating cells

new
match enum find add "final" "cell"
match "eX" word slice enum 10 10 0
match eY slice eX 2 0 2 
match "eX" int eX and add add add add "live" "cell " eX " " eY 
match y and and -1 0 1 
match x and and -1 0 1 
add add add add "around" "cell " add eY y " " add eX x 

ҹfinalcell 0 0ҹfinalcell 1 0ҹfinalcell 2 0

new
match total pack line find add "around" "cell"
match Ltotal pack string slice line find add "live" "cell" 10 -1 0
match "l1" "4"
match "l0" "and 3 4"
match "space" " "
match "s0" "add final add cell add space coords"
match "s1" "without 0 0"
match enum flatten string line unpack total
break
match coords string slice enum 12 -1 0
match sum add amount unpack total invert amount without enum string unpack total
break parse parse add "s" 
string amount without parse parse 
add "l" string amount 
without unpack Ltotal coords sum

ҹaroundcell 0 0ҹaroundcell 0 0ҹaroundcell 0 0ҹaroundcell 0 0ҹaroundcell 0 1ҹaroundcell 0 1ҹaroundcell 0 1ҹlivecell 0 1

'''


'''
conways game of life 

finalcell 0 0 finalcell 0 1 finalcell 0 2 finalcell 0 3 finalcell 0 4


boundleft -30
boundright 30
boundup -30
bounddown 30

new match dir and "left " "up " new add add "bound" dir match "current" word slice find add "bound" dir -1 -1 0 add add current -1  amount without find add "final" "cell"
new match dir and "right " "down " new add add "bound" dir match "current" word slice find add "bound" dir -1 -1 0 add current invert add -1  amount without find add "final" "cell"

delete line find add "bound" and and and "left" "right" "up" "down"

new match enum find add "final" "cell" match "eX" word slice enum 7 -1 2 match eY slice eX add 4 end eX -1 2 match "eX" int eX and add add add add "live" "cell " eX " " eY match y and and -1 0 1 match x and and -1 0 1 add add add add "around" "cell " ex " " ey 

delete line find add "final" "cell"

new match total pack find add "around" "cell" match Ltotal pack find add "live" "cell" match "r0" pack and 3 4 match "r1" pack 3 match "s0" "without 0 0" match "text" add "final" "cell " match "s1" "add add final cell " match "s1" "add add text num" match enum flatten unpack total parse add "s"  amount without unpack parse add "r" string  amount without unpack Ltotal add add add "live" "cell " slice enum 10 -1 0  amount without without enum total total

print match "r1" □ match "r0" ■ match text1 "r" match text2 "final" match text3 "cell " match text4 " "match text5 "x" match text6 "s" match text7 "y" match text8 "" match subound int word slice find add "bound" "up" -2 -1 0 match sdbound int word slice find add "bound" "down" -2 -1 0 match slbound int word slice find add "bound" "left" -2 -1 0 match srbound int word slice find add "bound" "right" -2 -1 0 match "s2" "text8" match "s1" "add parse add text1 string  amount without unpack total find add text2 add text3 add x add text4 add y match text5 x+1 parse add text6 string  amount without add x add 1 srbound" match "s0" "add \n match x slbound match text7 add y 1 parse add text6 string add 1  amount without y without y add 1 sdbound" match "total" pack find add "final" "cell" match y add -1 subound match x add -1 slbound parse s1

'''


'''
mark print 0
delete here here here here here here line find " "
match m word slice line find add "ma" "rk" 12 13 0 put
delete word slice line find add "ma" "rk" 12 13 0
'''

'''
match m or or "a" "b" "c" match n add "A" m print add n m
'''

'''
output 1 if x and y equal
amount and x y

output 1 if x isnt negative
amount and "-" slice str x 0 1 0

output x if y isnt 0, else 0
match 

send set of exclusively non zero to one
 amount without 0 x 

output a string x multiplied by an integer y. matching the inputs allows this code to work without adjusting the 
slice parameters for string/number  amount.

match empty "" match A str_to_mult match N amount_to_mult match r0 "empty" match r1 slice line here add end here 7 -1 0 add A match "N" add N -1 parse parse add "r" string amount without 0 N

if F and G are sentences that use the keyword z, set z to G(z) and add F(z) to a set, until z is equal to N, then
output the set.
match empty "" match N input match r0 "empty" match r1 slice line here add end here 7 -1 0 add A match "N" add N -1 parse parse add "r" string amount without 0 N

without a, output b.

-x


tell if x is less than y

multiply two integers, x and y. The part at the start of matching y and here allows this to be used for x and y with an arbitrary
amount of digits.
match a x match N a match b y match s here add match N add N-1


'''

'''
new
    match enum find add "final" "cell"
        match "eX" word slice enum 7 -1` 2
            match eY slice eX add 4 end x -1 2
                match "eX" int eX
                    and
                        add add add "livecell " eX " " eY

                        match y and and -1 0 1
                            match x and and -1 0 1
                                add add add "aroundcell" ex " " ey

print 
match "r1" □
match "r0" ■
match text1 "r"
match text2 "final"
match text3 "cell "
match text4 " "
match text5 "x"
match text6 "s"
match text7 "y"
match text8 ""
match "total" pack find add "final" "cell"
match subound int word slice find add "bound" "up" -2 -1 0
match sdbound int word slice find add "bound" "down" -2 -1 0
match slbound int word slice find add "bound" "left" -2 -1 0
match srbound int word slice find add "bound" "right" -2 -1 0
match "s2" "text8"
match "s1" "add parse parse add text1 string amount without unpack total find add text2 add text3 add x add text4 add y match text5 x+1 parse add text6 string amount without add x add 1 srbound"
match "s0" "add \n match x slbound match text7 add y 1 parse parse  add text6 string add 1  amount without y without y add 1 sdbound"
match y add -1 subound
    match x add -1 slbound
        parse s1
                                '''


