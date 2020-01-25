from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def to_obj(self):
        return {
            "id": self.id,
            "title": self.title,
            "timestamp": self.timestamp
        }

@app.route('/books')
def books():
    page_num = request.args.get('offset', None)
    limit = request.args.get('limit', None)
    if page_num is None and limit is None:
        books_store_list = Books.query.paginate(per_page=limit, page=page_num, error_out=True)
    else:
        books_store_list = Books.query.paginate(per_page=int(limit), page=int(page_num), error_out=True)

    no_of_pages = books_store_list.pages
    next_page = books_store_list.next_num
    prev_page = books_store_list.prev_num
    current_page = books_store_list.page
    default_per_page = books_store_list.per_page

    max_limit = 10
    if limit is None:
        limit = default_per_page
    else:
        if int(limit) > max_limit:
            limit = max_limit

    url = request.url
    base_url = request.base_url

    if books_store_list.has_next:
        next_url = f"{base_url}?offset={next_page}&limit={limit}"
    else:
        next_url = url

    if books_store_list.has_prev:
        previous_url = f"{base_url}?offset={prev_page}&limit={limit}"
    else:
        previous_url = url

    return {
        "books_store": [book.to_obj() for book in books_store_list.items],
        "meta": {
            "pageSize": limit
        },
        "links": {
            "self": url,
            "next": next_url,
            "previous": previous_url
        }
    }


if __name__ == '__main__':
    app.run(debug=True)