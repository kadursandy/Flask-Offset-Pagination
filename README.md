# Flask-Offset-Pagination
Flask Pagination Example

This example demonstrates flask sql alchemy pagination with a books example.

Create a db with books.db and books table
Populate the books table for illustration

run> python sample_data.py 

Click below links to paginate

```
  http://localhost:5000/books
  http://localhost:5000/books?limit=20&offset=2
  http://localhost:5000/books?limit=10&offset=3
