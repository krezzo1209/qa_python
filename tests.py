from main import BooksCollector
import pytest


class TestBooksCollector:

    def setup_method(self):
        # Создаем новый экземпляр перед каждым тестом
        self.collector = BooksCollector()

    def test_add_new_book_add_two_books(self):
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(self.collector.get_books_genre()) == 2

    def test_add_new_book_with_empty_name(self):
        self.collector.add_new_book('')
        assert len(self.collector.get_books_genre()) == 0

    def test_add_new_book_with_long_name(self):
        long_name = 'a' * 41
        self.collector.add_new_book(long_name)
        assert len(self.collector.get_books_genre()) == 0

    def test_add_new_book_with_valid_name(self):
        name = 'Маленький принц'
        self.collector.add_new_book(name)
        assert name in self.collector.get_books_genre()

    def test_set_book_genre_valid(self):
        self.collector.add_new_book('Мастер и Маргарита')
        self.collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        assert self.collector.get_book_genre('Мастер и Маргарита') == 'Фантастика'

    def test_set_book_genre_invalid_book(self):
        self.collector.set_book_genre('Несуществующая книга', 'Фантастика')
        # Жанр не должен устанавливаться для несуществующей книги
        assert self.collector.get_books_genre().get('Несуществующая книга') is None

    def test_set_book_genre_invalid_genre(self):
        self.collector.add_new_book('Книга')
        previous_genre = self.collector.get_book_genre('Книга')
        self.collector.set_book_genre('Книга', 'Неизвестный жанр')
        # Жанр не должен измениться
        assert self.collector.get_book_genre('Книга') == previous_genre == ''

    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book('Книга1')
        self.collector.set_book_genre('Книга1', 'Фантастика')
        self.collector.add_new_book('Книга2')
        self.collector.set_book_genre('Книга2', 'Ужасы')

        result = self.collector.get_books_with_specific_genre('Фантастика')
        assert 'Книга1' in result
        assert 'Книга2' not in result

    def test_get_books_for_children(self):
        # Добавляем книгу для детей (не в списке возрастных жанров)
        self.collector.add_new_book('Детская книга')
        self.collector.set_book_genre('Детская книга', 'Мультфильмы')

        # Добавляем книгу для взрослых (жанр "Ужасы")
        self.collector.add_new_book('Страшилка')
        self.collector.set_book_genre('Страшилка', 'Ужасы')

        result = self.collector.get_books_for_children()

        assert 'Детская книга' in result
        # Книги с жанром "Ужасы" не должны быть в списке
        assert 'Страшилка' not in result

    def test_add_and_delete_favorites(self):
        # Добавляем книгу и устанавливаем жанр
        book_name = 'Любимая книга'

        # Добавляем книгу
        self.collection = BooksCollector()

        # Обнуляем коллекцию перед тестом, чтобы избежать влияния предыдущих тестов
        if hasattr(self.collection, '_favorites_books'):
            self.collection._favorites_books.clear()

        # Добавляем книгу
        self.collection.add_new_book(book_name)

        # Добавляем в избранное
        self.collection.add_book_in_favorites(book_name)

        favorites = self.collection.get_list_of_favorites_books()

        # Проверяем, что книга есть в списке избранных
        assert book_name in favorites

        # --- Позитивная проверка: список содержит добавленную книгу ---

    favorites_list = favorites  # уже получен выше
    assert isinstance(favorites_list, list)
    assert book_name in favorites_list

    # Повторное добавление не должно увеличивать список
    previous_length = len(favorites_list)
    self.collection.add_book_in_favorites(book_name)
    assert len(self.collection.get_list_of_favorites_books()) == previous_length

    # Удаляем из избранного
    self.collection.delete_book_from_favorites(book_name)
    favorites_after_delete = self.collection.get_list_of_favorites_books()
    assert book_name not in favorites_after_delete


def test_delete_nonexistent_from_favorites(self):
    # Удаление книги, которой нет в избранных — ничего не произойдет без ошибок
    try:
        self.collection.delete_book_from_favorites('Некоторая книга')
        # Если исключение не возникло — тест прошел успешно
        pass
    except Exception:
        pytest.fail("Удаление несуществующей книги вызвало исключение")

        # Проверка, что список остался пустым (или не изменился)
    if hasattr(self.collection, '_favorites_books'):
        assert len(self.collection._favorites_books) == 0


def test_get_all_books_when_empty(self):
    # Проверка метода получения всех книг при пустой коллекции
    books = self.collection.get_books_genre()
    assert isinstance(books, dict)
    assert len(books) == 0


def test_add_multiple_books_and_retrieve_all(self):
    books_to_add = ['Книга А', 'Книга Б', 'Книга В']
    for book in books_to_add:
        self.collection.add_new_book(book)
    all_books = self.collection.get_books_genre()
    for book in books_to_add:
        assert book in all_books


def test_duplicate_addition_of_same_book(self):
    book_name = 'Повторная книга'
    self.collection.add_new_book(book_name)
    initial_count = len(self.collection.get_books_genre())

    # Попытка добавить ту же книгу еще раз — должна остаться одна запись
    self.collection.add_new_book(book_name)

    new_count = len(self.collection.get_books_genre())
    assert initial_count == new_count


def test_set_and_get_multiple_genres_for_different_books(self):
    books_and_genres = {
        'Книга1': 'Фантастика',
        'Книга2': 'Драма',
        'Книга3': ''
    }

    for book, genre in books_and_genres.items():
        if not book:
            continue
        if not genre:
            continue
        if not any(b['name'] == book for b in list(self.collection.get_books_genre().values())):
            self.collection.add_new_book(book)
        if genre:
            self.collection.set_book_genre(book, genre)

    for book, genre in books_and_genres.items():
        if genre:
            assert self.collection.get_book_genre(book) == genre
        else:
            # Для книг без жанра или с пустым жанром — возвращается ''
            assert self.collection.get_book_genre(book) == ''

