import platform
import importlib

striking_string = importlib.import_module("00-beauty-of-python").__getattribute__('striking_string')
bucket = importlib.import_module("magics").__getattribute__('bucket')


EXPLAIN = f"""
Data types are the most basics of computer science, because all of the known theory
so called as "Information Tech" are bound to be stored in somewhere subjected to some structure.

A fundamental knowledge is that computers using a stick-bar liked container to store data, which called MEMORY.
——————————————————————————————————————————————————————————————————————————————————————————————>
｜
｜         0        1        2        3        4        5        6        7        8  ... ...
｜   - - - -, - - - -, - - - -, - - - -, - - - -, - - - -, - - - -, - - - -, - - - -  ... ...
｜   0 0 1 0, 1 0 1 1, 0 1 0 1, 1 1 1 0, 0 1 1 0, 1 0 1 1, 0 1 0 1, 1 1 1 1, 0 0 0 1  ... ...
｜
｜   As you seen in the figure, no matter which kind of data, they are all represented by "bit" in a single sequence.
——————————————————————————————————————————————————————————————————————————————————————————————>

>>You may curious, how can I tell from a totally messed up pile of zero and one???
Knowledge Point 0: Please make yourself comfort for using 0 
                   as the first happen event in computer world!!
                   How would we introduce a contract, try to read every 16 bits as an number?
                   YES, dude, "every <length> bits as an number" is just the definition of word-length in IT.
                   Nowadays, our computer are most likely to be 64bit, which means your cpu read from memory
                   at a step-length of 64 to recognize a number. Commonly, an integer(整数) is 64bit.
                   Here is word-length of your computer: {striking_string(platform.architecture(), line_sep='')}


>>So you must be curious, how can a computer represent a letter 'A' 
>>and how to even store a pile of 'A's in an excel file.
This is all about of DATA TYPE & DATA STRUCTURE.
Knowledge Point 1: All data are just numbers, 
                   It's confusing at first but in fact, 'A' is just {striking_string(ord('A'), line_sep='')}.
                   We call 'A' as a type of char.


>> You may curious, what about a word of "apple"? Are they the accumulated numbers?
Knowledge Point 2: Actually we call "apple" a string, just 
                   to regard it as a sequence as letter(number) placed continuously.
                   Shown as follows: {striking_string([ord(letter) for letter in "apple"], 
                                                      color='yellow', line_sep='')}.


>> Also, you must curious about how to hold a pile of "apple" just as how to put 10 iPhone in to a bucket.
Knowledge Point 3: This is just a relationship between items and placeholder(aka. container).
                   You put many basic items in to an item-container.
                   You can also put as many as strings as you want in Python, it's quite simple!
                   SEE THAT EXAMPLE:
                   Let's assume you have 7 iPhone:
                   >> iPhone_3 = 'iPhone 3'
                   >> iPhone_4 = 'iPhone 3GS'
                   >> iPhone_5 = 'iPhone 4'
                   >> iPhone_6 = 'iPhone 4S'
                   >> iPhone_7 = 'iPhone 5'
                   >> iPhone_8 = 'iPhone 5C'
                   >> iPhone_9 = 'iPhone 6'
                   >> iPhone_10 = 'iPhone 7'
                   Let's put all these iPhones into our market bucket!
                   >> bucket = list()
                   >> bucket.append(iPhone_3)
                   >> bucket.append(iPhone_4)
                   >> bucket.append(iPhone_5)
                   >> bucket.append(iPhone_6)
                   >> bucket.append(iPhone_7)
                   >> bucket.append(iPhone_8)
                   >> bucket.append(iPhone_9)
                   >> bucket.append(iPhone_10)
                   Let's print the bucket out!
                   >> print(bucket)
                   {striking_string(bucket, color='green', line_sep='')}
"""


print(EXPLAIN)
