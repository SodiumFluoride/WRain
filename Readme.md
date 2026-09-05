WRain is a functional, set based esolang thats commutative over line composition. Meaning, line order does not matter. 

Every line executes at once, commands are queued, and then it executes again. It will keep running until every command is deleted.

All data is an unordered collection of elements. They can hold duplicate elements. The element types are numbers, collections, addresses, and strings. addresses are a custom object, and refer to a piece of a line. They can be casted to a string by simply outputting the text contained in that piece.

There are two types of words, commands and functions. commands take in input, and alter the program, or the terminal in the case of print. functions take in input, and ouput something based on that.

The components of an address are a line to reference, a start, and an end. They are a reference to all the code from their start to their end in that line. When casted to a string, they will become a copy of the code they reference.

This is an abelian language, which means execution order between lines does not matter, which is why collections are unordered. The way that is done is by handling everything as if it had been done at the same time. Often this is resolved by only doing one thing at a time. When multiple, potentially conflicting things are done at the same time, it will be referred to as a collision. The sources of collisions are operating on collections with more than one element, or operating on multiple collections at the same time.

There are Two* types of functions, ordinary and special. Ordinary functions take in collections of elements, in this case C1 C2 C3.... and output the collecion of the outputs of every permutation of a single element chosen from the collections, and passed into some underlying function.
So if x={a,b} and y={c,d}, and the underlying function of word is func(n,m), then word x y = {func(a,c),func(a,d),func(b,c),func(b,d)}. As an example, the underlying function of Add is addition of two elements. so if x={1,2,3} and y={5,6}, Add={1+5,1+6,2+5,2+6,3+5,3+6}={6,7,7,8,8,9}. If the inputs have only one element, there is only one possible permutation, so it would simply equal a set with only one element, the underlying function with those single elements as the input. So Add {4} {5} simply equals {9}. Currently, all commands are ordinary functions.

This is the template I will use to denote functions.

func name
a:type1, b:type2, c:type3..... -> x:type
g(a,b,c....)

this means func name has an underlying function g, which takes in something of type1, type2, type3.... and ouputs something of of type x.


Special functions have no underlying function, and simply deal with the collection in its entirety.


There are also functions that don't fit into either category. I will denote them with weird, and explain them on a case by case basis

These are the commands. You can only have one command per line.



print, ordinary, command

to pring:string castable-> no output

Queues the elements of to print to be printed. Causes an unresolvable collision if multiple things are queued, whose printing order would affect the ouput. So print({"ab","ab"}) will work but print({"ab","cd"}) will not.



put, ordinary, command

where to put:address, to put:string castable->no output

Queues to put to be inserted at the start of where to put. Causes an unresolvable collision under the same conditions as print



delete, ordinary, command

to delete:address -> no output

Queues the piece of the line that to delete is a reference to to to be deleted. 



new, ordinary, command

code:string castable -> no output

Queues a new line to be created with code as its code.



add, ordinary

a:T, b:T -> x:T

a+b
A and B can be anything with defined addition. Addresses do not have defined addition, but can be casted to strings, which do. It can also be different types if they can be casted into each other in which case the program will do that, but relying on this is not good.



here, weird

no input -> x:address

Takes in no input, outputs an address referencing the words starts to end



slice, ordinary

a:address, start_1:int, end_1:int, scale:int -> x:address

If start_1 or end_1 is negative, they will be set to the size of a, plus themselves, allowing you to "count backwards" from the end of a. scale allows you to create a new address that is not contained within a.
slice makes a new address with a start of a.start+start_1-scale, and an end of a.start+end_1+scale.
If a="this |is a| line", slice a 4 -1 3="this i|s a l|ine" 
a can be a string as well.



parse, ordinary

a:string castable -> x:any

Executes a as code. parse can only take in collections with one element.



without, special

to remove:Collection, base:Collection -> x:Collection

outputs base with all elements it shares with to remove removed.



and, special

a:Collection, b:Collection -> x:Collection

outputs a and b combined into a single collection



flatten, special

a:Collection -> x:Collection

outputs a with all duplicate elements removed



word, ordinary

a:address -> x:address

outputs an address x which is a with its start extended to the start of the word if it is inside of a word, and with its end extended to the end of the word if it is inside of a word.



amount, special

a:Collection-> {x:int}

outputs a collection with the amount of elements in a as its only element.




size, ordinary

a:size defined-> x:int

outputs the size of a. for strings, the amount of characters. for ints, the amount of digits. for addresses, end-start. for collections, the amount of elements



start, ordinary

a:address -> x:int

start of a



end, ordinary

a:address -> x:int

end of a



int, ordinary

a:int castable -> a:int

casts a to an int



string, ordinary

a:string castable -> a:string

casts a to a string



line, ordinary

a:adress -> x:address

outputs an address referencing the entire line which a is in



match, weird

a:string castable, b:any, c:weird -> x:any

this is one of the most important words in WRain, so LISTEN UP. match is not a function. if you tried to model it as a function, the same input would be sent to different ouputs. However, it is "pure" in the functional programming sense.
match executes the code after it once for each element in b. each time, a will represent the current element.
suppose you had x={a,b}. word x x would be equal to {word a a, word a b, word b a, word b b}, because x is a collection. If instead you did match y {a,b} word y y, it would equal {word a a, word b b}. So match allows you to reuse data without creating new branches. 
Suppose you wanted to double every word after the keyword duplicate. 
put slice find "duplicate" 12 -1 2 word slice find "duplicate" 12 -1 2 is close to the code you would need, but because there could be multiple words you want to duplicate, this code would try to put every word thats after any instance of duplicate after every duplicate. which is obviously not what you want. instead, do 
match current slice find "duplicate" 12 -1 2 put current word current.




pack, special

a:Collection -> {a:Collection}

outputs a collection with a as its only element



unpack, ordinary/special/weird

{a:collection, b:collection, c:collection...} -> x:Collection
takes in a collection of collections packed with pack, and outputs a collection of all their elements. 
and a b={a,b}. 
pack and a b={{a,b}} 
and pack and a b pack and b c={{a,b},{b,c}}
unpack and pack and a b pack and b c={a,b,b,c}



invert, ordinary

a:T:invertible -> x:T:invertible

currently only defined for ints. outputs negative a.
