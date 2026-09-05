import typing
lines=[]




x=100
def ack():
    global x
    x-=10
    return x


def recurselist(params,expression,index,args):
    final=[]
    for filler in params[index]:
        if (1+index)<len(params):
            a=recurselist(params,expression,index+1,args+[filler])
            final+=a
        else:
            final+= [expression(args+[filler])]
    return final

class Line: 

    def __hash__(self):
        return hash(id(self))

    def construct(self):
        if self.code=="":
            lines.remove(self)
            return ""
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
        code=" "+code+" "
        self.to_delete=[]
        self.to_put={}
        self.code=code
        self.construct()

    def __str__(self):
        return self.code
    
    def slice(self,a,b):
        if b>len(self.code):
            b=len(self.code)
        f=Address(self,a,b)
        return f

    def apply(self):
        c=list(self.code)

             
        for f in self.to_delete:
            c[f[0]:f[1]]=['']*(f[1]-f[0])
        for key in self.to_put.keys():
            c[key]+=self.to_put[key]

        self.code=''.join(c)
        self.to_put={}
        self.to_delete=[]
        self.construct()
         
        return self.code
    
class Address:

    def __init__(self,line,a,b):
        if b<0:
            b=len(line.code)+b+1

        if a<0:
            a=len(line.code)+a
        
        
        self.line=line
        self.start=a
        self.end=b
        self.code=line.code[a:b]
        z=self.code
        self.debug=self.line.code[0:self.start]+"^"+self.line.code[self.start:self.end]+"^"+self.line.code[self.end:]
        Z=self.debug
        False
    def __str__(self):
        return self.code
    #def __str__(self):
    #    return self.line.code[0:self.start]+"^"+self.line.code[self.start:self.end]+"^"+self.line.code[self.end:]

    def __hash__(self):
        return hash((self.line,self.start,self.end))

    def __int__(self):
        return int(str(self))

    def __len__(self):
        return len(self.code)

    def __eq__(self,a):
        if isinstance(a,Address):
            return self.line==a.line and self.start==a.start and self.end==a.end
        
        return False

types = {
    "address":type(Address(Line(""),0,0)),
    "line":type(Line("")),
}


class Scanner():
    forceparse=False
    breakk=False
    to_add=[]
    cancommand=True
    index=0
    start=0
    end=0
    iterations=0
    line=None
    parsebuffer=[]
    newline=True
    matches={}
    needmatch=True
    skip=False

    def sbranch(self,n):
        pass

    def Go(self):
        running=False
         

        for line in lines:
            skip=False
            self.cancommand=True
             
            self.index=0
            self.line=line
            while self.index<len(line.words):
                if skip:
                    break
                self.parse()
                '''
                a=line.words[self.index]
                if line.words[self.index]=="replace":
                    pass
                if line.words[self.index]=="put":
                    pass
                elif line.words[self.index]=="new":
                    pass
                    break

                elif line.words[self.index]=="delete":
                    pass
                    break

                elif line.words[self.index]=="print":

                    break
                self.index+=1'''
        for line in lines:
            line.apply()
        for filler in self.to_add:
            a=Line(filler)
            lines.append(a)
        self.to_add=[]
        if self.iterations>0:
            self.iterations-=1
            self.Go()
        else:
            print("halted!")
             

    def wput(self):
         
        self.running=True
        if not(self.cancommand):
            raise Exception("Can't have multiple commands per line!")
        self.cancommand=False
#        self.index+=1
        first=self.parse()
         
         
        second=self.parse()
         
         
        lines
        for adr in first:
            for fillerer in second:
                fillerer=str(fillerer)
                if adr.start in adr.line.to_put.keys():
                    if fillerer+adr.line.to_put[adr.start]==self.line.to_put[adr.start]+fillerer:
                        self.line.to_put[adr.start]+=fillerer
                    else:
                        raise Exception("string collision!")
                else:
                    adr.line.to_put[adr.start]=fillerer
        return []

    def wreplace(self):
         
        self.running=True
        if not(self.cancommand):
            raise Exception("Can't have multiple commands per line!")
#        self.index+=1
        first=self.parse()
        second=self.parse()
        for adr in first:
             
             
            for fillerer in second:
                fillerer=str(fillerer)
                adr.line.to_delete.append((adr.start,adr.end))
                if adr.start in adr.line.to_put.keys():
                    if fillerer+adr.line.to_put[adr.start]==self.line.to_put[adr.start]+fillerer:
                        self.line.to_put[adr.start]+=fillerer
                    else:
                        raise Exception("string collision!")
                else:
                    adr.line.to_put[adr.start]=fillerer
        return []

    def wdelete(self):
         
#        self.index+=1
        self.running=True
        if not(self.cancommand):
            raise Exception("Can't have multiple commands per line!")
        z=self.parse()
        for Z in z:
             
             
            Z.line.to_delete.append((Z.start,Z.end))

        return []

    def wnew(self):
        self.running=True
        if not(self.cancommand):
            raise Exception("Can't have multiple commands per line!")
        self.cancommand=False
