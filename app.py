from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy dictionary (multilingual support)
dictionary = {
    'english': {
        'apple': 'A round fruit with red or green skin.',
        'python': 'A programming language or a type of snake.'
    },
    'tamil': {
        'apple': 'செம்பழம் (செம்மண்ணில் விளையும் பழம்)',
        'python': 'பைத்தான் என்பது ஒரு நிரலாக்க மொழி.'
    }
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    word = request.form.get('word', '').lower()
    lang = request.form.get('lang', 'english').lower()
    return redirect(url_for('word_detail', searched_word=word, lang=lang))

@app.route('/word/<searched_word>')
def word_detail(searched_word):
    lang = request.args.get('lang', 'english').lower()
    definition = dictionary.get(lang, {}).get(searched_word)
    return render_template('word.html', word=searched_word, definition=definition, lang=lang)

if __name__ == '__main__':
    app.run(debug=True)
