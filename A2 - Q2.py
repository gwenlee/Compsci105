

def read_sentence(sentence, max_letters):
    try:
        new_list = []
        if len(sentence[0]) > max_letters:
            new_list = get_definition(sentence[0])
            read_sentence(new_list,max_letters)
            read_sentence(sentence[1:],max_letters)
        else:
            old = [sentence[0]]
            print(str(old).strip("['']"),end=" ")
            read_sentence(sentence[1:], max_letters)
    except IndexError:
        pass

def get_definition(word):
    if word == 'sentence':
        return ['set', 'of', 'words']
    if word == 'difficult':
        return ['not', 'easy']

read_sentence(['this','sentence','is','difficult', 'to', 'read'],7)            
