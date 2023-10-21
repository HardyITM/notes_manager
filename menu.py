"""Модуль `NoteManager` предоставляет функционал для управления заметками используя SQLite."""
from notes_manager import NoteManager


def main():
    """
    Основная функция для взаимодействия с менеджером заметок.

    Она представляет меню пользователю с различными опциями для управления заметками,
    включая добавление, просмотр, поиск, удаление и просмотр подробной информации о заметках.
    """

    db_name = "notes.db"
    note_manager = NoteManager(db_name)

    while True:
        print_menu()
        choice = input("Введите номер действия: ")

        if choice == "1":
            add_note(note_manager)
        elif choice == "2":
            view_all_notes(note_manager)
        elif choice == "3":
            search_notes(note_manager)
        elif choice == "4":
            delete_note(note_manager)
        elif choice == "5":
            view_note_details(note_manager)
        elif choice == "6":
            break
        else:
            print("Неправильный выбор. Пожалуйста, выберите существующий номер действия.")

def print_menu():
    """
    Выводит на экран меню с возможными действиями для управления заметками.
    """
    print("Меню:")
    print("1. Добавить новую заметку")
    print("2. Просмотреть список всех заметок")
    print("3. Поиск заметок по ключевому слову")
    print("4. Удалить заметку")
    print("5. Просмотреть подробную информацию о заметке")
    print("6. Выйти")

def add_note(note_manager):
    """
    Получает данные заметки от пользователя и добавляет эту заметку в базу данных.
    """
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    note_manager.add_note(title, content)
    print("Заметка успешно добавлена!")

def view_all_notes(note_manager):
    """
    Извлекает все заметки из базы данных и выводит их.
    """
    notes = note_manager.view_all_notes()
    if notes:
        for note in notes:
            print(f"{note[0]}. {note[1]}")
    else:
        print('Заметки отсутствуют')

def search_notes(note_manager):
    """
    Получает ключевое слово от пользователя и ищет все заметки, связанные с этим ключевым словом.
    """
    keyword = input("Введите ключевое слово для поиска: ")
    matching_notes = note_manager.search_notes(keyword)
    if matching_notes:
        print("Найденные заметки:")
        for note in matching_notes:
            print(f"{note[0]}. {note[1]}")
    else:
        print("Заметки с заданным ключевым словом не найдены.")

def delete_note(note_manager):
    """
    Получает идентификатор заметки от пользователя и удаляет эту заметку из базы данных.
    """
    note_id = input("Введите номер заметки для удаления: ")
    if not note_id.isdigit():
        print("Неправильный номер заметки, возможно вы ввели не число.")
    else:
        result_message = note_manager.delete_note(note_id)
        print(result_message)

def view_note_details(note_manager):
    """
    Получает идентификатор заметки от пользователя и выводит подробную информацию о этой заметке.
    """
    note_id = input("Введите номер заметки для просмотра подробной информации: ")
    if not note_id.isdigit():
        print("Неправильный номер заметки, возможно вы ввели не число.")
    else:
        note = note_manager.get_note_details(note_id)
        if note:
            print(f"Заголовок: {note[0]}")
            print(f"Содержание: {note[1]}")
        else:
            print("Заметка с указанным номером не найдена.")

if __name__ == "__main__":
    main()
