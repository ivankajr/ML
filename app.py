from flask import Flask, render_template, request, redirect
application = Flask(__name__)

@application.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':

        return render_template('hasil.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    application.run(debug=True)