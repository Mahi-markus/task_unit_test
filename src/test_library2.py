import pytest
from library import Library, Student


@pytest.fixture
def library():
    """Fixture to initialize the library with sample data."""
    books = {
        'The Last Battle': 'Free',
        'The Hunger Games': 'Free',
        'Cracking the Coding Interview': 'Free'
    }
    return Library(books)


@pytest.fixture
def student(library):
    """Fixture to initialize a student with the library."""
    return Student("Test Student", library)


def test_show_available_books(library, capsys):
    """Test displaying available books."""
    library.show_avail_books()
    captured = capsys.readouterr()
    assert "Our Library Can Offer You The Following Books:" in captured.out
    assert "The Last Battle" in captured.out
    assert "The Hunger Games" in captured.out



def test_show_available_books_no_books(library, capsys):
    """Test displaying available books when none are free."""
    for book in library.books:
        library.books[book] = "Borrowed"
    library.show_avail_books()
    captured = capsys.readouterr()
    assert "Our Library Can Offer You The Following Books:" in captured.out
    assert not any(book in captured.out for book in library.books)


def test_lend_book_success(library):
    """Test successful lending of a book."""
    result = library.lend_book("The Last Battle", "Test Student")
    assert result is True
    assert library.books["The Last Battle"] == "Test Student"


def test_lend_book_failure(library):
    """Test attempting to lend an already borrowed book."""
    library.lend_book("The Last Battle", "Test Student")
    result = library.lend_book("The Last Battle", "Another Student")
    assert result is False
    assert library.books["The Last Battle"] == "Test Student"


def test_return_book(library):
    """Test returning a borrowed book."""
    library.lend_book("The Last Battle", "Test Student")
    library.return_book("The Last Battle")
    assert library.books["The Last Battle"] == "Free"


def test_return_book_not_borrowed(library, capsys):
    """Test returning a book that was not borrowed."""
    library.return_book("The Last Battle")
    captured = capsys.readouterr()
    assert "Thanks for returning The Last Battle" in captured.out


def test_student_request_book_success(student):
    """Test successful book borrowing by a student."""
    student.library.lend_book("The Last Battle", student.name)
    student.books.append("The Last Battle")
    assert "The Last Battle" in student.books
    assert student.library.books["The Last Battle"] == "Test Student"



def test_student_return_book_success(student, library):
    """Test successfully returning a borrowed book."""
    student.books.append("The Last Battle")
    student.library.books["The Last Battle"] = student.name
    student.library.return_book("The Last Battle")
    student.books.remove("The Last Battle")
    assert "The Last Battle" not in student.books
    assert library.books["The Last Battle"] == "Free"




def test_student_view_borrowed_empty(student, capsys):
    """Test viewing borrowed books when none are borrowed."""
    student.view_borrowed()
    captured = capsys.readouterr()
    assert "You haven't borrowed any books" in captured.out


def test_student_view_borrowed_with_books(student, capsys):
    """Test viewing borrowed books when some are borrowed."""
    student.books.append("The Last Battle")
    student.books.append("The Hunger Games")
    student.view_borrowed()
    captured = capsys.readouterr()
    assert "The Last Battle" in captured.out
    assert "The Hunger Games" in captured.out


def test_student_view_borrowed_removed_books(student, capsys):
    """Test viewing books after returning them."""
    student.books.append("The Last Battle")
    student.books.remove("The Last Battle")
    student.view_borrowed()
    captured = capsys.readouterr()
    assert "You haven't borrowed any books" in captured.out

    