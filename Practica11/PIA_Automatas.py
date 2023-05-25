import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QRegExpValidator
from PyQt5.QtCore import Qt, QRegExp

class BonitaInterfaz(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Validar cadenas")
        self.setFixedSize(340, 200)

        self.LblBackground = QLabel(self)
        self.LblBackground.setGeometry(0, 0, 340, 250)
        self.LblBackground.setStyleSheet("background-image: url(img/background.jpg);")
        
        self.LblTitle = QLabel("WcW | W={a,b}*", self)
        self.LblTitle.setGeometry(112, 30, 250, 25)
        self.LblTitle.setStyleSheet("font-size: 15px; font-weight: bold; color: #FFFFFF;")

        self.LblVCad = QLabel("Ingresa una cadena:", self)
        self.LblVCad.setGeometry(112, 60, 130, 20)
        self.LblVCad.setStyleSheet("font-size: 13px; font-weight: bold; color: #FFFFFF;")

        self.TxtVCadena = QLineEdit(self)
        self.TxtVCadena.setGeometry(60, 100, 230, 20)
        self.TxtVCadena.setStyleSheet("font-size: 12px; border: none; border-bottom: 1px solid")
        self.TxtVCadena.setText("")


        # Establecer el validador de expresión regular para aceptar solo minúsculas
        validator = QRegExpValidator(QRegExp("^[a-z]+$"))
        self.TxtVCadena.setValidator(validator)

        self.TxtVCadena.textChanged.connect(self.convertir_a_minusculas)

        self.PanelButton = QPushButton("Validar", self)
        self.PanelButton.setGeometry(130, 140, 85, 30)
        self.PanelButton.setStyleSheet("font-size: 12px; background-color: #3F8AB2; color: #FFFFFF;")
        self.PanelButton.clicked.connect(self.validar_cadena)

    def convertir_a_minusculas(self):
        texto_actual = self.TxtVCadena.text()
        texto_minusculas = texto_actual.lower()
        if texto_actual != texto_minusculas:
            self.TxtVCadena.setText(texto_minusculas)

    def validar_cadena(self):
        cadena = self.TxtVCadena.text()
        caracteres = list(cadena)

        if 'c' not in caracteres:
            QMessageBox.warning(self, "Advertencia", "La letra 'c' no se encuentra en la cadena")
            return

        c = caracteres.index("c")
        iz = cadena[:c]
        der = cadena[c + 1:]

        if all(caracter == 'a' or caracter == 'b' for caracter in iz):
            if iz == der:
                QMessageBox.information(self, "Información", "La cadena es válida")
            else:
                QMessageBox.warning(self, "Información", "La cadena es inválida")
        else:
            QMessageBox.warning(self, "Advertencia", "La cadena contiene caracteres diferentes a 'a' y 'b'")

    def closeEvent(self, event):
        # Lógica para cerrar la aplicación correctamente
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = BonitaInterfaz()
    ventana.show()
    sys.exit(app.exec_())
