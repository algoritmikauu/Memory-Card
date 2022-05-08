#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QButtonGroup
from random import shuffle, randint
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def show_result():
    RadioGroupButton.hide()
    AnsGroupBox.show()
    button.setText("Следующий вопрос")

def show_question():
    AnsGroupBox.hide()
    RadioGroupButton.show()
    button.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_question.setText(q.question)
    b.setText(q.right_answer)
    show_question()
def show_correct(res):
    a.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct("Правильно!")
        main_win.score += 1
        print("Статистика:")
        print("Всего вопросов:", main_win.total)
        print("Правильных ответов:", main_win.score)
        print("Рейтинг:", main_win.score/main_win.total * 100,"%")
    else:
        show_correct("Неверно!")
        print("Неверно:", main_win.total-main_win.score)
        print("Статистика:")
        print("Всего вопросов:", main_win.total)
        print("Правильных ответов:", main_win.score)
        print("Рейтинг:", main_win.score/main_win.total * 100,"%")

def next_question():
    main_win.total += 1
    print("Статистика:")
    print("Всего вопросов:", main_win.total)
    print("Правильных ответов:", main_win.score)
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q)

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

app = QApplication([])
#окно приложения
main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(600, 400)
lb_question = QLabel("Какой национальности не существует?")

RadioGroupButton = QGroupBox("Варианты ответов")
RadioGroup = QButtonGroup()
rbtn1 = QRadioButton("Энцы")
rbtn2 = QRadioButton("Смурфы")
rbtn3 = QRadioButton("Чулымцы")
rbtn4 = QRadioButton("Алеуты")
answer = [rbtn1, rbtn2, rbtn3, rbtn4]

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupButton.setLayout(layout_ans1)
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
#кнопка
button = QPushButton("Ответить")

AnsGroupBox = QGroupBox('Результат теста')

a = QLabel("Правильно/Неправильно")
b = QLabel('Правильный ответ')

layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(a, alignment = Qt.AlignLeft)
layout_ans4.addWidget(b)

AnsGroupBox.setLayout(layout_ans4)
AnsGroupBox.show()

layout = QVBoxLayout()

layout.addWidget(lb_question)
layout.addWidget(RadioGroupButton)
layout.addWidget(AnsGroupBox)
layout.addWidget(button)

main_win.setLayout(layout)

question_list = []
q1 = Question('В каком году Европейский Союз впервые ввел евро в качестве валюты?', '1999', '1985', '2003', '2001')
question_list.append(q1)
q2 = Question('Какой национальный цветок Японии?', 'Сакура', 'Ромашка', 'Хокайд', 'Кеоке')
question_list.append(q2)
q3 = Question('Сколько полос на флаге США?', '13', '12', '14', '11')
question_list.append(q3)
q4 = Question('Какое национальное животное Австралии?', 'Красный кенгуру', 'Пеликан', 'Черный скорпион', 'Тарантул')
question_list.append(q4)
q5 = Question('До 1923 года как назывался турецкий город Стамбул?', 'Константинопль', 'Амстердам', 'Варшава', 'Нимен')
question_list.append(q5)
q6 = Question('Кто открыл пенициллин?', 'Александр Флеминг', 'Джон Фемельгтон', 'Пенни Амберт', 'Николай Броздов')
question_list.append(q6)
q7 = Question('В 1952 году президентом какой страны был предложен Альберт Эйнштейн?', 'Израиль', 'Германия', 'Франция', 'Польша')
question_list.append(q7)
q8 = Question('Где находится самая маленькая кость человека?', 'Ухо', 'Нога', 'Рука', 'Голова')
question_list.append(q8)
q9 = Question('Почему Александр Македонский требовал от своих солдат брить бороды', 'Чтобы враг не смог ухватить их за них', 'Для красоты', 'Для удобства', 'Защита')
question_list.append(q9)
q10 = Question('Для чего в прошлом веке американские шахтеры брали с собой в шахту клетки с канарейками', 'Для обнаружения газов метана', 'От скуки', 'Для отпугивания летучих мышей', 'Поесть')
question_list.append(q10)

button.clicked.connect(click_ok)
main_win.total = 0
main_win.score = 0
next_question()

main_win.show()

app.exec()