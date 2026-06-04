"""Точка входа в приложение."""

import sys

from PySide6.QtWidgets import QApplication, QMessageBox

from DataBase.database import Database
from UserInterface.login_window import LoginWindow


def main():
    app = QApplication(sys.argv)

    try:
        db = Database()
    except Exception as e:
        QMessageBox.critical(
            None, "Ошибка подключения к БД",
            f"Не удалось подключиться к базе данных:\n{e}\n\n"
            "Проверьте настройки в constants.py и что PostgreSQL запущен.")
        sys.exit(1)

    window = LoginWindow(db)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()