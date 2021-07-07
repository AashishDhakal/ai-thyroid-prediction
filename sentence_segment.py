import nltk

def sentence_segment(str, candidate_pos = ['NN', 'NNS', 'JJ', 'NNP', 'CD', 'RB', 'VBN', 'VBD']):
    tokens = nltk.word_tokenize(str)
    stopwords = {'old', 'meds'}
    keywordSent = []
    pos = nltk.pos_tag(tokens)
    i = 0
    while (i < len(pos)):
        sent = ""
              
        while (pos[i][1] in candidate_pos and pos[i][0] not in stopwords):
            sent += f"{pos[i][0]} "
            i += 1
                
        if (pos[i][1] not in candidate_pos) or (pos[i][0] in stopwords):
            i += 1
        if sent != "":
            keywordSent.append(sent.strip())

    return keywordSent