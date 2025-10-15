import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget
from api_client import obtener_juegos_mas_populares


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Top 50 Juegos Más Populares 🎮")
        self.setGeometry(300, 200, 600, 600)

        # Widgets y Layout principal
        self.layout = QVBoxLayout()
        self.btn_cargar = QPushButton("Cargar Top 50 Juegos")
        self.lista_juegos = QListWidget()

        # Agregamos widgets al layout
        self.layout.addWidget(self.btn_cargar)
        self.layout.addWidget(self.lista_juegos)
        self.setLayout(self.layout)

        # Conectar evento al botón
        self.btn_cargar.clicked.connect(self.cargar_juegos)

        # Lista para almacenar los juegos
        self.juegos = []

    def cargar_juegos(self):
        """Carga los 50 juegos más populares desde la API"""
        self.juegos = obtener_juegos_mas_populares(50)
        self.lista_juegos.clear()

        if not self.juegos:
            self.lista_juegos.addItem("❌ No se pudieron cargar los juegos.")
            return

        # Mostrar cada juego en la lista
        for juego in self.juegos:
            titulo = juego.get('title', 'Sin título')
            genero = juego.get('genre', 'Sin género')
            plataforma = juego.get('platform', 'Desconocido')
            self.lista_juegos.addItem(f"{titulo} - {genero} ({plataforma})")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())
