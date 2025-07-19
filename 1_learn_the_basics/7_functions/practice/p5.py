books = []


def add_book(title, author):
    """اضافه کردن کتاب جدید"""
    books.append({"title": title, "author": author})
    return f"کتاب '{title}' اضافه شد."


def find_book(title):
    """یافتن کتاب بر اساس عنوان"""
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    return None


def list_books():
    """نمایش همه کتاب‌ها"""
    if not books:
        return "کتابی وجود ندارد."
    return "\n".join(
        f"{i+1}. {b['title']} - {b['author']}" for i, b in enumerate(books)
    )


# تست سیستم
print(add_book("پایتون پیشرفته", "جان دو"))
print(add_book("یادگیری ماشین", "جین اسمیت"))
print(list_books())
print(find_book("پایتون پیشرفته"))
