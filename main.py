from flask import Flask, render_template, request

from result import Result

app = Flask(__name__)

#initialize request form web page
@app.route('/input', methods=['GET'])
def input():
    return render_template('index.html', title="Input page")

# calculate and display the pixel grid array
@app.route('/calculate', methods=['POST'])
def calculate():
    return Result(request.form).display()

if __name__ == '__main__':
    app.run(host='0.0.0.0')


