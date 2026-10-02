"""some code examples."""

'''
output 1 if x and y equal
amount without x y


output 1 if x isnt negative
amount without "-" slice str x 0 1 0


output a string x multiplied by an integer y. matching the inputs allows this code to work without adjusting the slice parameters for string/number  amount.
match empty "" match A str_to_mult match N amount_to_mult match r0 "empty" match r1 slice line here add end here 7 -1 0 add A match "N" add N -1 parse parse add "r" string amount without 0 N


truth machine. if the input is 0, output 0 and then halt. if the input is 1, keep outputting 1 forever
new match r1 "print 1" match r0 and "print 0" "delete line find i" parse add r get
delete line find i 

print the numbers 0 through ten
current print 0
delete word slice line find add "cur" "rent" -1 -1 0
match "num" word slice line find add "cur" "rent" -1 -1 0 put num add num 1
break match r0 "i" delete line find parse add "r" amount without string word slice line find add "cur" "rent" -1 -1 0 string 10

'''

'''
conways game of life
finalcell 0 0 finalcell 1 0 finalcell 0 -2

boundleft -1
boundright 3
boundup -3
bounddown 1

new add "bound" add "left " match "current" word slice line find add "bound" "left " -1 -1 0 string add int current add -1 amount without string word slice find add "final" "cell" 11 11 0 string current
new add "bound" add "right " match "current" word slice line find add "bound" "right " -1 -1 0 string add int current add 1 amount without string word slice find add "final" "cell" 11 11 0 string current
new add "bound" add "up " match "current" word slice line find add "bound" "up " -1 -1 0 string add int current add -1 amount without string word slice find add "final" "cell" 11 11 0 string current
new add "bound" add "down " match "current" word slice line find add "bound" "down " -1 -1 0 string add int current add 1 amount without string word slice find add "final" "cell" 11 11 0 string current



new match "enum" find add "final" "cell" match "eX" int word slice enum 10 10 0 match "eY" word slice line enum -1 -1 0 and add add add add "live" "cell " eX " " eY match "y" and and -1 0 1 match "x" and and -1 0 1 add "around" add "cell " add string add eY y add " " string add eX x gabbagool

new match total pack line find add "around" "cell" match Ltotal pack string slice line find add "live" "cell" 10 -1 0 match "l1" "4" match "l0" "and 3 4" match "space" " " match "s0" "add final add cell add space coords" break match "s1" "without 0 0" match enum flatten string line unpack total break match coords string slice enum 12 -1 0 match sum add amount unpack total invert amount without enum string unpack total break parse parse add "s" string amount without parse parse add "l" string amount without break unpack Ltotal coords sum

print match "r1" □ match "r0" ■ match text1 "r" match text2 "final" match text3 "cell " match text4 " " match text5 "x" match text6 "s" match text7 "y" match text8 "" match subound int word slice line find add "bound" "up" -1 -1 0 match sdbound int word slice line find add "bound" "down" -1 -1 0 match slbound int word slice line find add "bound" "left" -2 -1 0 match srbound int word slice line find add "bound" "right" -1 -1 0 match "s2" "text8" match "s1" "add parse add text1 string amount find add text2 add text3 add string x add text4 string y match text5 add x 1 parse parse add text6 string amount without x srbound" match "s0" "add newlineee match text5 slbound match text7 add y 1 parse parse add text6 string add 2 break invert amount without y sdbound" match "total" pack line find add "final" "cell"match y add -1 subound match x add -1 slbound parse s1

'''

'''
printing the cells (for conways game of life. this would all be one line, i split it up to make it easier to edit/read, same with all the other code snippets that are split like this.)

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
bound updating for conways game of life

new add "bound" add "left " match "current" word slice line find add "bound" "left " -1 -1 0 string add int current add -1 amount without string word slice find add "final" "cell" 11 11 0 string current

boundleft -30
'''

'''

updating cells for conways game of life

new
match enum find add "final" "cell"
match "eX" word slice enum 10 10 0
match eY slice eX 2 0 2 
match "eX" int eX and add add add add "live" "cell " eX " " eY 
match y and and -1 0 1 
match x and and -1 0 1 
add add add add "around" "cell " add eY y " " add eX x 


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

'''




'''
match m or or "a" "b" "c" match n add "A" m print add n m
'''

