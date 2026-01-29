
from flask import Flask, render_template, request
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    cluster = None
    if request.method == 'POST':
        income = float(request.form['income'])
        score = float(request.form['score'])

        X = np.array([[15,39],[20,81],[30,6],[40,77],[55,40]])
        model = KMeans(n_clusters=3, random_state=0).fit(X)
        cluster = model.predict([[income,score]])[0]

    return render_template('index.html', cluster=cluster)

if __name__ == '__main__':
    app.run(debug=True)