#       self.index+=1
        a=self.parse()
        self.to_add+=a
        print(a)
        return []

    def wprint(self):
        self.running=True
        if not(self.cancommand):
            raise Exception("Can't have multiple commands per line!")
        self.cancommand=False
         
#        self.index+=1
        final=self.parse()

        print()
        print()
        print()
        print("hello world!")
        for filler in final:
            print(filler)  

         
        print("its the thing")
        return []

    layer=0
    waslayer=0
    toprint=""

    def parse(self):
        try:
            layer=self.layer
            out=[]
            s=self
            word=""

            while self.parsebuffer!=[]:
                if self.parsebuffer[0]=="":
                    self.parsebuffer.pop(0)
                else:
                    break
            if self.parsebuffer!=[]:
                
                word=self.parsebuffer.pop(0)
            elif self.index>=len(s.line.words):
                return []
            else:
                word=s.line.words[s.index]
                s.index+=1
            self.word=word
            print(word,end=" ")
            if self.breakk:
                    pass
            if word=='':
                return self.parse()
            if word in self.Words.keys():
                self.layer=layer+1
                out=self.Words[self.word]()
                if self.breakk:
                    pass
                if self.forceparse:
                    return []
                return out
            if word[0]=='"':
                return [word[1:-1]]
            if word.isdigit() or (word[0]=="-" and word[1:].isdigit()):
                return [int(word)]
            if word in self.matches:
                a=self.matches[word]
                if a==None:
                    return []
                if self.breakk:
                    pass
                return [self.matches[word]]
            return [str(word)]
        except Exception as gack:
            if self.forceparse:
                return []
            else:
                raise gack
    def wunbreak(self):
        self.breakk=False
        return self.parse()
    def Find(self,s,exclude=False):
        full=[]
         
        for real in s:
            for l in lines:
                x=0
                c=l.code
                a=c.find(real,x)
                x=a+1
                while a!=-1:
                    z=l.slice(a,a+len(real))
                    
                    full.append(z)
                    a=c.find(real,x)
                    x=a+1
         
        return full

    wordsize={

    }
    def wmatch(self):
        self.sbranch(3)
        a=self.parse()
        b=self.parse()

        if b==[]:
            t=self.forceparse
            self.forceparse=True
            for fillerer in a:
                self.matches[fillerer]=None
            self.parse()
            self.forceparse=t
            return

        c=self.index
        final=[]
        temp=self.cancommand

        for filler in b:
            for fillerer in a:
                self.matches[fillerer]=filler
            self.cancommand=temp

            self.index=c
            final+=self.parse()
        for A in a:
            goback=self.matches.get(A)
            if goback==None:
                self.matches.pop(A)
            else:
                self.matches[A]=goback
        pass
        return final

    def wslice(self):
        self.sbranch(4)
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
                        if start<0:
                            start+=1+len(adr)
                        if type(adr)==type(""):
                            a=adr[start-scale:end+scale]
                            
                            yield adr[start-scale:end+scale]
                        else:
                            a=adr.line.slice(adr.start+start-scale,adr.start+end+scale)
                            adr.start
                            adr.end
                            yield a

    def wparse(self):
        toadd=self.parse()
        if len(toadd)>1:
            raise Exception("Can't parse sets because im a lazy bum that sucks at programming")
        if toadd==[]:
            return []
        else:
            toadd=toadd[0]
            self.parsebuffer=str(toadd).split(" ")+self.parsebuffer

        return self.parse()

    def wbreak(self):
        self.breakk=True
        return self.parse()

    def wwithout(self):
        self.sbranch(2)
        a=self.parse()
        b=self.parse()
        c=[x for x in b if not(x in a)]
        pass
        return c

    def wword(self):
        final=[]
        adr=self.parse()

        for x in adr:
            needs=True
            neede=True
            search=0
            prevstart=0
            prevend=0
            while search<len(x.line.blocks):
                teststart=x.line.blocks[search][0]
                testend=x.line.blocks[search][1]
                if teststart>x.start and needs:
                    fstart=prevstart
                    needs=False
                if testend>x.end and neede:
                    fend=testend
                    neede=False

                if not(needs) and not(neede):
                    a=x.line.slice(fstart,fend)
                     
                    final.append(a)
                    break

                prevstart=teststart
                search+=1
            if needs:
                fstart=teststart
            if neede:
                fend=testend
            a=x.line.slice(fstart,fend)
             
            final.append(a)


         
        return final 

    def win(self):
        global lines
        tlines=lines
        final=[]
        for filler in self.parse():
            filler=Line(str(filler))
            lines=[filler]
            final+=self.parse()
        lines=tlines
        return final

    def wskip(self):
        self.skip=True
        return []

    

    def wadd(self):
        self.sbranch(2)
        A=self.parse()
        B=self.parse()
        final=[]
        for a in A:
            for b in B:
                if isinstance(a,type(b)):
                    final.append(a+b)
                else:
                    try:
                        final.append(a+type(a)(b))
                    except:
                        final.append(type(b)(a)+b)
        return final

  
    def wand(self):
        self.sbranch(2)
        return self.parse()+self.parse()

    def wflatten(self):
        #lambda:list(set(self.parse()))
        a=self.parse()
        b=set(a)
        c=list(b)
        return c



    def __init__(self):
        self.Words={
            "add":self.wadd,
            "here":lambda:[self.line.slice(self.line.blocks[self.index-1][0],self.line.blocks[self.index-1][1]+1)],
            "this":lambda:[self.line.slice(0,-1)], 
            "find_in":lambda:[*self.Find(self.parse())],
            "put":self.wput,
            "delete":self.wdelete,
#            "replace":self.wreplace,
            "new":self.wnew,
            "print":self.wprint,
            "find":lambda:[*self.Find(self.parse())],
        #    "shift":lambda:[a:=[self.parse(),self.parse(),self.parse()],a[0].line.slice(a[0].start+y,a[0].start+z) for x in a[0] for y in a[1] for z in a[2]][1],
            "slice":lambda:[*self.wslice(),],
            "slice_word":1,
            "parse":self.wparse,                                                                                                                                                                                                                                                                #this will cause a bug that will cause unparsed words to carry over and be run after the run ends, such as in the case of parse "find str hi parse" though i cant image it actually causing problems if you write code as intended. ill pretend its an awesome emergent property of my awesome code ah fuck but this would mean different orderings of sets would behave differently why cant i ever have fun do i just leave it in anyway
            "without":self.wwithout,
            "and":self.wand,
            "flatten":self.wflatten,
            #"or":lambda:(a:=[self.parse(),self.parse()]) and [x for x in a[0] if a in []],
            "word":lambda:self.wword(),
            "amount":lambda:[len(self.parse())],
            "size":lambda:[len(x) for x in self.parse()],
            "start":lambda:[x.start for x in self.parse()],
            "end":lambda:[x.end for x in self.parse()],
            "int":lambda:[int(x) for x in self.parse()],
            "string":lambda:[str(x) for x in self.parse()],
            "line":lambda:[x.line.slice(0,-1) for x in self.parse()],
            "match":self.wmatch,
            "skip":self.wskip,
            "pack":lambda:[self.parse()],
            "unpack":lambda:[x for y in self.parse() for x in y],
            "invert":lambda:[-x for x in self.parse()],  
            "break":self.wbreak,
            "unbreak":self.wunbreak,
        }
        print(self.Words.keys())
        print()

