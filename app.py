from flask import *
import re

app = Flask(__name__)

@app.route('/')
def surya():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    email=  request.form[' email']
    matches = re.findall(regex_pattern, test_string,email)

    return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, email=email,matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
