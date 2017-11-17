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