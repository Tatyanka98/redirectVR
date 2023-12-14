from flask import Flask, redirect, render_template, request

app = Flask(__name__)

url_vr = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'

@app.route('/')
def index():
    return redirect(url_vr)

@app.route('/setting', methods=['GET','POST'])
def settings():
    if request.method == 'POST':
        global url_vr
        url_vr = request.form['url_vr']
        return redirect('/end')
    else:
        return render_template('set.html')
@app.route('/end')
def done():
    return "Все готово"
if __name__ == '__main__':
    app.run(debug=True)