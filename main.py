# Python Crash Course kapitel 2

# Metode
def print_hi(name):
    # try it yourself 2-1 og 2-2.
    msg: str = name
    print(msg)

    msg = 'hostile variable takeover from prograMMer'
    print(msg)

    # try it yourself 2-3 og 2-4
    print(msg.title())
    print(msg.upper())
    print(msg.lower())
    original_msg = '     Hello World     '
    full_msg = f'{original_msg.strip()} - {msg}{"!"}!'
    print(full_msg.title())

    # try it yourself 2-5
    famous_quote = 'Marcus Aurelius once wrote: "It was for the best, so nature had no choice but to do it"'
    print(famous_quote)

    # try it yourslef 2-6 og 2-7
    famous_person = ' marcus aurelius '
    quote = '"It was for the best, so nature had no choice but to do it"'
    text = f'{famous_person.strip().title()} once wrote: {quote}'
    print(text)

    # why is this so provoking ???
    first_number = 0.2
    second_number = 0.1
    third_number = 3

    result_1 = first_number + second_number
    result_2 = third_number * second_number
    print(result_1)
    print(result_2)

    # try it yourself 2-8
    print(3 + 5)
    print(2 ** 3)
    print(10 - 2)
    print(6 - -2)

    # try it yourself 2-9
    favourite = 'My favourite number is: '
    number = 10
    print(f'{favourite.strip()} {number}')

    # try it yourself 2-10
    '''
    here's
    a
    comment
    block
    '''  # comment block

    # another comment block
    #
    #
    #
    #
    #
    # another comment block

    # try it yourself 2-11
    import this
    print(this.s)


# Metodekald
if __name__ == '__main__':
    param = 'Hello World'
    print_hi(param)
