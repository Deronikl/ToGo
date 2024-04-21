from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import sys

# Создание карты с новыми центральными координатами и зумом
m = folium.Map(location=[47.2358, 39.7176], zoom_start=15)

# Добавление интерактивной Яндекс карты
folium.raster_layers.TileLayer(
    tiles='http://vec0{1-4}.maps.yandex.net/tiles?l=map&v=20.06.18-0&x={x}&y={y}&z={z}',
    attr='Яндекс',
    name='Яндекс Карты'
).add_to(m)

# Преобразование карты в HTML строку
html_map = m._repr_html_()

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Ростов_с_Друзьми")

layout = QVBoxLayout()

# Создание виджета для отображения HTML-кода
web_view = QWebEngineView()
web_view.setHtml(html_map)

layout.addWidget(web_view)

container = QWidget()
container.setLayout(layout)
window.setCentralWidget(container)

window.show()
sys.exit(app.exec_())