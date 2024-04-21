from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QScrollArea
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import sys
import geocoder

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
        self.current_location_button = QPushButton('Мое местоположение')
        self.current_location_button.setMaximumHeight(30)  
        self.exit_button = QPushButton('Выход')
        self.exit_button.setMaximumHeight(30)  

        self.search_button.clicked.connect(self.perform_search)
        self.current_location_button.clicked.connect(self.show_current_location)
        self.exit_button.clicked.connect(self.close_app)

        self.web_view = QWebEngineView()

        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.addWidget(self.place_input)
        scroll_layout.addWidget(self.search_button)
        scroll_layout.addWidget(self.result_label)
        scroll_layout.addWidget(self.current_location_button)
        scroll_layout.addWidget(self.exit_button)
        scroll_layout.addWidget(self.web_view)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        layout.addWidget(scroll_area)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def create_map(self, location):
        m = folium.Map(location=location, zoom_start=15)
        folium.Marker(location, popup='Ваше местоположение').add_to(m)
        html_map = m._repr_html_()
        self.web_view.setHtml(html_map)

    def find_coordinates_in_rostov(self, place_name):
        rostov_bounds = (47.1509, 39.7015, 47.3053, 39.8792)
        geolocator = Nominatim(user_agent="geo_tool")
        try:
            location = geolocator.geocode(place_name)
            if location and rostov_bounds[0] <= location.latitude <= rostov_bounds[2] and rostov_bounds[1] <= location.longitude <= rostov_bounds[3]:
                return (location.latitude, location.longitude)
            else:
                return None
        except GeocoderTimedOut:
            return None

    def perform_search(self):
        place_name = self.place_input.text()
        coordinates = self.find_coordinates_in_rostov(place_name)
        if coordinates:
            self.result_label.setText(f"Координаты места {place_name} в пределах Ростова-на-Дону: {coordinates}")
            self.create_map(coordinates)
        else:
            self.result_label.setText(f"Координаты для места {place_name} не найдены в пределах Ростова-на-Дону")

    def show_current_location(self):
        current_location = geocoder.ip('me')
        coordinates = (current_location.latlng[0], current_location.latlng[1])
        self.result_label.setText(f"Ваше текущее местоположение: {coordinates}")
        self.create_map(coordinates)

    def close_app(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapWithSearch()
    window.show()
    sys.exit(app.exec_())