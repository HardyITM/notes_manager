"""Модуль `sqlite3` предоставляет интерфейс для работы с базами данных SQLite."""
import sqlite3


class NoteManager:
    """
    Класс для управления заметками в базе данных.
    """

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_notes_table()

    def create_notes_table(self):
        """
        Создание таблицы 'notes' в базе данных, если она не существует.
        """
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            """
            )

    def add_note(self, title, content):
        """
        Добавление новой заметки в базу данных.

        Args:
            title (str): Заголовок заметки.
            content (str): Содержание заметки.
        """
        with self.conn:
            self.conn.execute(
                "INSERT INTO notes (title, content) VALUES (?, ?)", (
                    title, content)
            )

    def view_all_notes(self):
        """
        Получение списка всех заметок.

        Returns:
            list: Список кортежей (id, title) всех заметок.
        """
        with self.conn:
            cursor = self.conn.execute("SELECT id, title FROM notes")
            notes = cursor.fetchall()
            return notes

    def search_notes(self, keyword):
        """
        Поиск заметок по ключевому слову в содержании.

        Args:
            keyword (str): Ключевое слово для поиска.

        Returns:
            list: Список кортежей (id, title) найденных заметок.
        """
        with self.conn:
            cursor = self.conn.execute(
                "SELECT id, title FROM notes WHERE content LIKE ?", (
                    f"%{keyword}%",)
            )
            matching_notes = cursor.fetchall()
            return matching_notes

    def delete_note(self, note_id):
        """
        Удаление заметки по её идентификатору.

        Args:
            note_id (int): Идентификатор заметки для удаления.
        """
        request = self.conn.execute("SELECT id FROM notes WHERE id = ?", (note_id,))
        existing_note = request.fetchone()
        if existing_note:
            with self.conn:
                self.conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
            return "Заметка успешно удалена!"
        return "Заметка с указанным идентификатором не существует."

    def get_note_details(self, note_id):
        """
        Получение подробной информации о заметке по её идентификатору.

        Args:
            note_id (int): Идентификатор заметки.

        Returns:
            tuple or None: Кортеж с информацией о заметке или None.
        """
        with self.conn:
            cursor = self.conn.execute(
                "SELECT title, content FROM notes WHERE id = ?", (note_id,)
            )
            matching_notes = cursor.fetchone()
            return matching_notes
