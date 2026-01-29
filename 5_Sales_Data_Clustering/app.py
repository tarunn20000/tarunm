
from flask import Flask, render_template, request
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    cluster = None
    if request.method == 'POST':
        sales = float(request.form['sales'])
        price = float(request.form['price'])

        X = np.array([[100,10],[300,20],[800,50]])
        model = KMeans(n_clusters=3, random_state=0).fit(X)
        cluster = model.predict([[sales,price]])[0]

    return render_template('index.html', cluster=cluster)

if __name__ == '__main__':
    app.run(debug=True)
