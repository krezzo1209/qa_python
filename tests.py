from main import BooksCollector
import pytest




class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # Проверяем, что добавилось именно две книги
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_with_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        # Пустое название не должно добавляться
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_with_long_name(self):
        collector = BooksCollector()
        long_name = 'a' * 41  # длина 41 символа
        collector.add_new_book(long_name)
        # Название длиной 41 символа не должно добавляться
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        assert collector.get_book_genre('Мастер и Маргарита') == 'Фантастика'

    def test_set_book_genre_invalid_book(self):
        collector = BooksCollector()
        # Попытка установить жанр для несуществующей книги
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        # Жанр для несуществующей книги не должен устанавливаться
        assert collector.get_books_genre().get('Несуществующая книга') is None

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        # Попытка установить жанр, которого нет в списке допустимых
        collector.set_book_genre('Книга', 'Неизвестный жанр')
        # Жанр не должен измениться (оставаться пустым)
        assert collector.get_book_genre('Книга') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга2', 'Ужасы')

        result = collector.get_books_with_specific_genre('Фантастика')
        assert 'Книга1' in result
        assert 'Книга2' not in result

    def test_get_books_for_children(self):
        collector = BooksCollector()

        # Добавляем книгу для детей (не в списке возрастных жанров)
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')

        # Добавляем книгу для взрослых (жанр "Ужасы")
        collector.add_new_book('Страшилка')
        collector.set_book_genre('Страшилка', 'Ужасы')

        result = collector.get_books_for_children()

        assert 'Детская книга' in result
        assert 'Страшилка' not in result

    def test_add_and_delete_favorites(self):
        collector = BooksCollector()

        # Добавляем книгу и устанавливаем жанр
        collector.add_new_book('Любимая книга')






    def test_add_and_delete_favorites(self):
        # Создаем экземпляр коллектора
        collector = BooksCollector()

        # Добавляем книгу и устанавливаем жанр
        collector.add_new_book('Любимая книга')


        # Добавляем в избранное
        collector.add_book_in_favorites('Любимая книга')

        favorites = collector.get_list_of_favorites_books()
        previous_length = len(favorites)

        assert 'Любимая книга' in favorites


        # Повторное добавление не изменит список
        collector.add_book_in_favorites('Любимая книга')
        assert len(collector.get_list_of_favorites_books()) == previous_length

        # Удаляем из избранного
        collector.delete_book_from_favorites('Любимая книга')
        assert 'Любимая книга' not in collector.get_list_of_favorites_books()

    def test_delete_nonexistent_from_favorites(self):
        # Удаление книги, которой нет в избранных — ничего не произойдет без ошибок
        collector = BooksCollector()
        try:
            collector.delete_book_from_favorites('Некоторая книга')
        except Exception:
            pytest.fail("Удаление несуществующей книги вызвало исключение")
        # Проверка, что список остался пустым
        assert len(collector.get_list_of_favorites_books()) == 0

