iPhone_3 = 'iPhone 3'
iPhone_4 = 'iPhone 3GS'
iPhone_5 = 'iPhone 4'
iPhone_6 = 'iPhone 4S'
iPhone_7 = 'iPhone 5'
iPhone_8 = 'iPhone 5C'
iPhone_9 = 'iPhone 6'
iPhone_10 = 'iPhone 7'
bucket = list()
bucket.append(iPhone_3)
bucket.append(iPhone_4)
bucket.append(iPhone_5)
bucket.append(iPhone_6)
bucket.append(iPhone_7)
bucket.append(iPhone_8)
bucket.append(iPhone_9)
bucket.append(iPhone_10)
bucket.append("iPhone 8")
bucket.append("iPhone 8 Plus")
bucket.append("iPhone X")
bucket.append("iPhone XS")
bucket.append("iPhone XS Max")
bucket.append("iPhone 11 ")
bucket.append("iPhone 11 Pro")
bucket.append("iPhone 11 Pro Max")
bucket.append("iPhone 12")
bucket.append("iPhone 10086")


def magic_delete_last_of_bucket(buc: list) -> list:
    del buc[-1]
    return buc[7:]


mapping = {1: 'Peter', 2: 'Debbie'}


def water_mapping(map_: dict):
    map_[1] = 'Water'
    return 'Water'


persons = [{
        'person_de_bucket': [],
        'person_de_name': 'Debbie',
        'person_de_gender': 'little boy',
        'person_de_phone': '110-120-119-114-10086'
    }]