#parse |"find str amon", "find str gus"|


scanner=Scanner()



inputamt={"add":2,"match":3,"slice":4,"without":2,"and":2,"or":2}
wordss=['add', 'here', 'this', 'find_in', 'put', 'delete', 'new', 'print', 'find', 'slice', 'slice_word', 'parse', 'without', 'and', 'flatten', 'word', 'amount', ' amount', 'start', 'end', 'int', 'string', 'match', 'line', 'skip', 'pack', 'unpack', 'invert']
branchindex=-1
def branchprint(theline,layer):

    global branchindex
    branchindex+=1
    if branchindex>=len(theline.words):
        return
    a=theline.words[branchindex]
    if a=='':
        return branchprint(theline,layer)


    if a in wordss:

        if a in inputamt.keys():
            print(a)
            for filler in range(inputamt[a]):
                print("    "*layer,end=" ")
                branchprint(theline,layer+1)
        else:
            print(a,end=" ")
            branchprint(theline,layer+1)
    else:
        print(a)

def Branchprint(stri):
    branchprint(Line(stri),0)



thecode='''


finalcell 0 0

new match enum find add "final" "cell" match "eX" word slice enum 10 10 0 match "eY" slice eX 2 0 2 match "eX" int eX and add add add add "live" "cell " eX " " eY match "y" and and -1 0 1 match " " and and -1 0 1 add add add add "around" "cell " add eY y " " add eX x 


break new match total pack line find add "around" "cell" match Ltotal pack string slice line find add "live" "cell" 10 -1 0 match "l1" "4" match "l0" "and 3 4" match "space" " " match "s0" "add final add cell add space coords" match "s1" "without break 0 0" match enum flatten string line unpack total break match coords string slice enum 12 -1 0 match sum add amount unpack total invert amount without enum string unpack total break parse parse add "s" string amount without parse parse add "l" string amount without unpack Ltotal coords sum




'''

"""
new 
match total pack find add "around" "cell"
match Ltotal pack find add "live" "cell"
match "r0" pack and 3 4 match "r1" pack 3
match "s0" "add final add cell num"
match "s1" "without 0 0"
match enum flatten unpack total
match nums slice enum 12 -1 0
Ltotal without add "live" add "cell "
parse parse add "s" string amount

"""

'''thecode=thecode.replace("\n\n","ҹ")
thecode=thecode.replace("\n"," ")
thecode=thecode.replace("ҹ","\n")'''
lines=thecode.split("\n")
lines=[Line(x) for x in lines]
print("matcha")

Branchprint('parse parse add "s" string amount without unpack parse parse add "l" string amount without string unpack Ltotal coords sum')
a=Line("gaksgdjasd")


scanner.Go()
print("gabbagool!")
print()
for f in lines:
    print(f)