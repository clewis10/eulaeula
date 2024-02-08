# main.py
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':
        form_data = request.form
        search = form_data.get('search')
        if search == 'google':
            google_data = ['1', '2', '3', '4']
            return render_template('data.html', form_data=form_data, context=google_data)
        elif search == 'tiktok':
            tiktok_data = ['a', 'b', 'c', 'd']
            return render_template('data.html', form_data=form_data, context=tiktok_data)
        else:
            return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)

