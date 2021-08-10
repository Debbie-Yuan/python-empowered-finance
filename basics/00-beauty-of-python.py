
def striking_string(string: str, color: str = 'blue', line_sep='\n') -> str:
    _color_string_map = {
        'blue': '34',
        'yellow': '33',
        'red': '31',
        'green': '32'
    }
    return "{}\033[{}m{}\033[0m".format(line_sep, _color_string_map[color], string)


if __name__ == '__main__':
    import this  # noqa

    print(
        # striking_string("Feel free(fly) to try this out!", color='yellow')
        striking_string("Welcome to Python World!")
    )
