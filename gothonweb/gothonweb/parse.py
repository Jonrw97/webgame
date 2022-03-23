from gothonweb.lexicon import *

class ParseError(Exception):
    pass

class Sentence(object):

    def __init__(self, verb, obj, num):

        self.verb = verb[1]
        self.obj = obj[1]
        self.num = num[1]

def peek(word_list):

    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):

    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')
    skip(word_list, 'error')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        return ('error','missing verb')

def parse_object(word_list):
    skip(word_list, 'stop')
    skip(word_list, 'error')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        return ('error','missing object')

def parse_number(word_list):
    skip(word_list, 'stop')
    skip(word_list, 'error')
    next_word = peek(word_list)

    if next_word == 'numbers':
        return match(word_list, 'numbers')
    else:
        return ('numbers', None)


def parse_sentence(sentence):
    word_list = scan(sentence) 
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    num = parse_number(word_list)
    
    parsed = get_parse_sentence(Sentence(verb, obj, num))
    converted_parse = convertTuple(parsed)
    return converted_parse

def get_parse_sentence(parsed):
    if get_num(parsed):
        parsed = (parsed.num)
        return parsed
    else:
        parsed = (parsed.verb, parsed.obj)
        return parsed

def convertTuple(tup):
    str = ''.join(tup)
    return str

def get_num(word_list):
    if (word_list.num)==None:
        return False
    else:
        return True


