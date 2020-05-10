import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIntValidator
from generate_algebra_problems import PROBLEM_GENERATORS, generate_deck_of_problems
import generate_anki_deck as gen
import random
import datetime as dt


app = QApplication(sys.argv)
window = QWidget()
main_layout = QVBoxLayout()
_txt_layout = QGridLayout()
textbox_values = dict()
for i, probname in enumerate(PROBLEM_GENERATORS.keys()):
    _text_box = QLineEdit()
    _text_box.setText("0")
    _text_box.setValidator(QIntValidator(0, 99))
    _txt_layout.addWidget(QLabel(probname), i, 0)
    _txt_layout.addWidget(_text_box, i, 1)
    textbox_values[probname] = (lambda v: lambda: int(v.text()))(_text_box)
main_layout.addLayout(_txt_layout)
_gerar_deck_layout = QHBoxLayout()
_gerar_deck_layout.addWidget(QLabel('Caminho de saída'))
_txt_caminho_saida = QLineEdit()
_gerar_deck_layout.addWidget(_txt_caminho_saida)
botao = QPushButton('Gerar deck do Anki')
def on_click_botao_gerar_deck():
    outpath = _txt_caminho_saida.text()
    prob_qtt = dict()
    for probname, get_value in textbox_values.items():
        prob_qtt[probname] = get_value()
    today_date = dt.datetime.now().strftime('%Y-%m-%d')
    deck_name = f'deck-{today_date}'
    deck = gen.create_deck(random.randint(1, 9999999999), deck_name)
    generate_deck_of_problems(deck, deck_name, outpath, prob_qtt)
    alert = QMessageBox()
    alert.setText('Deck gerado! Importe-o no Anki para treinar.\n')
    alert.exec_()
botao.clicked.connect(on_click_botao_gerar_deck)
_gerar_deck_layout.addWidget(botao)
main_layout.addLayout(_gerar_deck_layout)
window.setWindowTitle('Geração de problemas matemáticos')
window.setLayout(main_layout)
window.show()
sys.exit(app.exec_())