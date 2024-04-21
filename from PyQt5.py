from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QScrollArea
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import sys

class MapWithSearch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map with Search Functionality")
        layout = QVBoxLayout()

        self.place_input = QLineEdit()
        self.place_input.setMaximumHeight(30)
        self.search_button = QPushButton('Найти на карте')
        self.result_label = QLabel()
        self.result_label.setMaximumHeight(30)
        self.exit_button = QPushButton('Выход')
        self.exit_button.setMaximumHeight(30)

        self.search_button.clicked.connect(self.perform_search)
        self.exit_button.clicked.connect(self.close_app)

        self.web_view = QWebEngineView()

        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.addWidget(self.place_input)
        scroll_layout.addWidget(self.search_button)
        scroll_layout.addWidget(self.result_label)
        scroll_layout.addWidget(self.exit_button)
        scroll_layout.addWidget(self.web_view)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        layout.addWidget(scroll_area)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def create_map(self, locations):
        m = folium.Map(location=[47.235713, 39.701505], zoom_start=12)
        for location in locations:
            folium.Marker(location, popup='Место').add_to(m)
        html_map = m._repr_html_()
        self.web_view.setHtml(html_map)

    def perform_search(self):
        place_name = self.place_input.text()
        locations = []
        geolocator = Nominatim(user_agent="geo_tool")
        try:
            location = geolocator.geocode(place_name)
            if location:
                address = location.address.split(', ')
                for addr in address:
                    if place_name.lower() in addr.lower():
                        coordinates = (location.latitude, location.longitude)
                        locations.append(coordinates)
        except GeocoderTimedOut:
            pass

        if locations:
            self.result_label.setText(f"Найдено место '{place_name}'")
            self.create_map(locations)
        else:
            self.result_label.setText(f"Место '{place_name}' не найдено")

    def close_app(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapWithSearch()
    window.show()
    sys.exit(app.exec_())