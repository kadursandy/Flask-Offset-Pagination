from app import db, Books
from faker import Faker
fake = Faker()

# create the table books
# db.create_all()

# store 800 book titles
for i in range(1, 801):
    title = fake.sentence()
    book = Books(title=title)
    print('Adding Book ', book)
    db.session.add(book)
    db.session.commit()

