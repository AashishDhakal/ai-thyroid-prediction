import json

diagnostics = {
    'A': 'hyperthyroid',
    'B': 'T3 toxic',
    'C': 'toxic goitre',
    'D': 'secondary toxic',
    'E': 'hypothyroid',
    'F': 'primary hypothyroid',
    'G': 'compensated hypothyroid',
    'H': 'secondary hypothyroid',
    'I': 'increased binding protein',
    'J': 'decreased binding protein',
    'K': 'concurrent non-thyroidal illness',
    'L': 'consistent with replacement therapy',
    'M': 'underreplaced',
    'N': 'overreplaced',
    'O': 'antithyroid drugs',
    'P': 'I131 treatment',
    'Q': 'surgery',
    'R': 'discordant assay results',
    'S': 'elevated TBG',
    'T': 'elevated thyroid hormones'    
}

gender = {
    "M": "Male",
    "F": "Female"
}


adjective = {
    "M": "His",
    "F": "Her"
}

pronoun = {
    "M": "He",
    "F": "She"
}

def get_diagnosis(item):
    target = item.get('Target')
    if target == '-':
        return 'not diagnosed yet'
    diagnostic = ''
    for i in range(0, len(target)):
        try:
            if i == 0:
                diagnostic = diagnostic + diagnostics[target[i]]
            else:
                diagnostic = diagnostic + ',' + diagnostics[target[i]]
        except KeyError:
            continue
    return f"diagnosed with {diagnostic}"


with open("dataset.json") as f:
    with open('dataset.txt', 'w+') as txtfile:
        data = json.loads(f.read())
        for item in data:
            medication = "not on any"
            if item.get('on_thyroxine') == 't':
                medication = "on thyroxine"
            elif item.get('on_antithyroid_medication') == 't':
                medication = "on methimazole"
            tsh = 'not measured' if item.get('TSH_measured') == 'f' else item.get('TSH')
            tt4 = 'not measured' if item.get('TT4_measured') == 'f' else item.get('TT4')
            t4u_and_fti = f"T4U is measured {item.get('T4U')} with FTI {item.get('FTI')}"
            if item.get('FTI_measured') == 'f' and item.get('T4U_measured') == 'f':
                t4u_and_fti = f"T4U and FTI are not measured"
            elif item.get('FTI_measured') == 'f' and item.get('T4U_measured') == 't':
                t4u_and_fti = f"T4U is measured {item.get('T4U')}"
            else:
                t4u_and_fti = f"T4U is not measured and FTI is measured {item.get('FTI')}"
            sentence = f"A {item.get('age')} year old {gender.get(item.get('sex'), '')} , is {medication} medication.{pronoun.get(item.get('sex'), '')} consulted an endocrinologist. {adjective.get(item.get('sex'), '')} TSH level is {tsh}, TT4 is {tt4}, {t4u_and_fti}. {pronoun.get(item.get('sex'), '')} is {get_diagnosis(item)}. {pronoun.get(item.get('sex'), '')} continued on thyroxine meds.\n"
            txtfile.write(sentence)
