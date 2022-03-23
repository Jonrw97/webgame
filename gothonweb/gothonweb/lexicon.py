lexicon = {
    'shoot':'verb',
    'dodge':'verb',
    'tell': 'verb',
    'place':'verb',
    'throw':'verb',
    'joke':'noun',
    'jon':'noun',
    'guard':'noun',
    'bullet':'noun',
    'bomb':'noun',
    'up':'direction',
    'a':'stop',
    'the':'stop',
    'to':'stop',
    'in':'stop',
    'of':'stop',
    'by':'stop'
}


def scan(sentance):
    results = []
    line = sentance.lower()
    words = line.split()
    for word in words:
        word_type = lexicon.get(word)
        if word_type == None:
            try:
                int(word)
            except ValueError:
                results.append(('error', word))
            else:
                results.append(('numbers', word))
        else:
            results.append((word_type, word))
    return results