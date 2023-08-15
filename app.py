import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/submit', methods=['POST'])
def message():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args['name']
    return f"I am waving at {name}"

@app.route('/count_vowels', methods=['POST'])
def counter():
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = request.form['text']
    number_of_vowels = 0
    for letter in text:
        if letter in vowels:
            number_of_vowels += 1
    return f'There are {number_of_vowels} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def sort_names():
    list_of_names = request.form['names'].split(',')
    sorted_list = ','.join(sorted(list_of_names))
    return f"{sorted_list}"

@app.route('/names', methods=['GET'])
def get_name():
    name = request.args['add']
    return f'Julia, Alice, Karim, {name}'

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

