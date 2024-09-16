from flask import Flask, render_template, request

app = Flask(__name__)

characters = {
    "Globin": {
        "Life": 20,
        "Armor": 5,
        "Damage": 10
    },
    "Orc": {
        "Life": 30,
        "Armor": 10,
        "Damage": 15
    },
    "Elf": {
        "Life": 15,
        "Armor": 3,
        "Damage": 12
    }
}

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search', methods=['GET'])
def search_character():
    name = request.args.get('name')
    
    character = characters.get(name)
    
    if character:
        return render_template('character.html', name=name, character=character)
    else:
        return render_template('character.html', error="Character not found")

if __name__ == '__main__':
    app.run(debug=True)
