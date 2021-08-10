import platform
import importlib

striking_string = importlib.import_module("00-beauty-of-python").__getattribute__('striking_string')


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

>> You may curious, what about apple? Are they the accumulated numbers?
Knowledge Point 2: Actually we call "apple" a string, just 
                   to regard it as a sequence as letter(number) placed continuously.
                   Shown as follows: {striking_string([ord(letter) for letter in "apple"], 
                                                      color='yellow', line_sep='')}.


"""


print(EXPLAIN)
