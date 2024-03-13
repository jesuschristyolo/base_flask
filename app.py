from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clothing')
def clothing():
    return render_template('clothing.html')


@app.route('/shoes')
def shoes():
    return render_template('shoes.html')


@app.route('/jacket')
def jacket():
    return render_template('jacket.html')


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        response = make_response(render_template('welcome.html', name=name))
        response.set_cookie('user_data', {'name': name, 'email': email})
        return response
    return redirect('/')


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('user_data', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
