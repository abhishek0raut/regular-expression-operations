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
