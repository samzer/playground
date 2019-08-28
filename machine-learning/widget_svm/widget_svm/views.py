from flask import render_template, request
from widget_svm import app
from support_vector_machine import SupportVectorMachine

@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')


@app.route('/api',  methods=['POST'])
def api():
    data = request.json
    X,y = process_data(data)

    model = SupportVectorMachine()
    model.fit(X,y)



    return {
        'w': list(model.w.flatten()),
        'b': model.b
    }

def process_data(data):
    X = list()
    y = list()

    for i in data:
        for row in data[i]:
            X.append(row)
            y.append(int(i))

    return X,y
