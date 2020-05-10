import numpy as np
import random
import math
import generate_anki_deck as gen


def create_cloze_card_add_radicals():
    v = np.random.randint(1, 9, 3)
    eq = (
        "{{c1::\( %d \sqrt{%d} \)}}"
        " + "
        "{{c2::\( %d \sqrt{%d} \)}}"
        " = "
        "{{c3::\( %d \sqrt{%d} \)}}"
        ) % (v[0],v[2], v[1],v[2], (v[0]+v[1]),v[2])
    return eq

def create_cloze_card_subtract_radicals():
    v = np.random.randint(1, 9, 3)
    eq = (
        "{{c1::\( %d \sqrt{%d} \)}}"
        " - "
        "{{c2::\( %d \sqrt{%d} \)}}"
        " = "
        "{{c3::\( %d \sqrt{%d} \)}}"
        ) % (v[0],v[2], v[1],v[2], (v[0]-v[1]),v[2])
    return eq

def create_cloze_card_multiply_radicals(deck):
    v = np.random.randint(1, 9, 4)
    squareroot = math.sqrt(v[1]*v[3])
    if squareroot == math.floor(squareroot):
        result = "%d" % (v[0]*v[1]*v[2],)
    else:
        result = "%d \sqrt{%d}" % (v[0]*v[2], v[1]*v[3])
    eq = (
        "{{c1::\( %d \sqrt{%d} \)}}"
        " * "
        "{{c2::\( %d \sqrt{%d} \)}}"
        " = "
        "{{c3::\( %s \)}}"
        ) % (v[0], v[1], v[2], v[3], result)
    return eq

def create_cloze_card_divide_radicals(deck):
    v = np.random.randint(1, 9, 3)
    eq = (
        "{{c1::\( %d \sqrt{%d} \)}}"
        " / "
        "{{c2::\( %d \sqrt{%d} \)}}"
        " = "
        "{{c3::\( %d \)}}"
        ) % (v[0],v[2],v[1],v[2], (v[0]/v[1]))
    return eq


PROBLEM_GENERATORS = {
    'Adição': create_cloze_card_add_radicals,
    'Subtração': create_cloze_card_subtract_radicals,
    'Multiplicação': create_cloze_card_multiply_radicals,
    'Divisão': create_cloze_card_divide_radicals,
}

def generate_deck_of_problems(deck, deck_name, path, problem_quantities):
    problems = []
    for question_type, qtty in problem_quantities.items():
        for _ in range(qtty):
            problems.append(PROBLEM_GENERATORS[question_type]())
    random.shuffle(problems)
    for p in problems:
        gen.add_cloze_card(deck, p, '')
    gen.save_deck(deck, deck_name, path)
        

