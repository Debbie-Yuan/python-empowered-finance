import importlib
from typing import Optional

striking_string = importlib.import_module("00-beauty-of-python").__getattribute__('striking_string')

persons = [{
        'person_de_bucket': [],
        'person_de_name': 'Debbie',
        'person_de_gender': 'little boy',
        'person_de_phone': '110-120-119-114-10086'
    }]


def write_your_answer_here() -> Optional[str]:
    _ = "How to get the first person's gender?"
    gender = None
    # TODO Implement your code here:

    # Your Implementation.
    return gender


if __name__ == '__main__':
    color, message = ('green', 'Well done, perfectly correct!') \
        if write_your_answer_here() == 'little boy' else ('red', 'Emmmmm, Not correct。。。')
    print(striking_string(message, color=color))
