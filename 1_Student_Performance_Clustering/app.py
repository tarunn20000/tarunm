
from flask import Flask, render_template, request
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    cluster = None
    if request.method == 'POST':
        hours = float(request.form['hours'])
        attendance = float(request.form['attendance'])
        marks = float(request.form['marks'])

        X = np.array([[2,60,40],[4,70,60],[6,80,75],[8,90,90]])
        model = KMeans(n_clusters=3, random_state=0).fit(X)
        cluster = model.predict([[hours,attendance,marks]])[0]

    return render_template('index.html', cluster=cluster)

if __name__ == '__main__':
    app.run(debug=True)
