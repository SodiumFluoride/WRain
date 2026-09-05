"""some code examples."""

'''
printing (for conways game of life. this would all be one line, i split it up to make it easier to edit/read, same with all the other code snippets that are split like this.)

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


