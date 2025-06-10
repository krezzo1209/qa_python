from main import BooksCollector
import pytest


class TestBooksCollector:

    def setup_method(self):
        # Создаем новый экземпляр перед каждым тестом
        self.collector = BooksCollector()

    def test_add_two_books_increases_collection(self):
        # Проверка добавления двух книг увеличивает коллекцию
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(self.collector.get_books_genre()) == 2

    def test_add_book_with_empty_name_does_not_add(self):
        # Проверка, что книга с пустым названием не добавляется
        self.collector.add_new_book('')
        assert len(self.collector.get_books_genre()) == 0

    def test_add_book_with_long_name_does_not_add(self):
        # Проверка, что книга с очень длинным названием не добавляется
        long_name = 'a' * 41
        self.collector.add_new_book(long_name)
        assert len(self.collector.get_books_genre()) == 0

    def test_add_valid_book_name(self):
        # Проверка, что валидное название книги добавляется
        name = 'Маленький принц'
        self.collector.add_new_book(name)
        books = self.collector.get_books_genre()
        assert name in books

    def test_set_valid_genre_for_existing_book(self):
        # Проверка установки жанра для существующей книги
        self.collector.add_new_book('Мастер и Маргарита')
        self.collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        assert self.collector.get_book_genre('Мастер и Маргарита') == 'Фантастика'

    def test_set_genre_for_nonexistent_book_does_not_create_entry(self):
        # Проверка, что жанр не устанавливается для несуществующей книги
        self.collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert self.collector.get_books_genre().get('Несуществующая книга') is None

    def test_set_invalid_genre_does_not_change_existing_genre(self):
        # Проверка, что при установке некорректного жанра жанр не меняется
        self.collector.add_new_book('Книга')
        previous_genre = self.collector.get_book_genre('Книга')
        self.collector.set_book_genre('Книга', 'Неизвестный жанр')
        assert self.collector.get_book_genre('Книга') == previous_genre == ''

    def test_get_books_with_specific_genre_returns_correct_books(self):
        # Проверка получения книг по конкретному жанру
        self.collector.add_new_book('Книга1')
        self.collector.set_book_genre('Книга1', 'Фантастика')
        self.collector.add_new_book('Книга2')
        self.collector.set_book_genre('Книга2', 'Ужасы')

        result = self.collector.get_books_with_specific_genre('Фантастика')
        assert 'Книга1' in result
        assert 'Книга2' not in result

    def test_get_books_for_children_excludes_adult_books(self):
        # Проверка получения книг для детей (без жанра "Ужасы")

        # Добавляем книгу для детей
        self.collector.add_new_book('Детская книга')
        self.collector.set_book_genre('Детская книга', 'Мультфильмы')

        # Добавляем книгу для взрослых
        self.collector.add_new_book('Страшилка')
        self.collector.set_book_genre('Страшилка', 'Ужасы')

        result = self.collector.get_books_for_children()

        assert 'Детская книга' in result
        assert 'Страшилка' not in result

    def test_add_and_remove_favorite_book(self):
        book_name = 'Любимая книга'

        # Обнуляем список избранных (если нужно)

    if hasattr(self.collector, '_favorites_books'):
        self.collector._favorites_books.clear()

        # Добавляем книгу в коллекцию и в избранное
    self.collector.add_new_book(book_name)
    self.collection.add_book_in_favorites(book_name)

    favorites = self.collection.get_list_of_favorites_books()

    # Проверяем, что книга есть в списке избранных
    assert book_name in favorites

    # Проверяем тип возвращаемого значения — список
    assert isinstance(favorites, list)

    # Повторное добавление не увеличит список
    previous_length = len(favorites)
    self.collection.add_book_in_favorites(book_name)
    assert len(self.collection.get_list_of_favorites_books()) == previous_length

    # Удаляем из избранного и проверяем отсутствие книги в списке
    self.collection.delete_book_from_favorites(book_name)
    favorites_after_delete = self.collection.get_list_of_favorites_books()
    assert book_name not in favorites_after_delete


def test_delete_nonexistent_from_favorites_does_not_raise_exception(self):
    # Удаление несуществующей книги — должно пройти без ошибок
    try:
        self.collection.delete_book_from_favorites('Некоторая книга')
    except Exception:
        pytest.fail("Удаление несуществующей книги вызвало исключение")

    # Можно дополнительно проверить, что список остался пустым или неизменным (если есть такая логика)
    if hasattr(self.collection, '_favorites_books'):
        assert len(self.collection._favorites_books) == 0


def test_get_all_books_when_empty_returns_empty_dict(self):
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


def test_duplicate_addition_does_not_duplicate_entry(self):
    book_name = 'Повторная книга'
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