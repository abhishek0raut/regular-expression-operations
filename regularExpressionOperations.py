import re

# The `match` method matches a pattern at the beginning of a string
    def example_1():
    '''
    >>> example_1()
    <_sre.SRE_Match object; span=(0, 11), match='hello world'>
    '''
    hello_regex = re.compile(r,'Hello world')
    result = hello_regex.match('Hello world !')
    print(result)
    
    def example_2():
    '''
    >>> example_2()
    None
    '''
    hello_regex = re.compile(r'hello world')
    result = hello_regex.match('blah blah hello world')
    print(result)


# We can use the `search` method to find a pattern in the middle of string
    def example_3():
    '''
    >>> example_3()
    <_sre.SRE_Match object; span=(10, 21), match='hello world'>
    '''
    hello_regex = re.compile(r'hello world')
    result = hello_regex.search('blah blah hello world')
    print(result)

    def example_4():
    '''
    >>> example_4()
    <_sre.SRE_Match object; span=(0, 1), match='7'>
    '''
    digit_regex = re.compile(r'\d')
    result = digit_regex.match('7')
    print(result)

    def example_5():
    '''
    >>> example_5()
    <_sre.SRE_Match object; span=(0, 1), match='7'>
    '''
    digit_regex = re.compile(r'\d')
    result = digit_regex.match('78baxter')
    print(result)

    def example_6():
    '''
    >>> example_6()
    None
    '''
    digit_regex = re.compile(r'\d')
    result = digit_regex.match('Jet78')
    print(result)


    def example_7():
    '''
    >>> example_7()
    <_sre.SRE_Match object; span=(0, 1), match='b'>
    '''
    digit_regex = re.compile(r'\w')
    result = digit_regex.match('bMeyer468')
    print(result)
    
    def example_8():
    '''
    >>> example_8()
    <_sre.SRE_Match object; span=(4, 10), match='aaaaaa'>
    '''
    regex = re.compile(r'a+')
    result = regex.search('bbbbaaaaaabcd')
    print(result)
