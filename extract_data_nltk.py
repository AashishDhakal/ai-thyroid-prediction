from sentence_segment import sentence_segment
import nltk

GENDER = {
    'Male': 'M',
    'Female': 'F'
}

MEDICATION = [
    'Thyroxine',
    'Cabimazole',
    'Methimazole'
]

DIAGNOSTICS = [
    'hyperthyroid',
    'T3 toxic',
    'toxic goitre',
    'secondary toxic',
    'hypothyroid',
    'primary hypothyroid',
    'compensated hypothyroid',
    'secondary hypothyroid',
    'concurrent non-thyroidal illness',
    'antithyroid',
]


def data_in_list_check(tokens, data):
    empt_list = []
    for x in tokens:
        for y in x.split():
            empt_list.append(y)
    if data in empt_list:
        return True
    else:
        return False


def value_check(tokens, data):
    pos = nltk.pos_tag(nltk.word_tokenize(tokens[tokens.index(data) + 1]))
    for x in pos:
        if x[1] == 'CD':
            measured_data = x[0]
            break
        else:
            measured_data = 'none'
    return measured_data


def check_diagnosis(tokens):
    try:
        data = tokens[tokens.index('diagnosed') + 1]
        return data if data in DIAGNOSTICS else 'none'
    except ValueError:
        return 'none'


with open("dataset.txt") as txtfile:
    data = txtfile.read()
    data_list = data.split('\n')
    
    i = 0
    
    for item in data_list:
        if i > 15 and i < 19:

            print(item, end="\n\n")

            tokens = sentence_segment(item)

            print(tokens, end="\n\n")

            out = dict()
            out['age'] = tokens[0].split()[0]
            out['gender'] = GENDER.get(tokens[1]) if tokens[1] in GENDER else '-'
            out['query_hypothyroid'] = 'true' if data_in_list_check(tokens, MEDICATION[0]) else 'false'
            out['query_hyperthyroid'] = 'true' if data_in_list_check(tokens, MEDICATION[1]) else 'false'
            out['query_antithyroid'] = 'true' if data_in_list_check(tokens, MEDICATION[2]) else 'false'
            out['tsh_level'] = value_check(tokens, 'TSH level')
            out['t3'] = value_check(tokens, 'T3')
            out['tt4'] = value_check(tokens, 'TT4')
            out['t4u'] = value_check(tokens, 'T4U')
            out['fti'] = value_check(tokens, 'FTI')
            out['diagnosis'] = check_diagnosis(tokens)

            print(out, end="\n\n")

        if i > 19:
            break

        i += 1
