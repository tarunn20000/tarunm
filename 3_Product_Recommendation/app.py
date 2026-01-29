
from flask import Flask, render_template, request
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)

products = {
    "Phone": [200,4.5],
    "Laptop": [800,4.7],
    "Headphones": [50,4.0],
    "Camera": [500,4.6]
}

@app.route('/', methods=['GET','POST'])
def index():
    recs = []
    if request.method == 'POST':
        product = request.form['product']
        X = np.array(list(products.values()))
        model = KMeans(n_clusters=2, random_state=0).fit(X)
        labels = model.labels_
        selected_cluster = labels[list(products.keys()).index(product)]
        recs = [p for i,p in enumerate(products) if labels[i]==selected_cluster]
    return render_template('index.html', recs=recs, products=products)

if __name__ == '__main__':
    app.run(debug=True)
