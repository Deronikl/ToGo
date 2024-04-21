from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import sys

class MapWithoutSearch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map without Search Functionality")
        layout = QVBoxLayout()

        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.create_map()

    def create_map(self):
        m = folium.Map(location=[47.2358, 39.7176], zoom_start=15)

        folium.raster_layers.TileLayer(
            tiles='http://vec0{1-4}.maps.yandex.net/tiles?l=map&v=20.06.18-0&x={x}&y={y}&z={z}',
            attr='Yandex',
            name='Yandex Maps'
        ).add_to(m)

        html_map = m._repr_html_()
        self.web_view.setHtml(html_map)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapWithoutSearch()
    window.show()
    sys.exit(app.exec_())

