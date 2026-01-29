
from flask import Flask, render_template, request
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    cluster = None
    if request.method == 'POST':
        time = float(request.form['time'])
        pages = float(request.form['pages'])

        X = np.array([[1,2],[5,10],[10,20]])
        model = KMeans(n_clusters=3, random_state=0).fit(X)
        cluster = model.predict([[time,pages]])[0]

    return render_template('index.html', cluster=cluster)

if __name__ == '__main__':
    app.run(debug=True)
