import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import random
class PartyPlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Party Planner')

        self.label = QLabel('Всем участникам вечеринки есть 18?', self)

        self.button_yes = QPushButton('Да', self)
        self.button_yes.clicked.connect(self.on_yes_clicked)

        self.button_no = QPushButton('Нет', self)
        self.button_no.clicked.connect(self.on_no_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_yes)
        layout.addWidget(self.button_no)

        self.setLayout(layout)

        self.show()

    def on_yes_clicked(self):
        self.random_activity(True)

    def on_no_clicked(self):
        self.random_activity(False)

    def random_activity(self, adults_only):
        foodlist = ["Пицца (каждый может выбрать свои любимые начинки)",
                    "Тако или фахитас (с различными видами начинок и соусов)",
                    "Суши роллы (подготовить различные ингредиенты и научиться складывать роллы)",
                    "Бургеры (с разнообразными видами фарша и топпингов)",
                    "Лазанья (можно подготовить несколько видов: классическая, овощная, с морепродуктами)",
                    "Гуакамоле и сальса (свежие закуски к чипсам)",
                    "Шашлык (подготовить маринады и различные виды мяса)",
                    "Фруктовый салат (разнообразие фруктов и ягод, можно добавить йогурт или мед)",
                    "Домашние пирожки (с различными начинками: мясные, капустные, сладкие)"]
        activities18 = ["Дегустация вин или других напитков"]
        activities = [
            "Викторина",
            "Караоке",
            "Настольные игры",
            "Тематический квест",
            "Вечеринка с костюмами",
            "Фотосессия",
            "Танцы",
            "Чтение стихов или коротких рассказов",
            "Игра 'Мафия'",
            "Кинопросмотр",
            "Различные конкурсы и эстафеты",
            "Показ мод",
            "Обсуждение интересных тем",
            "Совместное приготовление ужина",
            "Командные игры и соревнования",
            "DIY проекты (создание чего-то своими руками)",
            "Пикник",
            "Вечеринка с танцевальными баттлами",
            "Вечеринка с живой музыкой",
            "Вечеринка с тематическими активностями (например, диско-вечеринка, вечеринка в стиле 80-х и т. д.)",
            "Квиз-шоу",
            "Вечеринка с караоке-баттлами",
            "Медитация или йога",
            "Вечеринка с просмотром звездного неба",
            "Вечеринка с тематическими костюмами",
            "Вечеринка с играми на свежем воздухе",
            "Вечеринка с тематическими декорациями",
            "Вечеринка с фейерверками",
            "Кулинарный баттл",
            "Совместное посещение квест-комнаты",
            "Вечеринка с фильмами под открытым небом",
            "Экскурсия по достопримечательностям города",
            "Спортивные соревнования",
            "Вечеринка с дегустацией различных видов чая или кофе",
            "Мастер-класс по созданию коктейлей"
        ]

        if adults_only:
            random_text = random.choice(activities + activities18)
            print(random_text)
        else:
            random_text = random.choice(activities)
            print(random_text)
        if random_text == "Совместное приготовление ужина":
            random_food = random.choice(foodlist)
            print('Мы выбрали для вас блюдо:', random_food)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    party_planner = PartyPlanner()
    sys.exit(app.exec_())
