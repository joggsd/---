import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# ui.py에서 정의한 Ui_MainWindow 클래스를 가져옵니다.
from ui import Ui_MainWindow

class CalculatorApp(QMainWindow):
    def __init__(self):
        """
        생성자: UI를 설정하고 시그널과 슬롯을 연결합니다.
        """
        super().__init__()

        # UI를 초기화합니다.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # '계산' 버튼의 clicked 시그널을 calculate_sum 메서드(슬롯)에 연결합니다.
        self.ui.calculate_button.clicked.connect(self.calculate_sum)

    def calculate_sum(self):
        """
        두 입력창의 값을 더하여 결과 라벨에 표시하는 메서드입니다.
        """
        try:
            # 입력창에서 텍스트를 가져와 float으로 변환합니다.
            num1 = float(self.ui.input1.text())
            num2 = float(self.ui.input2.text())

            # 두 숫자를 더합니다.
            result = num1 + num2

            # 결과 라벨에 계산 결과를 문자열로 변환하여 설정합니다.
            self.ui.result_label.setText(str(result))
        except ValueError:
            # 숫자로 변환할 수 없는 값이 입력된 경우 에러 메시지를 표시합니다.
            self.ui.result_label.setText("숫자만 입력하세요")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())