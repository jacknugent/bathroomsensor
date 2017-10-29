##run on computer, simulates the distance  
import time
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    dist = 60
    if dist < 70:
        return render_template('open.html', value = dist)
    else:
        return render_template('closed.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
