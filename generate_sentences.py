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
    'O': 'antithyroid',   
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
    target = item.get("Target")
    if target == '-':
        return "not diagnosed yet"
    target_list = [x for x in target]
    
    diag_list = []
    for x in target_list:
        if x in diagnostics:
            diag_list.append(x)

    if not len(diag_list):
        return "not diagnosed yet"

    diagnostic = diagnostics.get(diag_list[0])
    return f"diagnosed with {diagnostic}"


def check_meds_continuation(item):
    for t in item.get('Target'):
        if t in ['A', 'B', 'C', 'D']:
            meds = 'Cabimazole'
            break
        elif t in ['E', 'F', 'G', 'H']:
            meds = 'Thyroxine'
            break
        elif t in ['O']:
            meds = 'Methimazole'
            break
        else:
            meds = False
    return meds


with open("dataset.json") as f:
    with open('dataset.txt', 'w+') as txtfile:
        data = json.loads(f.read())

        for item in data:
            medication = "not on any"
            if item.get('on_thyroxine') == 't':
                medication = "on Thyroxine"
            elif item.get('on_antithyroid_medication') == 't':
                medication = "on Methimazole"
            elif item.get('query_hyperthyroid') == 't':
                medication = "on Cabimazole"
            tsh = 'not measured' if item.get('TSH_measured') == 'f' else item.get('TSH')
            t3 = 'not measured' if item.get('T3_measured') == 'f' else item.get('T3')
            tt4 = 'not measured' if item.get('TT4_measured') == 'f' else item.get('TT4')
            t4u_and_fti = f"T4U is measured {item.get('T4U')} with FTI {item.get('FTI')}"
            if item.get('FTI_measured') == 'f' and item.get('T4U_measured') == 'f':
                t4u_and_fti = f"T4U and FTI are not measured."
            elif item.get('FTI_measured') == 'f' and item.get('T4U_measured') == 't':
                t4u_and_fti = f"T4U is measured {item.get('T4U')} and FTI is not measured."
            else:
                t4u_and_fti = f"T4U is not measured and FTI is measured {item.get('FTI')}."
            continue_var = check_meds_continuation(item)

            if not continue_var:
                continue_status = 'stopped medication.'
            else:
                if item.get('query_hyperthyroid') == 't' or item.get('on_thyroxine') == 't' \
                        or item.get('on_antithyroid_medication') == 't':
                    continue_status = f'continued on {continue_var} meds.'
                else:
                    continue_status = f'started {continue_var} meds.'

            sentence = f'A {item.get("age")} year old {gender.get(item.get("sex"), "Patient")}, ' \
                f'is {medication} medication. {pronoun.get(item.get("sex"), "Patient")} consulted '\
                'an endocrinologist. ' + adjective.get(item.get("sex"), "Patient's") +\
                f' TSH level is {tsh}, T3 is {t3}, TT4 is {tt4}, {t4u_and_fti} {pronoun.get(item.get("sex"), "Patient")} '\
                f'is {get_diagnosis(item)}. {pronoun.get(item.get("sex"), "Patient")} {continue_status}\n'
            txtfile.write(sentence)
