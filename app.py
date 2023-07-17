from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Data storage (can be replaced with a database in a production environment)
books = []
members = []


# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Book management routes
@app.route('/books', methods=['GET', 'POST'])
def book_management():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        quantity = int(request.form['quantity'])
        book = {'title': title, 'author': author, 'quantity': quantity}
        books.append(book)
        return redirect('/books')
    else:
        return render_template('books.html', books=books)


@app.route('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    del books[book_id]
    return redirect('/books')


# Member management routes
@app.route('/members', methods=['GET', 'POST'])
def member_management():
    if request.method == 'POST':
        name = request.form['name']
        initial_debt = int(request.form['initial_debt'])
        member = {'name': name, 'debt': 0}
        members.append(member)
        return redirect('/members')
    else:
        return render_template('members.html', members=members)

@app.route('/members/delete/<int:member_id>', methods=['POST'])
def delete_member(member_id):
    del members[member_id]
    return redirect('/members')



if __name__ == '__main__':
    app.run(debug=True)
