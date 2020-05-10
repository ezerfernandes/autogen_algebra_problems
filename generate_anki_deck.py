import genanki
import os

CSS = """.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}
.cloze {
 font-weight: bold;
 color: blue;
}
.nightMode .cloze {
 color: lightblue;
}
"""


_simple_model = genanki.Model(
    2383734, 'Simple model',
    fields=[dict(name='Question'), dict(name='Answer'), dict(name='Tags')],
    templates=[
        dict(
            name='Card 1',
            qfmt='<div>{{Question}}</div>',
            afmt='{{FrontSide}}<hr id="answer"><div>{{Answer}}</div>',
            )])


_cloze_model = genanki.Model(
    998877661,
    'My Cloze Model',
    fields=[
        {'name': 'Text'},
        {'name': 'Extra'},
    ],
    templates=[{
        'name': 'My Cloze Card',
        'qfmt': '{{cloze:Text}}',
        'afmt': '{{cloze:Text}}<br>{{Extra}}',
    },],
    css=CSS,
    model_type=genanki.Model.CLOZE)

def create_deck(id, title):
    deck = genanki.Deck(id, title)
    return deck

def add_simple_card(deck, question, answer):
    new_note = genanki.Note(
        model=_simple_model,
        fields=[question, answer])
    deck.add_note(new_note)

def add_cloze_card(deck, cloze_text, extra, tags=None):
    new_note = genanki.Note(
        model=_cloze_model,
        fields=[cloze_text, extra],
        tags=tags,
        )
    deck.add_note(new_note)

def save_deck(deck, deck_name, path):
    genanki.Package(deck).write_to_file(os.path.join(path, f'{deck_name}.apkg'))