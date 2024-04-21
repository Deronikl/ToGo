import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QCheckBox
from PyQt5.QtCore import Qt
import PyQt5.QtCore

class ShoppingListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.shopping_list = []

        self.setWindowTitle("Список покупок")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.layout = QVBoxLayout()

        self.product_input = QLineEdit()
        self.quantity_input = QLineEdit()

        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.add_product)

        self.shopping_list_widget = QListWidget()

        mark_as_bought_button = QPushButton("Пометить как купленные")
        mark_as_bought_button.clicked.connect(self.mark_as_bought)

        delete_checked_button = QPushButton("Удалить отмеченные")
        delete_checked_button.clicked.connect(self.delete_checked_items)

        self.layout.addWidget(self.product_input)
        self.layout.addWidget(self.quantity_input)
        self.layout.addWidget(add_button)
        self.layout.addWidget(self.shopping_list_widget)
        self.layout.addWidget(mark_as_bought_button)
        self.layout.addWidget(delete_checked_button)

        self.setLayout(self.layout)

    def add_product(self):
        product = "    " + self.product_input.text()
        quantity = self.quantity_input.text()
        item = f"{product} - {quantity}"
        self.shopping_list_widget.addItem(item)

    def mark_as_bought(self):
        for i in range(self.shopping_list_widget.count()):
            item = self.shopping_list_widget.item(i)
            checkbox = QCheckBox("")
            self.shopping_list_widget.setItemWidget(item, checkbox)

    def delete_checked_items(self):
        for i in range(self.shopping_list_widget.count()):
            item = self.shopping_list_widget.item(i)
            widget = self.shopping_list_widget.itemWidget(item)
            if isinstance(widget, QCheckBox) and widget.isChecked():
                self.shopping_list_widget.takeItem(i)

def run():
    app = QApplication(sys.argv)
    shopping_list_app = ShoppingListApp()
    shopping_list_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()