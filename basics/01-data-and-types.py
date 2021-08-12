import platform
import importlib

striking_string = importlib.import_module("00-beauty-of-python").__getattribute__('striking_string')
bucket = importlib.import_module("magics").__getattribute__('bucket')
magic_delete_last_of_bucket = importlib.import_module("magics").__getattribute__('magic_delete_last_of_bucket')
face_to_name = importlib.import_module("magics").__getattribute__('mapping')
persons = importlib.import_module("magics").__getattribute__('persons')
water_mapping = importlib.import_module("magics").__getattribute__('water_mapping')


PERSON_INFO_DICT = """'person_de_bucket': [],
                                                                   'person_de_name': 'Debbie',
                                                                   'person_de_gender': 'little boy',
                                                                   'person_de_phone': '110-120-119-114-10086'})
"""


EXPLAIN = f"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
                   {striking_string(bucket[:9], color='green', line_sep='')}
                   
                   Yeah! You just finished to write an example of how to reference a variable!
                   In every language, assignment is done by using "=", at left side is a new(blank)
                   variable that waiting to point to a value in some special structure in the memory.
                   
                   At the most lower level, we call the variable A "Pointer". Because it's just like 
                   a man telling you(CPU) where(address of real value in memory) is the restaurant to get a meal.
                   
                   In the next step, you used append method of list to append some variables into the container:
                   This works like, you arrived restaurant, and you are about to pickup whatever you like into 
                   a small basket. Every time you want to add something you want to eat, you have to ask for the 
                   service man for "where you guys put my favourite fish?? or SA NIAO NIU WAN??". They tell you an 
                   address, you go to the address, pick up the food you want to eat, and back to the service man, 
                   loop until you found it enough to eat.
                   
                   Last at the cashier, the service man print a receipt for you to check.
     
                   
>> OK, Now you are at home, how to take out a phone?
Knowledge Point 3: Access item in container!
                   Containers like list, tuple are support for indexing.
                   Indexing is just an operation of get item from a sequence by numeric order.
                   ** But everything in the IT world is starting from 0!!!!!
                   - So, if you want to get the first iPhone you put into the bucket, you need to write like this:
                   >> print(bucket[0])
                   - what if you want to get the last item put into the bucket? Is is need to count from scratch??
                   ** No, In Python, -1 is everywhere to represent the last one in a container:
                   >> print(bucket[-1])
                   - How to select a range of iPhone? Because I don't want to use versions before iPhone 6!!!
                   It's quite easy in Python to do this using a 'slice'!
                   ** A slice is a tuple composed by three integer! Like (0, 11, 2)! 
                      slice(0, 11, 2) means you want to start from 0, end smaller than 11(open bound, equal to 10)
                      and every time you go for next, you add 2 instead of 1.
                      Using 0 to 10 as an example, using slice to cut a list container contains 0 to 10, you will get:
                   >> print(list(range(0, 11, 2)))
                   >> {striking_string(list(range(0, 11, 2)), color='blue', line_sep='')}
                   So back to our case, if you want to use just the latest iPhone, you would write:
                   >> print(bucket[7: -1]) or just in abbr. print(bucket[7: ])
                   >> {striking_string(bucket[7: -1], color='yellow', line_sep='')}  # not using abbr.
                   >> {striking_string(bucket[7:], color='yellow', line_sep='')}  # using abbr.
                   
                   Oops! There is something wired! Look at the last one, delete it!
                   Its really simple to do!
                   >> del bucket[-1]
                   >> {striking_string(magic_delete_last_of_bucket(bucket), color='green', line_sep='')}


>> At real life, we always meet some case which need to be referred:
    - Find a person by his/her face.
    - Find a real name by his phone number.
    - Find the color in rgb by the common name. (Like color='green' or color='blue')
    - Look up a word in the dictionary, you should find the index page and quickly jump to the correct page.
    
    Hey, how to represent these real-life mapping in Python?
    In common, we can find that you are always want to quickly find something by a reference, and the reference you 
    look up is uniquely representing the object. Such a person has only one real face (mask not included).
    Then, using deep learning, converting multiple pictures of one person, and extracting its digit fingerprint:
    Like this example:
        1. 698d51a19d8a121ce581499d7b701668 -> Peter
        2. 99f30f737f3a513060a4906b948daf4a -> Debbie
        3.           ::                     ->   ::
        4.           ::                     ->   ::
        5.           ::                     ->   ::
    Our we can make it simple in our case:
        #  1                                -> Peter
        #  2                                -> Debbie
    Don't you think it's quite like a dictionary?
Knowledge Point 4: Yes, Python has a internal container type called "dict". 
                   A dict is just a mapping, and it looks like a mapping.
                   face_to_name = {"{1: 'Peter', 2: 'Debbie'}"}
                   >> print(face_to_name)
                   >> {striking_string(face_to_name, color='blue', line_sep='')}
                   
                   ** 1 is the key of 'Peter' and 'Peter' is the value of 1, we call [1, 'Peter'] a key-value pair.
                   To get items of the dict, using items() method.
                   
                   >> print(list(face_to_name.items()))
                   >> {striking_string(list(face_to_name.items()), color='blue', line_sep='')}
                   ** It's a contract that people treat the item[0] as the key, and item[1] as the value, 
                      just adapt to it.

Hey wait, look at the blue k-v pairs, it's wired! It's a list, and what in the list are not as the same as above,
rather, the item in the list is another list(Actually is a tuple, it's just an immutable list, in which
all items are not allowed to change) ! Yes, you can nest whatever you want into list, tuple, set, dict...
And we call it, Nested Structure.
Knowledge Point 5: Nested Structure!!!
                   Nested Structure is the most striking point when I'm new to program, especially when I first write
                   programs to store multiple students info into a single container.
                   Nested Structure are so flexible, you can put a dict into the first place of bucket, and also, 
                   a new bucket can be set as the first item's value.
                   Like this:
                   >> persons = []
                   >> person = 1
                   >> person_de_bucket = []
                   >> person_de_name = 'Debbie'
                   >> person_de_gender = 'little boy'
                   >> person_de_phone = '110-120-119-114-10086'
                   So we could pack it up as this: {striking_string(f"persons.append({'{'}{PERSON_INFO_DICT}"
                                                                    , color='green', line_sep='')}
                   How to get the first person's gender?
                   Well, you haven't know how to get a value in the dict according its key, time to tell you!
                   Get a value by key is so easy and it's just (using face_to_name, you want to get the name
                                                                whose face image fingerprint is 1): 
                   >> face_to_name[1]
                   >> {striking_string(face_to_name[1], color='yellow', line_sep='')}
                   
                   OK, But what if you want to change 'Peter' into 'Water'????
                   Well, its super easy too.
                   
                   >> face_to_name[1] = 'Water'  #  and that's all of it
                   >> {striking_string(water_mapping(face_to_name), color='yellow', line_sep='')}
                   
                   {striking_string("*** So, let's go back to 'HOW TO GET THE FIRST PERSON'S GENDER?'", color='red', 
                                    line_sep='')}
                   {striking_string("*** This is today's homework, please try to figure it out!", color='red', 
                                    line_sep='')}

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""


print(EXPLAIN)
